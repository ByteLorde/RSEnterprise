from RSEnterprise.src.plugins.bot.LeatherTanningBot.BotScript import BotScript
from RSEnterprise.src.plugins.bot.LeatherTanningBot.Stages.StageReader import StageReader


class TanningBot(BotScript):

    def __init__(self):
        self.stageReader = StageReader()
