import os
from dotenv import load_dotenv
from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI,RunResult,set_tracing_disabled
import rich

load_dotenv()
set_tracing_disabled(disabled=True)
gemini_api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)        

shopping_agent = Agent(
    name="shopping_agent",
    instructions="you assist user to finding products and making purchase decisions.",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash-lite", openai_client=client),
    handoff_description="a shopping agent to help user in shopping",
)

support_agent = Agent(
    name="support_agent",
    instructions="you help user post-purchase support and returns.",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash-lite", openai_client=client),
    handoff_description="a support agent to help user post-purchase queries.",
)
triage_agent = Agent(
    name="triage_agent",
    instructions=(
        "you are a triage agent, you delegate task to appropriate agent or use appropriate given tools"
        "\nwhen user asked for shopping related query, you always use given tools"
        "\nyou never reply on your own, always use given tool to reply user"
    ),
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash-lite", openai_client=client),
    tools=[
        shopping_agent.as_tool(
            tool_name="transfer_to_shopping_agent",
            tool_description="you assist user to finding products and making purchase decisions.always add this ✅ emojis in your reply, start replay with this ✅ emojis",
        ),
        support_agent.as_tool(
            tool_name="transfer_to_support_agent",
            tool_description="you help user with post-purchase support and returns.always add this ❌ emojis in your reply, start replay with this ❌ emojis",
        )
    ]
)

result:RunResult = Runner.run_sync(starting_agent=triage_agent, input="help me to find a good visit watch.",max_turns=2)

rich.print(result.final_output)