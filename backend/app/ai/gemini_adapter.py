from .chatbot_provider import ChatbotProvider

class GeminiProvider(ChatbotProvider):
    def __init__(self,client:dict,model:dict) -> None:
        self.client = client
        self.model = model
        
    def chat(self, messages: list[dict]) -> str:
        return ""
    
    def generate_content(self, message: list[dict]) -> str:
        return ""