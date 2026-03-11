import streamlit as st
from agent import get_agent

st.title("ReAct Agent")
st.write("Ask a complex question that requires searching, comparing, or analyzing.")

agent = get_agent()
query = st.text_input("Enter your query:")

if st.button("Submit") and query:
    with st.spinner("Agent is thinking..."):
        result = agent.invoke({"input": query})

    with st.expander("Step-by-step reasoning", expanded=False):
        for step in result.get("intermediate_steps", []):
            action, observation = step
            st.markdown(f"**Thought:** {action.log}")
            st.markdown(f"**Action:** {action.tool}[{action.tool_input}]")
            st.markdown(f"**Observation:** {str(observation)[:500]}")
            st.markdown("---")

    st.subheader("Final Answer")
    st.markdown(result["output"])
