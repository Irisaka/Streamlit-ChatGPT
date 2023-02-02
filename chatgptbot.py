import streamlit as st
from streamlit_chat import message
from revChatGPT.Official import Chatbot

def main():
    def get_input(prompt):
        """
        Multi-line input function
        """
        # Display the prompt
        print(prompt, end="")

        # Initialize an empty list to store the input lines
        lines = []

        # Read lines of input until the user enters an empty line
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)

        # Join the lines, separated by newlines, and store the result
        user_input = "\n".join(lines)

        # Return the input
        return user_input

    def chatbot_commands(cmd: str) -> bool:
        """
        Handle chatbot commands
        """
        if cmd == "!help":
            print(
                """
            !help - Display this message
            !rollback - Rollback chat history
            !reset - Reset chat history
            !exit - Quit chat
            """
            )
        elif cmd == "!exit":
            exit()
        elif cmd == "!rollback":
            chatbot.rollback(1)
        elif cmd == "!reset":
            chatbot.reset()
        else:
            return False
        return True

    # import argparse

    # # Get API key from command line
    # parser = argparse.ArgumentParser()
    # parser.add_argument(
    #     "--api_key",
    #     type=str,
    #     required=True,
    #     help="OpenAI API key",
    # )
    # args = parser.parse_args()
    # # Initialize chatbot
    # chatbot = Chatbot(api_key=args.api_key)

    st.set_page_config(
        page_title="",
        page_icon="🧊",
        layout="centered",
        initial_sidebar_state="expanded",
    )
    st.title("MyChatGPT")

    if 'message_history' not in st.session_state:
        st.session_state['message_history'] = []

    for index, message_ in enumerate(st.session_state['message_history']):
        message(message_[0], is_user=message_[1], key=index)   # display all the previous message

    placeholder = st.empty()  # placeholder for latest message
    placeholder2 = st.empty()

    with st.form("my_form"):
        input_ = st.text_input("you:")
        submitted = st.form_submit_button("Submit")
        if submitted:
            user_input = input_

            st.session_state['message_history'].append([user_input, 1])

            with placeholder.container():
                message(st.session_state['message_history'][-1][0], is_user=st.session_state['message_history'][-1][1]) # display the latest message

            # chatbot = Chatbot(api_key=st.secrets["API_KEY"])
            # # Start chat
            # while True:
            #     # PROMPT = get_input("\nUser:\n")
            #     PROMPT = 
            #     if PROMPT.startswith("!"):
            #         if chatbot_commands(PROMPT):
            #             continue
            #     response = chatbot.ask(PROMPT)
            #     print("ChatGPT: " + response["choices"][0]["text"])

            chatbot = Chatbot(api_key=st.secrets["API_KEY"])
            PROMPT =  "\nUser:\n" + user_input
            # if PROMPT.startswith("!"):
            #     if chatbot_commands(PROMPT):
            #         continue
            response = chatbot.ask(PROMPT)
            print("ChatGPT: " + response["choices"][0]["text"])
            st.session_state['message_history'].append([response["choices"][0]["text"], 0])
            with placeholder2.container():
                message(st.session_state['message_history'][-1][0], is_user=st.session_state['message_history'][-1][1]) # display the latest message


if __name__ == "__main__":
    main()