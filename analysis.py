import pandas as pd
import matplotlib.pyplot as plt

table=pd.read_csv("routes.csv")

table["duration"] = table["duration"].str.replace("s", "")
table["staticDur"] = table["staticDur"].str.replace("s", "")
table["duration"] = table["duration"].astype(int)
table["staticDur"] = table["staticDur"].astype(int)
table["delay"] = table["duration"] - table["staticDur"]

print(table)
