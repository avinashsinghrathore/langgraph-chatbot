import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

# st.session_state -> dict -> a special type of dict for streamlit which store data for the particular session
# once we manualy refresh the page then data will be erased otherwise it will be present in temp memory
CONFIG = {"configurable": {"thread_id": "thread-1"}}

if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

message_history = []

# load the conversation history
for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.text(message["content"])

# {"role": "user", "content": "Hi.."}
# {"role": "assistant", "content": "Your res.."}

user_input = st.chat_input("Type here")

if user_input:

    # first add the message to the message history
    st.session_state["message_history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)

    # first add the message to the message history

    with st.chat_message("assistant"):
        ai_message = st.write_stream(
            message_chunk.content
            for message_chunk, metadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config={"configurable": {"thread_id": "thread-1"}},
                stream_mode="messages",
            )
        )
    st.session_state["message_history"].append({"role": "assistant", "content": ai_message})
 