from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer 

# Creat An Object With Name Chat_bot
chat_bot = ChatBot('Chat_Bot')

# Train The Chat_bot Object
trainer = ChatterBotCorpusTrainer(chat_bot)

# Trian The Chat_bot On a Specific Data
trainer.train("chatterbot.corpus.english")

print("Hi , I am a ChatBot")
while True:
    query = input(">>> ")
    print(chat_bot.get_response(query))
