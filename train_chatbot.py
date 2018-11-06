# -*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

def train_from_file(fname):
    bot = ChatBot(
    "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="db.sqlite3"
    
    )
    chatterbot.set_trainer(ListTrainer)
    trainer = ListTrainer(bot)
    trainer.train(fname)

def train_from_terminal():
    bot = ChatBot(
    "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="db.sqlite3"
    #   "default_response": "I am sorry, but I do not understand."

    

    
    )
    print("Type something to begin...")
    while True:
        try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
            bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            break




def main():
    #train_from_file("ai.yml") # For training file
    train_from_terminal()
main()

