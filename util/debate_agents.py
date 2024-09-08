from .prompt import self_conf_elicit_prompt_ground_truth, self_conf_elicit_prompt_free_form
from .config.debater import role_prompts


class Debator():
    
    def __init__(self, agent_name, model, agent_info, use_role=False):
        self.agent_name = agent_name
        self.model = model
        self.use_role = use_role
        self.agent_info = agent_info
        
    
    def debate(self, prompt, question, a1_response, a2_response, chat_history):
        chat_history_str = ""
        for item in chat_history:
            chat_history_str += f"{item['agent_name']}: {item['response']}\n"
        
        formatted_prompt = prompt.format(
            question = question,
            response_one = a1_response,
            response_two = a2_response,
            chat_history = chat_history_str,
            role_description = role_prompts[self.agent_info["role_description"]] if self.use_role else "",
            agent_name = self.agent_info["agent_name"]
        )

        messages = [
            {"role": "system", "content": formatted_prompt},
            {"role": "user", "content": a1_response}
        ]
        response = self.model.generate_response(messages)
        return response, formatted_prompt