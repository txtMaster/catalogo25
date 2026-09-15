from .gemini_adapter import GeminiProvider

class ProviderFactory:
    @staticmethod
    def create_gemini_provider(client,model) -> GeminiProvider:
        return GeminiProvider(client,model)