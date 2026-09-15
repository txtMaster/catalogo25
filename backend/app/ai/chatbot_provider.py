from abc import ABC, abstractmethod

class ChatbotProvider(ABC):
    @abstractmethod 
    def chat(self,messages:list[dict]) -> str:
        pass
    
    @abstractmethod
    def generate_content(self,message:list[dict])->str:
        pass
    
    