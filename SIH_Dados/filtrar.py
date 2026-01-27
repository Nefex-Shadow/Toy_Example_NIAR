import pandas as pd
import os


i = 0
arquivos = os.listdir("./Dados_csv/")
for arq in arquivos:
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

    # Apenas diagnosticos de doencas respiratorias seram usadas.
    # Diagnosticos que comecam com "J" (coincidentemente, tambem sao os unicos com J)
    df = df.loc[df["DIAG_PRINC"].str.contains("J")]
    df.to_csv("./Dados_Filtrados/" + arq)

    # Contagem usada para acompanhamento do processo, nada mais
    print(i, "/", len(arquivos))
