from re import sub
import pandas as pd
import matplotlib.pyplot as plt
from time import time

if __name__ == "__main__":

    print("Loading Excel data...")
    loadTime = time()
    pvsheet = pd.read_excel(
        "./Resources/Mapping Police Violence.xlsx", usecols="A:O")
    loadTime = time() - loadTime
    print("Loading Finished. Loading time: {:.3f} seconds".format(loadTime))

    print("Brutality by State")
    pvsheet["State"].value_counts()[:10].plot(kind='bar', rot=0)
    plt.title("Brutality by State")
    plt.xlabel("State")
    plt.ylabel("Number of Incidents")
    plt.grid()
    plt.show()
 
    print("CA Incidents by Zipcode")
    agg = pvsheet.filter(items=["State", "Zipcode"])\
        .groupby("State").value_counts()["CA"]
    agg.head(n=10).plot(kind="bar", rot=0)
    plt.title("CA Incidents by Zipcode")
    plt.xlabel("Zipcode")
    plt.ylabel("Number of Incidents")
    plt.grid()
    plt.show()
