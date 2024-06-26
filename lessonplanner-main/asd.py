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
    page = st.sidebar.radio("Go to", ["Generate Plan", "View Plan"])

    if page == "Generate Plan":
        generate_plan()
    elif page == "View Plan":
        generated_plan()

# Function for generating plan
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
        # Store response in session state
        st.session_state.generated_response = response
        st.experimental_rerun()

# Function for displaying generated plan
def generated_plan():
    if "generated_response" in st.session_state:
        response = st.session_state.generated_response
        st.write("**Lesson Plan generated by Mistral model**")
        topics = response.split('\n')
        colms = st.columns((2, 2, 1))
        fields = ["**TOPICS**", '**LINK**', "**ACTION**"]
        for col, field_name in zip(colms, fields):
            # header
            col.write(field_name)

        for i, topic in enumerate(topics, 1):
            topic = topic.strip().replace("*", "")
            topic = re.sub(r'Subtopic \d+:', '', topic)
            topic = topic.strip()
            col1, col2, col3 = st.columns((2, 2, 1))
            disable_status = "summarize"
            if topic.strip() and not topic.strip().startswith("Topic"):
                col1.write(topic.strip())
                col2.write("https://example.com")
                button_type = "summarize" if disable_status else "Block"
                button_phold = col3.empty()  # create a placeholder
                do_action = button_phold.button(button_type, key=i)
                if do_action:
                    custom_action() #  remove button
            else:
                col1.write(f"**{topic.strip()}**")  # index

        # Option to clear stored response
        if st.button("Clear Response"):
            del st.session_state.generated_response

def custom_action():
    st.success("done")

if __name__ == "__main__":
    main()
