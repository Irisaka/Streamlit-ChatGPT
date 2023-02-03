import streamlit as st
from streamlit_chat import message
from streamlit_elements import elements, mui, lazy, sync, event
from revChatGPT.Official import Chatbot

def main():

    st.set_page_config(
        page_title="",
        page_icon="🧊",
        layout="centered",
        initial_sidebar_state="expanded",
    )
    st.title("MyChatGPT")

    if 'message_history' not in st.session_state:
        st.session_state['message_history'] = []

    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = Chatbot(api_key=st.secrets["API_KEY"])

    # if 'user_input' not in st.session_state:
    #     st.session_state.user_input = None

    # if st.session_state.user_input is not None:
    #     text = st.session_state.user_input.target.value
    # else:
    #     text = "你好"

    for index, message_ in enumerate(st.session_state['message_history']):
        message(message_[0], is_user=message_[1], key=index)   # display all the previous message

    placeholder = st.empty()  # placeholder for latest message
    placeholder2 = st.empty()

    # with elements("user_input_submit"):
    #     mui.TextField(label="you:", onChange=lazy(sync("user_input")))
    #     mui.Button("Enter", onClick=sync())

    with st.form("user_input_form", clear_on_submit=True):
        text = st.text_input('you:')
        submitted = st.form_submit_button("Enter")
        if submitted:
            st.session_state['message_history'].append([text, 1])

            with placeholder.container():
                message(st.session_state['message_history'][-1][0], is_user=st.session_state['message_history'][-1][1]) # display the latest message

            chatbot = st.session_state.chatbot
            PROMPT =  "\nUser:\n" + text
            response = chatbot.ask(PROMPT)
            st.session_state.chatbot = chatbot

            print("ChatGPT: " + response["choices"][0]["text"])
            st.session_state['message_history'].append([response["choices"][0]["text"], 0])
            with placeholder2.container():
                message(st.session_state['message_history'][-1][0], is_user=st.session_state['message_history'][-1][1]) # display the latest message


if __name__ == "__main__":
    main()