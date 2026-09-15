from dataclasses import dataclass
@dataclass
class ChatResponse:
    content:str
    input_tokens:int
    output_tokens:int