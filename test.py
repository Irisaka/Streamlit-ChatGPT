from revChatGPT.V1 import Chatbot

chatbot = Chatbot(config={
    "email": "107071603@qq.com",
    "password": "why20010803"
})

prompt = "how many beaches does portugal have?"
response = ""

for data in chatbot.ask(
  prompt
):
    response = data["message"]

print(response)