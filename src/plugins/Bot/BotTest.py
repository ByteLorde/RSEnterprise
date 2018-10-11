from src.plugins.Bot.Bot import Bot

bot1 = Bot()
bot2 = Bot()
bot3 = Bot()
bot4 = Bot()
bot5 = Bot()
botList = [bot1, bot2, bot3, bot4, bot5]

for i in range(0, 5):
    print("Bot #" + str(i + 1))
    currentBot = botList[i]
    currentBot.generateProfile()
    print("Name: " + currentBot.getName())
    print("Username: " + currentBot.getUsername())
    print("Password: " + currentBot.getPassword())
    print("Email: " + currentBot.getEmail())
    print("Birthday: " + str(currentBot.getBirthday()))
    print("Gender: " + currentBot.getGender())
    print()
