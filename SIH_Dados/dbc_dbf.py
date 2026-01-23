import pyreaddbc
import os

arquivos = os.listdir("./Dados/")

for a in arquivos:
    dfs = pyreaddbc.dbc2dbf(
        "./Dados/" + a, "./Dados_dbf/" + a.removesuffix(".dbc") + ".dbf"
    )
