class Debator():
    
    def __init__(self, agent_name, role_description, model):
        self.agent_name = agent_name
        self.role_description = role_description
        self.chat_history = []
        self.model = model
        
        self.question = None  
        self.a1_response = None
        self.a2_response = None
        
    
    
    def set_debate_content(self, question, a1_response, a2_response):
        self.question = question
        self.a1_response = a1_response
        self.a2_response = a2_response
        
    
    def clean_history(self):
        self.chat_history = []