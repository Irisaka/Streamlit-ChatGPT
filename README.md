# Streamlit-ChatGPT
Use Streamlit to quickly build a ChatGPT-based Web page. ChatGPT API is based on https://github.com/acheong08/ChatGPT.
<img width="732" alt="屏幕截图_20230203_170711" src="https://user-images.githubusercontent.com/58900145/220100808-27ec56ee-eac4-4c5b-ac5c-6699c9344151.png">
## Install
1. git clone https://github.com/Irisaka/Streamlit-ChatGPT.git
2. `pip install -r requirements.txt`
3. Insert your openai account information.
```python
# in chatgptbot.py
st.session_state.chatbot = Chatbot(config={
    "email": st.secrets["openai_email"],        # "email": your openai email
    "password": st.secrets["openai_password"]   # "password": your openai password
})
```
## Run Locally
`streamlit run chatgptbot.py`
## Run Online Preview
An example: https://irisaka-streamlit-chatgpt-chatgptbot-spnftb.streamlit.app/
More information see https://streamlit.io/
