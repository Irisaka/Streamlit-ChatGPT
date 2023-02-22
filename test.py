from revChatGPT.V1 import Chatbot

chatbot = Chatbot(config={
    "email": "",
    "password": ""
})

prompt = "how many beaches does portugal have?"
response = ""

for data in chatbot.ask(
  prompt
):
    response = data["message"]

print(response)
