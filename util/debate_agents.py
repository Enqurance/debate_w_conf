from .prompt import self_conf_elicit_prompt_ground_truth, self_conf_elicit_prompt_free_form
from .config.debater import role_prompts


class Debator():
    
    def __init__(self, agent_name, model, agent_info, use_role=False):
        self.agent_name = agent_name
        self.model = model
        self.use_role = use_role
        self.agent_info = agent_info
        
    
    # This function is for debate mode dual, you may refer to the params of this function
    # This function has two responses for input, so this is for debate mode dual
    def debate(self, prompt, question, a1_response, a2_response, chat_history):
        chat_history_str = ""
        for item in chat_history:
            chat_history_str += f"{item['agent_name']}: {item['response']}\n"
            
        system_prompt = prompt["system"].format(
            question = question,
            response_one = a1_response,
            response_two = a2_response,
            chat_history = chat_history_str,
            role_description = role_prompts[self.agent_info["role_description"]] if self.use_role else "",
        )
        
        user_prompt = prompt["user"].format(
            agent_name = self.agent_info["agent_name"]
        )

        response, messages = self.generate_response(system_prompt, user_prompt)
        return response, messages
    
    # This function is for debate mode single, you may refer to the params of this function
    # This function has only one response for input, so this is for debate mode single
    def debate(self, prompt, question, response, chat_history):
        chat_history_str = ""
        for item in chat_history:
            chat_history_str += f"{item['agent_name']}: {item['response']}\n"
            
        system_prompt = prompt["system"].format(
            question = question,
            response = response,
            chat_history = chat_history_str,
            role_description = role_prompts[self.agent_info["role_description"]] if self.use_role else "",
        )
        
        user_prompt = prompt["user"].format(
            agent_name = self.agent_info["agent_name"]
        )

        response, messages = self.generate_response(system_prompt, user_prompt)
        return response, messages
    
    
    def generate_response(self, system_prompt, user_prompt):
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        response = self.model.generate_response(messages)
        return response, messages