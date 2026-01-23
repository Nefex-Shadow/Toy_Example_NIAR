import os
import pandas as pd
from dbfread import DBF

for file in os.listdir("./Dados_dbf/"):
    if file.endswith(".dbf") and ("*" not in file):
        dbf = DBF(f"Dados_dbf/{file}", load=True, encoding="ISO-8859-1")
        dbf_df = pd.DataFrame(dbf.records)
        dbf_df.to_csv(f"./Dados_csv/{os.path.splitext(file)[0]}.csv")
        print(f"data/{file} converted to csv")
