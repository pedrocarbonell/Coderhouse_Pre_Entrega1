from enum import Enum

from pydantic import BaseModel, SecretStr

class Provider(str, Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"

class LLMConfig(BaseModel):
    openai_api_key: SecretStr | None = None
    anthropic_api_key: SecretStr | None = None

    def key_for(self, provider: Provider) -> str:
        key = getattr(self, f"{provider.value}_api_key")
        if not key or not key.get_secret_value():
            raise ValueError(f"Falta la API Key de {provider.value}")
        return key.get_secret_value()


