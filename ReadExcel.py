import numpy as np
import pandas as pd


class MTGCard:
    def __init__(self, title, cost, rules, flavor, year):
        self.title = title
        self.cost = cost
        self.rules = rules
        self.flavor = flavor
        self.year = year
        self.isCast = False

    def __str__(self):
        return str(self.title) + "\t" + str(self.cost) + "\n" \
            + str(self.rules) + "\n" \
            + "---\n" \
            + str(self.flavor) + "\n" \
            + str(self.year)
    
    def cast(self):
        self.isCast = True


if __name__ == "__main__":
    sheet = pd.read_excel("./Resources/Checklist.xlsx", dtype=object)
    cards = []
    for nrow in sheet.index:
        rowData = sheet.iloc[nrow]
        notes = rowData["Notes"]
        if str(notes) == "nan":
            notes = None
        date = rowData["Date Applied"].year
        cards.append(MTGCard(rowData["Company Name"], rowData["Location"],
                     rowData["Position"], notes, date))
    print(cards[0])
