from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot


chatbot = ChatBot("ลูกชิ้น")
conversation = [
    "สวัสดีค่ะ",
    "ดีค่ะนักเรียน",
    "เป็นยังไงบ้างคะ",
    "ครูสบายดี",
    "ทำไมไม่มีใครตอบครูเลย",
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)
textttt = str(input("Enter : "))

response = chatbot.get_response(textttt)
print(str(response))