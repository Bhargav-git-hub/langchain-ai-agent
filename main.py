
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain.agents import create_agent
import logging
from tools import search_tool, wiki_tool, save_to_txt

load_dotenv()


#logging.basicConfig(level=logging.DEBUG)
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


llm = ChatAnthropic(
    model="claude-sonnet-5-5"
)
# response = llm.invoke("What is the capital of USA?")
# print(response)

tools = [search_tool, wiki_tool, save_to_txt]
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
    You are a research assistant that helps generate research papers.
    Answer the user query accurately.
    Do not fabricate sources or claim to have used tools.
    """,
    response_format=ResearchResponse
)

query = input("Enter your query: ")
result = agent.invoke({
    "messages": [
        {"role": "user", "content": query}
    ]
})
response = result["structured_response"]
# print(result)
# print("#"*200)
# save_to_txt.invoke({
#     "data": response.model_dump_json(indent=4),
#     "filename": "output.txt"
# })

print(response)
print(response.model_dump_json(indent=4))

#logging.basicConfig(level=logging.INFO)