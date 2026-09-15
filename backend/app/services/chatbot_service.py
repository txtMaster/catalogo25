from app.ai.chatbot_provider import ChatbotProvider

class ChatService:
    def __init__(self,provider: ChatbotProvider) -> None:
        self.provider = provider
    
    def send_message(self,message:str)->str:
        return ""