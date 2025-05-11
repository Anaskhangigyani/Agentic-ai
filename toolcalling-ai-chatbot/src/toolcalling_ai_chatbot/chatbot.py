import chainlit as cl
import os
from dotenv import load_dotenv, find_dotenv
from agents import Agent, RunConfig, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool

load_dotenv(find_dotenv())

gemini_api_key = os.getenv("GEMINI_API_KEY")


@function_tool('get_weather')
async def get_weather(location: str, unit: str) -> str:
    """
    Fetch the weather for a given location, returning a short description.
    """
    return f"The weather in {location} is 22 degrees {unit}."


@function_tool("piaic_student_finder")
def student_finder(student_roll: int) -> str:
  """
  Find the PIAIC student based on the roll number
  """
  data = {1: "Uzairkhan",
          2: "Talhakhan",
          3: "Anaskhan"}

  return data.get(student_roll, "Not Found")

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

agent: Agent = Agent(
    name="Assistant",
    tools=[get_weather, student_finder],
    instructions="You are a helpful assistant"
)

@cl.on_chat_start
async def chat_start():
    await cl.Message(content='Hello! How can I assist you, Anaskhan?').send()
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
