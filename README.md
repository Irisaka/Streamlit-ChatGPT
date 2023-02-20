# Streamlit-ChatGPT
Use Streamlit to quickly build a ChatGPT-based Web page. ChatGPT API is based on https://github.com/acheong08/ChatGPT.
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
## Run locally
`streamlit run chatgptbot.py`
