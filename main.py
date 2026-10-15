import os
import asyncio

from dotenv import load_dotenv
from pydantic import SecretStr
from chain import LLMFactory
from schemas import LLMConfig, Provider

load_dotenv()


async def main():
    config = LLMConfig(
        openai_api_key=SecretStr(os.environ["OPENAI_API_KEY"]),
        anthropic_api_key=SecretStr(os.environ["ANTHROPIC_API_KEY"]),
    )
    client = LLMFactory.create_client(Provider.OPENAI, config)
    print(await client.stream("¿Qué es la entropía?"))

if __name__ == "__main__":
    asyncio.run(main())


