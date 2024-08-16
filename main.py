import streamlit as st
from langchain.memory import ConversationBufferMemory

from utils import get_chat_response

st.title("Chat-GPT小助手")

with st.sidebar:
    openai_api_key = st.text_input("请输入您的OPENAI API密钥:", type="password")
    st.markdown("[获取OPENAI API密钥](https://api.aigc369.com/)")

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai", "content": "你好,我是您的ai助手,有什么可以帮助您的吗?"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    if not openai_api_key:
        st.info("请输入您的OPENAI API密钥")
        st.stop()
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考中..."):
        response = get_chat_response(prompt, st.session_state["memory"], openai_api_key)

    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)

# 假设这是你的后端逻辑
def clear_chat_memory():
    # 这里应该是调用后端逻辑来清除记忆
    # 例如，调用一个API端点或者直接操作全局变量
    pass

# 创建一个按钮，并在点击时调用clear_chat_memory函数
clear_memory_button = st.button("清除记忆")

if clear_memory_button:
    # 调用后端逻辑来清除记忆
    clear_chat_memory()

    # 清空Streamlit的session状态
    st.session_state.clear()

    # 清除页面上的所有内容
    st.empty()
    # 可以在这里添加一些反馈信息
    st.write("记忆和页面内容已清除！")
    st.rerun()