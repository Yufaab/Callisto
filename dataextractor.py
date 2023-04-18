import pandas as pd
import numpy as np
import json
df=pd.read_csv("data/2022/round6.csv")
specific_column=df["Academic Program Name"].unique().tolist()
print("The column is:")
print(len(specific_column))
jsonobj = {'branches2022' : specific_column}
with open("branch.json", "w") as outfile:
    json.dump(jsonobj, outfile)