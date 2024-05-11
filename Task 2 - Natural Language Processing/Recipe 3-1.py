import pandas as pd


Text = "I am learning NLP"

res = pd.get_dummies(Text.split())

print(res)

