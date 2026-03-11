import streamlit as st
from agent import get_agent

st.title("ReAct Agent")
st.write("Ask a complex question that requires searching, comparing, or analyzing.")

agent = get_agent()
query = st.text_input("Enter your query:")

if st.button("Submit") and query:
    with st.spinner("Agent is thinking..."):
        result = agent.invoke({"messages": [{"role": "user", "content": query}]})

    with st.expander("Step-by-step reasoning", expanded=False):
        for msg in result["messages"]:
            if msg.type == "human":
                st.markdown(f"**User:** {msg.content}")
            elif msg.type == "ai" and msg.content:
                st.markdown(f"**Thought:** {msg.content}")
            elif msg.type == "tool":
                st.markdown(f"**Tool ({msg.name}):** {msg.content[:500]}...")

    st.subheader("Final Answer")
    st.markdown(result["messages"][-1].content)