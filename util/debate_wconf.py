from .data_loader import load_jsonl_data
from .language_assistants import LoadModel
from .config.model_info import model_info
from .prompt import (
    grade_school_math_prompt, 
    strategyqa_prompt,
    self_conf_elicit_prompt_ground_truth
)
from .debate_agents import Debator
from .config.debater import debaters
from .config import datapath

from tqdm import tqdm
import json
import datetime
import os

model_loaded = {}
current_timestamp = datetime.datetime.now().strftime('%H_%M_%S')
current_timestamp_day = datetime.datetime.now().strftime('%Y_%m_%d')

def ExtractAnswerGSM(answer):
    gt_answer = answer.split("#### ")[1]
    return gt_answer


def ExtractAnswerStrategyQA(answer):
    return answer


def LoadDebateAgents(args):
    debate_agents = []
    for agent_name, agent_info in debaters.items():
        debater_model_info = model_info[agent_info["model"]]
        debater_model_info["name"] = agent_name
        if debater_model_info["model_name"] in model_loaded:
            model = model_loaded[debater_model_info["model_name"]]
        else:
            model = LoadModel(debater_model_info)
        d = Debator(
            agent_name=agent_name,
            model=model,
            agent_info=agent_info,
            use_role=True
        )
        debate_agents.append(d)
    return debate_agents[:args.debate_agents]


def LoadAssistantModel(assistant):
    if assistant in model_loaded:
        model = model_loaded[assistant]
    else:
        a_model_info = model_info[assistant]
        a_model_info["name"] = "assistant"
        model = LoadModel(a_model_info)
        model_loaded[assistant] = model
    return model


def LoadAssistantModels(args):
    asst_1 = LoadAssistantModel(args.assistant_1)
    asst_2 = LoadAssistantModel(args.assistant_2)
        
    return asst_1, asst_2

        
def GSMDebateOneByOne(args):
    # 'prompt' is for chating assistant, not for debaters, this is the same as GSMDebateCompare()
    data_path = datapath.GSM_dataset_path
    GSM_data = load_jsonl_data(data_path)
    debate_history = []
    
    # Load the debate agents
    debate_agents = LoadDebateAgents(args)
    debate_prompts = self_conf_elicit_prompt_ground_truth[args.self_elicit]
    
    # Iterate over the GSM dataset
    for item in tqdm(GSM_data[:500], desc="Debating..."):
        
        # Result list for GSM debating
        result = {
            "question": item["question"],
            "ground_truth": ExtractAnswerGSM(item["answer"]),
            "prompting_scheme": args.self_elicit,
            "debate_agents": [debater.agent_name for debater in debate_agents],
            "debate_turns": args.debate_turns,
            "debate_history": [],
        }
        
        history = []
        for _ in range(args.debate_turns):
            for debater in debate_agents:
                if len(history) == 0:
                    # No chat history, we do initial debate
                    prompt = debate_prompts["init"]
                    system_prompt = prompt["system"].format(
                        debater=debater.agent_name
                    )
                    user_prompt = prompt["user"].format(
                        question=item["question"]
                    )
                    debate_response, messages = debater.debate(system_prompt, user_prompt)
                    history.append({
                        "agent_name": debater.agent_name,
                        "agent_model": debater.model.model,
                        "prompt": messages,
                        "response": debate_response
                    })
                else:
                    # Debate afterwards
                    prompt = debate_prompts["debate"]
                    system_prompt = prompt["system"].format(
                        debater=debater.agent_name
                    )
                    history_str = "\n".join([f"{item['agent_name']}:\n{item['response']}" for item in history])
                    user_prompt = prompt["user"].format(
                        question=item["question"],
                        debate_history=history_str
                    )
                    debate_response, formatted_prompt = debater.debate(system_prompt, user_prompt)
                    history.append({
                        "agent_name": debater.agent_name,
                        "agent_model": debater.model.model,
                        "prompt": formatted_prompt,
                        "response": debate_response
                    })


        result["debate_history"] = history
        debate_history.append(result)
        
    path = os.path.join(args.output_dir, "GSM", current_timestamp_day)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, current_timestamp + ".json"), "w") as f:
        json.dump(debate_history, f, indent=4)
        

def StrategyQADebateOneByOne(args):
    pass