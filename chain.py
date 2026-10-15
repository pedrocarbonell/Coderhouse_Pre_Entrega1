# External dependencies
from abc import ABC, abstractmethod
from openai import AsyncOpenAI

# Internal dependecies
from schemas import LLMConfig, Provider


class BaseLLMClient(ABC):
    @abstractmethod
    async def stream(self, prompt: str) -> str:
        pass

class OPENAICLIENT(BaseLLMClient):
    def __init__(self, config: LLMConfig):
        self.client = AsyncOpenAI(api_key=config.key_for(Provider.OPENAI))

    async def stream(self, prompt: str) -> str:
        stream = await self.client.responses.create(
            model = "gpt-6-luna",
            input = prompt,
            stream = True,
        )

        chunks = []
        async for event in stream:
            if event.type == "response.output_text.delta":
                print(event.delta, end="", flush=True)
                chunks.append(event.delta)
        return "".join(chunks)

class ANTHROPICCLIENT(BaseLLMClient):
    def __init__(self, config: LLMConfig):
        self.client = AsyncAnthropic(api_key=config.key_for(Provider.ANTHROPIC))

    async def stream(self, prompt: str) -> str:
        stream = await self.client.responses.create(
            model = "haiku-5-5",
            messages = [
                {
                    "role": "user",
                    "content": prompt,
                }

            ]
        )

class LLMFactory:
    _clients = {
        Provider.OPENAI: OPENAICLIENT,
        Provider.ANTHROPIC: ANTHROPICCLIENT
    }

    @staticmethod
    def create_client(provider: Provider, config: LLMConfig) -> BaseLLMClient:
        return LLMFactory._clients[Provider(provider)](config)



