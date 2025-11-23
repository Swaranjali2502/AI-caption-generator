
You said:
import streamlit as st
from agent import CaptionAgent 

st.title("📸 AI Caption Generator Agent")

topic = st.text_input("Enter your topic:")
category = st.selectbox("Choose category:", 
                        ["Travel", "Fashion", "Food", "Fitness", "Love", "Nature"])

tone = st.selectbox("Choose tone:", 
                    ["Aesthetic", "Funny", "Emotional", "Bold", "Motivational"])

if st.button("Generate Captions"):
    if topic:
        agent = CaptionAgent()
        output = agent.generate(topic, category, tone)
        st.text_area("Generated Captions:", output, height=300)
    else:
      st.warning("Please enter a topic!")