from GUI.main_gui import run_gui
from Bot.Logic.Dumb import DumbBot
from Bot.Logic.Kill import KillBot
from Bot.Logic.Random import RandomBot
from Bot.Logic.Copy import CopyBot
from Bot.Logic.Stock import StockFish
from Bot.Intialization.ChessBot import ChessBot
from Bot.GameConnector import GameConnector
from Bot.ResultUtil import ResultUtil


def bot_select():
    """Run GUI, initialize a bot type based on input from GUI"""
    ResultUtil.resetResultFile()
    bot = ChessBot("lip_dQJI4YyJYwytH4emLoyq")
    
    selection = run_gui()
    if selection[0] == 'Dumb Bot':
        GameConnector(bot, bot.getGames()[0]["gameId"],DumbBot)
    elif selection[0] == 'Random Bot':
        GameConnector(bot, bot.getGames()[0]["gameId"],RandomBot)
    elif selection[0] == 'Copy Bot':
        GameConnector(bot, bot.getGames()[0]["gameId"],CopyBot)
    elif selection[0] == 'Kill Bot':
        GameConnector(bot, bot.getGames()[0]["gameId"],KillBot)
    elif selection[0] == 'Stock Fish':
        GameConnector(bot, bot.getGames()[0]["gameId"],StockFish)
    return bot

bot_choice = bot_select()


