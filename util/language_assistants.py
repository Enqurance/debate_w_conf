import os
import openai
import anthropic
import transformers

from util.prompt import assistant_prompts


class LanguageAssistant():
    def __init__(self, name, model):
        self.name = name
        self.model = model
        
    
    def generate_response(self):
        pass


class OpenAIAssistant(LanguageAssistant):
    def __init__(self, name, model, api_key=None, base_url=None, kwargs={}):
        super().__init__(name, model)
        self.api_key = api_key
        self.base_url = base_url
        self.openai_client = None
        self.kwargs = kwargs
        
        if api_key is None:
            raise ValueError("OPENAI_API_KEY must be provided if using openai models")
        elif base_url is None:
            self.openai_client = openai.OpenAI(
                api_key=self.api_key
            )
        else:
            self.openai_client = openai.OpenAI(
                api_key=self.api_key,
                base_url=self.base_url
            )
            
    def generate_response(self, messages):
        super().generate_response()
        response = self.openai_client.chat.completions.create(
            model=self.model,
            messages=messages,
            **self.kwargs
        )
        
        return response.choices[0].message.content
    

class LLaMAAssistant(LanguageAssistant):
    def __init__(self, name, model, model_path, kwargs={}):
        super().__init__(name, model)
        self.model_path = model_path
        self.kwargs = kwargs
        self.pipeline = transformers.pipeline(
            "text-generation",
            model=self.model_path,
            model_kwargs=self.kwargs,
        )

        
    def generate_response(self, messages):
        super().generate_response()
        outputs = self.pipeline(
            messages,
            max_new_tokens=512,
            kwargs=self.kwargs
        )
        
        return outputs[0]["generated_text"][-1]["content"]
    
    
class ClaudeAssistant(LanguageAssistant):
    def __init__(self, name, model, api_key=None, base_url=None, kwargs={}):
        super().__init__(name, model)
        self.api_key = api_key
        self.base_url = base_url
        self.openai_client = None
        self.kwargs = kwargs
        
        if api_key is None:
            raise ValueError("ANTHROPIC_API_KEY must be provided if using claude models")
        elif base_url is None:
            self.anthropic_client = anthropic.Anthropic(
                api_key=self.api_key
            )
        else:
            self.anthropic_client = anthropic.Anthropic(
                api_key=self.api_key,
                base_url=self.base_url
            )
            
    def generate_response(self, messages):
        super().generate_response()
        system_prompt = messages[0]["content"]
        messages = messages[1:]
        response = self.anthropic_client.messages.create(
            model=self.model,
            system=system_prompt,
            messages=messages,
            max_tokens=self.kwargs["max_tokens"]
        )
        
        return response.content[0].text


def LoadModelAssistant(model_info):
    if "llama" in model_info["model_name"].lower():
        return LLaMAAssistant(
            model_info["name"],
            model_info["model_name"],
            model_info["model_path"],
            kwargs=model_info["kwargs"]
        )
    elif "gpt" in model_info["model_name"].lower():
        if model_info["api_key"] is None:
            model_info["api_key"] = os.getenv("OPENAI_API_KEY")
        return OpenAIAssistant(
            model_info["name"],
            model_info["model_name"],
            model_info["api_key"],
            model_info["base_url"],
            kwargs=model_info["kwargs"]
        )
    elif "claude" in model_info["model_name"].lower():
        if model_info["api_key"] is None:
            model_info["api_key"] = os.getenv("ANTHROPIC_API_KEY")
        return ClaudeAssistant(
            model_info["name"],
            model_info["model_name"],
            model_info["api_key"],
            model_info["base_url"],
            kwargs=model_info["kwargs"]
        )
    pass