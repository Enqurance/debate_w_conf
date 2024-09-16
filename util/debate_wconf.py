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
    assert args.debate_agents == len(debaters)
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
    return debate_agents


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


def GSMDebateCompare(args):
    # 'prompt' is for chating assistant, not for debaters
    prompt = grade_school_math_prompt
    data_path = datapath.GSM_dataset_path
    GSM_data = load_jsonl_data(data_path)
    debate_history = []
    
    # Load the assistant models
    asst_1, asst_2 = LoadAssistantModels(args)
    
    # Load the debate agents
    debate_agents = LoadDebateAgents(args)
    debate_prompts = self_conf_elicit_prompt_ground_truth[args.self_elicit]
    
    # Iterate over the GSM dataset
    for item in tqdm(GSM_data, desc="Debating..."):
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": item["question"]}
        ]
        
        response_1 = asst_1.generate_response(messages)
        response_2 = asst_2.generate_response(messages)
        
        result = {
            "question": item["question"],
            "ground_truth": ExtractAnswerGSM(item["answer"]),
            "assistant_model_1": args.assistant_1,
            "assistant_model_2": args.assistant_2,
            "prompting_scheme": args.self_elicit,
            "response_1": response_1,
            "response_2": response_2,
            "chat_history": []
        }
        chat_history = []
        
        for _ in range(args.debate_turns):
            for debater in debate_agents:
                # time.sleep(0.1)
                debate_response, formatted_prompt = debater.debate(debate_prompts, item["question"], response_1, response_2, chat_history)
                chat_history.append({
                    "agent_name": debater.agent_name,
                    "agent_model": debater.model.model,
                    "prompt": formatted_prompt,
                    "response": debate_response
                })

        result["chat_history"] = chat_history
        debate_history.append(result)
        
    path = os.path.join(args.output_dir, "GSM", current_timestamp_day)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, current_timestamp + ".json"), "w") as f:
        json.dump(debate_history, f, indent=4)
        
        
def GSMDebateSingle(args):
    # 'prompt' is for chating assistant, not for debaters, this is the same as GSMDebateCompare()
    prompt = grade_school_math_prompt
    data_path = datapath.GSM_dataset_path
    GSM_data = load_jsonl_data(data_path)
    debate_history = []
    
    # Load the assistant models
    asst = LoadAssistantModel(args.assistant_1)
    
    # Load the debate agents
    debate_agents = LoadDebateAgents(args)
    debate_prompts = self_conf_elicit_prompt_ground_truth[args.self_elicit]
    
    # Iterate over the GSM dataset
    for item in tqdm(GSM_data[:100], desc="Debating..."):
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": item["question"]}
        ]
        
        response = asst.generate_response(messages)
        
        result = {
            "question": item["question"],
            "ground_truth": ExtractAnswerGSM(item["answer"]),
            "assistant_model": args.assistant_1,
            "prompting_scheme": args.self_elicit,
            "response": response,
            "chat_history": []
        }
        chat_history = []
        
        # Debating here
        for _ in range(args.debate_turns):
            for debater in debate_agents:
                debate_response, formatted_prompt = debater.debate(debate_prompts, item["question"], response, chat_history)
                chat_history.append({
                    "agent_name": debater.agent_name,
                    "agent_model": debater.model.model,
                    "prompt": formatted_prompt,
                    "response": debate_response
                })

        result["chat_history"] = chat_history
        debate_history.append(result)
        
    path = os.path.join(args.output_dir, "GSM", current_timestamp_day)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, current_timestamp + ".json"), "w") as f:
        json.dump(debate_history, f, indent=4)
        

def StrategyQADebateCompare(args):
    pass


def StrategyQADebateSingle(args):
    # 'prompt' is for chating assistant, not for debaters
    prompt = strategyqa_prompt
    data_path = datapath.StrategyQA_dataset_path
    StrategyQA_data = load_jsonl_data(data_path)
    debate_history = []
    
    # Load the assistant models
    asst = LoadAssistantModel(args.assistant_1)
    
    # Load the debate agents
    debate_agents = LoadDebateAgents(args)
    debate_prompts = self_conf_elicit_prompt_ground_truth[args.self_elicit]
    
    # Iterate over the StrategyQA dataset
    for item in tqdm(StrategyQA_data[:100], desc="Debating..."):
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": item["question"]}
        ]
        
        response = asst.generate_response(messages)
        
        result = {
            "question": item["question"],
            "ground_truth": ExtractAnswerStrategyQA(item["answer"]),
            "assistant_model": args.assistant_1,
            "prompting_scheme": args.self_elicit,
            "response": response,
            "chat_history": []
        }
        chat_history = []
        
        # Debate here
        for _ in range(args.debate_turns):
            for debater in debate_agents:
                debate_response, formatted_prompt = debater.debate(debate_prompts, item["question"], response, chat_history)
                chat_history.append({
                    "agent_name": debater.agent_name,
                    "agent_model": debater.model.model,
                    "prompt": formatted_prompt,
                    "response": debate_response
                })

        result["chat_history"] = chat_history
        debate_history.append(result)
        
    path = os.path.join(args.output_dir, "StrategyQA", current_timestamp_day)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, current_timestamp + ".json"), "w") as f:
        json.dump(debate_history, f, indent=4)