from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain

from langchain.memory import ConversationBufferMemory
import os

def get_chat_response(promt, memory, openai_api_key):
    model = ChatOpenAI(model="gpt-4o", openai_api_key=openai_api_key, openai_api_base="https://api.aigc369.com/v1")
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": promt})
    return response["response"]

# memory = ConversationBufferMemory(return_message=True)
# print(get_chat_response("从零开始的异世界生活第三季什么时候播出？", memory, os.getenv("OPENAI_API_KEY")))
# print(get_chat_response("第一集时长有多少？", memory, os.getenv("OPENAI_API_KEY")))

class ChatMemory:
    def __init__(self):
        self.memory = {}

    def reset_memory(self):
        self.memory.clear()

# 假设这是你的后端逻辑
def clear_chat_memory():
    memory_instance = ChatMemory()  # 这里应该是获取到实际的内存实例
    memory_instance.reset_memory()