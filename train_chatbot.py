# -*- coding: utf-8 -*-

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

def main():
    train_from_file("ai.yml") # For training file

main()

