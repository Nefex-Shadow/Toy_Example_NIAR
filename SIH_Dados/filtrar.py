import pandas as pd
import os


i = 0
for arq in os.listdir("./Dados_csv/"):
    i += 1
    df = pd.read_csv("./Dados_csv/" + arq)
    df = df[
        [
            "CNES",
            "DT_INTER",
            "ANO_CMPT",
            "MES_CMPT",
            "DIAG_PRINC",
            "N_AIH",
            "MORTE",
            "DIAS_PERM",
            "UTI_MES_TO",
            "VAL_TOT",
            "VAL_UTI",
            "SEXO",
            "COD_IDADE",
            "IDADE",
            "RACA_COR",
            "MUNIC_RES",
            "MUNIC_MOV",
            "DIAG_SECUN",
            "PROC_REA",
        ]
    ]
    df = df.loc[df["DIAG_PRINC"].str.contains("J")]
    df.to_csv("./Dados_Filtrados/" + arq)
    print(i)
