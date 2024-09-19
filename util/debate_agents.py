from .prompt import self_conf_elicit_prompt_ground_truth, self_conf_elicit_prompt_free_form
from .config.debater import role_prompts


class Debator():
    
    def __init__(self, agent_name, model, agent_info, use_role=False):
        self.agent_name = agent_name
        self.model = model
        self.use_role = use_role
        self.agent_info = agent_info
        
    
    # This function is for initial debate, thus the parameters do not include the debate history
    def debate(self, system_prompt, user_prompt):
        response, messages = self.generate_response(system_prompt, user_prompt)
        return response, messages
    
    
    def generate_response(self, system_prompt, user_prompt):
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        response = self.model.generate_response(messages)
        return response, messages