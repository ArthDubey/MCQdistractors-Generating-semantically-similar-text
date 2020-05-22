import pandas as pd

df=pd.read_csv("answer.csv")

def sol(s):
    s=str(s)
    # for i in range(len(s)-1):
    #     if s[i]=='"' and s[i+1]=='"':
    s.replace('''""''','''"''')
    return s

df["distractor"]=df["distractor"].apply(sol)
df.to_csv("answer.csv")