from .data_loader import load_jsonl_data
from .language_assistants import LoadModelAssistant
from .config.model_info import model_info
from .prompt import grade_school_math_prompt, debate_prompt_ground_truth
from .debate_agents import Debator
from .config.debater import debaters

import json

model_loaded = {}


def GSMDebate(args):
    prompt = grade_school_math_prompt
    data_path = "./data/GSM/GSM_test.jsonl"
    GSM_data = load_jsonl_data(data_path)


    # Load the assistant models
    if args.assistant_1 in model_loaded:
        asst_1 = model_loaded[args.assistant_1]
    else:
        a1_model_info = model_info[args.assistant_1]
        a1_model_info["name"] = "assistant_1"
        asst_1 = LoadModelAssistant(a1_model_info)
        model_loaded[args.assistant_1] = asst_1

    if args.assistant_2 in model_loaded:
        asst_2 = model_loaded[args.assistant_2]
    else:
        a2_model_info = model_info[args.assistant_2]
        a2_model_info["name"] = "assistant_2"
        asst_2 = LoadModelAssistant(a2_model_info)
        model_loaded[args.assistant_2] = asst_2
    
    # TODO: Load the debate agents
    assert args.debate_agents == len(debaters)
    debate_agents = []
    for agent_name, agent_info in debaters.items():
        debater_model_info = model_info[agent_info["model"]]
        debater_model_info["name"] = agent_name
        if debater_model_info["model_name"] in model_loaded:
            model = model_loaded[debater_model_info["model_name"]]
        else:
            model = LoadModelAssistant(debater_model_info)
        d = Debator(
            agent_name=agent_name,
            model=model,
            agent_info=agent_info,
            use_role=True
        )
        debate_agents.append(d)
    
    for item in GSM_data[:1]:
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": item["question"]}
        ]
        
        response_1 = asst_1.generate_response(messages)
        response_2 = asst_2.generate_response(messages)
        
        chat_history = []
        
        for _ in range(args.debate_turns):
            for debater in debate_agents:
                debate_response, formatted_prompt = debater.debate(debate_prompt_ground_truth, item["question"], response_1, response_2, chat_history)
                chat_history.append({
                    "agent_name": debater.agent_name,
                    "prompt": formatted_prompt,
                    "response": debate_response
                })

        with open("./result/chat_history.json", "w") as f:
            json.dump(chat_history, f, indent=4)