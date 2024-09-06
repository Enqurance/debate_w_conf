from .data_loader import load_jsonl_data
from .language_assistants import LoadModelAssistant
from .model_info import model_info
from .prompt import grade_school_math_prompt


def GSMDebate(args):
    prompt = grade_school_math_prompt
    data_path = "./data/GSM/GSM_test.jsonl"
    GSM_data = load_jsonl_data(data_path)
    
    
    # Load the assistants models
    a1_model_info = model_info[args.assistant_1]
    a1_model_info["name"] = "assistant_1"
    a2_model_info = model_info[args.assistant_2]
    a2_model_info["name"] = "assistant_2"
    
    asst_1 = LoadModelAssistant(a1_model_info)
    asst_2 = LoadModelAssistant(a2_model_info)
    
    for item in GSM_data[:1]:
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": item["question"]}
        ]
        response_1 = asst_1.generate_response(messages)
        response_2 = asst_2.generate_response(messages)
        
        
        
    