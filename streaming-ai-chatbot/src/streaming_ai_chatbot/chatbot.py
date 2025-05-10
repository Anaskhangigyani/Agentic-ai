import chainlit as cl
import os
from dotenv import load_dotenv, find_dotenv
from agents import Agent, RunConfig, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

load_dotenv(find_dotenv())

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)

agent: Agent = Agent(name="Assistant", instructions="You are a helpful assistant")

@cl.on_chat_start
async def chat_start():
    await cl.Message(content='Hello How I Can Assist You? Anaskhan').send()
    cl.user_session.set('history', [])

@cl.on_message
async def on_message(msg: cl.Message):
    history = cl.user_session.get('history')
    history.append({"role": "user", "content": msg.content})
    response_msg = cl.Message(content="")
    await response_msg.send()

    result = Runner.run_streamed(
        agent,
        input=history,
        run_config=config
    )

    async for event in result.stream_events():
        if event.type == "raw_response_event" and hasattr(event.data, 'delta'):
            token = event.data.delta
            await response_msg.stream_token(token)

    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", history)
