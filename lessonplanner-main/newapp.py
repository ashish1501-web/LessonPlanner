import streamlit as st
from ollama import chat
import re
# Function to get LLama response


def getPlan(input_text, no_hours, level):
    messages = [
        {
            'role': 'user',
            'content': f"Generate a lesson plan for {no_hours} hours on {input_text} with a difficulty level of {level}. "
        },
    ]
    response = chat('lessonPlanner', messages=messages)
    return response['message']['content']

# Streamlit UI


def main():
    st.set_page_config(page_title="Generate plan",
                       page_icon='🖥️',
                       layout='wide',
                       initial_sidebar_state='expanded')

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Generate Plan", "View Plan","Summarize content"])

    if page == "Generate Plan":
        generate_plan()
    elif page == "View Plan":
        generated_plan()
    elif page=="Summarize content":
        summarize_content()

# Function for generating plan
def save_response_to_file(response):
    with open("generated_plan.txt", "w") as file:
        file.write(response)

def generate_plan():
    st.title("Generate plan 🖥️")

    input_text = st.text_input("Enter the Topic")

    col1, col2 = st.columns([8, 8])

    with col1:
        no_hours = st.text_input('No of hours')
    with col2:
        level = st.selectbox('Difficulty level',
                             ('beginner', 'intermediate', 'advanced'), index=0)

    submit = st.button("Generate")

    if submit:
        response = getPlan(input_text, no_hours, level)
        st.sidebar.write("## View Plan")
        st.session_state.generated_response = response
        save_response_to_file(response)
        # st.experimental_rerun()

import sys
sys.path.append(r'C:/Users/aharakun/Downloads/lessonplanner-main/WebScraper/WebScraper/spiders')
import get_topic

def summarize_content():
    st.title("Summarize content 🖥️")
    submit = st.button("Give topic")

    if submit:
        # response = getPlan(input_text, no_hours, level)
        # st.sidebar.write("## View Plan")
        st.success("yess bro")
        import os
        
        os.system("C:/Users/aharakun/Downloads/lessonplanner-main/a.bat")
        with open("summarized_content.txt","r") as file:
            lines=file.readlines()
            for line in lines:
                st.success(str(line))
        # st.session_state.generated_response = response
        # save_response_to_file(response)




# def generated_plan():
#     if "generated_response" in st.session_state:
#         response = st.session_state.generated_response
#         st.write("Below is the response from Mistral model:")
#         topics = response.split('\n')
#         data = []
#         for i, topic in enumerate(topics, 1):
#             topic = topic.strip().replace("*", "")
#             topic = re.sub(r'Subtopic \[\d+\]', '', topic)
#             topic = topic.strip()
#             if topic.strip():
#                 # Dummy link for now
#                 data.append({
#                     "Topic": topic.strip(),
#                     "Website Link": "https://example.com",
#                     "Button": st.button(f"Button {i}")
#                 })
#         st.table(data)


def custom_action():
    st.success("done")

import sys
sys.path.append(r'C:/Users/aharakun/Downloads/lessonplanner-main/WebScraper/WebScraper')
import fetch_url
from fetch_url import fetch_links
import asyncio
import time

def generated_plan():
    if "generated_response" in st.session_state:
        response = st.session_state.generated_response
        st.write("**Lesson Plan generated by Mistral model**")
        topics = response.split('\n')
        colms = st.columns((2, 2, 1))
        fields = ["**TOPICS**", '**LINK**']
        for col, field_name in zip(colms, fields):
            # header
            col.write(field_name)

        for i, topic in enumerate(topics, 1):
            topic = topic.strip().replace("*", "")
            topic = re.sub(r'Subtopic \d+:', '', topic)
            topic = topic.strip()
            col1, col2 = st.columns((2, 2))
            link=asyncio.run(fetch_links(topic.strip()))
            time.sleep(5)
            if topic.strip().startswith("Rules"):
                pass

            if topic.strip() and not topic.strip().startswith("Topic"):
                col1.write(topic.strip())
                col2.write(link[0])
            else:
                col1.write(f"**{topic.strip()}**")  # index

if __name__ == "__main__":
    main()
