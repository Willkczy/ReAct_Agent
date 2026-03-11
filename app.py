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
            content = msg.content
            if isinstance(content, list):
                content = "\n".join(item.get("text", "") for item in content if isinstance(item, dict))
            if not content:
                continue
            if msg.type == "human":
                st.markdown(f"**User:** {content}")
            elif msg.type == "ai":
                st.markdown(f"**Thought:** {content[:500]}")
            elif msg.type == "tool":
                st.markdown(f"**Tool ({msg.name}):** {content[:500]}...")

    st.subheader("Final Answer")
    final = result["messages"][-1].content
    # Handle Gemini's list-of-dicts format
    if isinstance(final, list):
        text = "\n".join(item["text"] for item in final if item.get("type") == "text")
    else:
        text = final
    st.markdown(text)