from chatterbot import ChatBot
import os
from gtts import gTTS

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# Get a response to an input statement

text = input("YOU: ")


# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed


# Saving the converted audio in a mp3 file named
# welcome


# Playing the converted file
while text != "!":
    response = str(chatbot.get_response(text))
    myobj = gTTS(text=response, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system('mpg123 /home/syndicate/PycharmProjects/Iris/test/Tests1/welcome.mp3')

    print("BOT:", response)
    text = input("YOU: ")
