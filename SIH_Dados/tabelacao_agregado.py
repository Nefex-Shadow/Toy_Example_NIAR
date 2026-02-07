import numpy as np
import pandas as pd
import os


def get_region(arq):
    return arq[2:4]


def calculo_idade(linha):
    if linha["COD_IDADE"] == 4:
        return linha["IDADE"]
    if linha["COD_IDADE"] == 2:
        return 0
    if linha["COD_IDADE"] == 3:
        return 0
    return np.nan


# Entropia de Shannon
def calculo_entropia(counts):
    counts = np.array(counts, dtype=float)
    total = counts.sum()
    if total == 0:
        return 0.0
    p = counts / total
    p = p[p > 0]  # remove zeros
    return -np.sum(p * np.log(p))


# Leitura dos dados
arquivos = os.listdir("./Dados_Filtrados/")
dfs = []
for a in arquivos:
    df = pd.read_csv("./Dados_Filtrados/" + a, index_col=0).reset_index(drop=True)
    df["region"] = get_region(a)
    dfs.append(df)
main_df = pd.concat(dfs)  # Juncao de todos os arquivos em um Dataframe

# Novo atributo: idade calculada (vide funcao "calculo idade" para formula)
main_df["age_years"] = main_df.apply(calculo_idade, axis=1)


# Filtragem dos dados pelo Ano/Mes
def get_df_mes_ano(mes, ano):
    janela_chao = ano * 10000 + mes * 100
    janela_teto = janela_chao + 31
    return main_df.loc[
        (main_df.DT_INTER >= janela_chao) & (main_df.DT_INTER <= janela_teto)
    ]


# Listas de lista dos valores de interesse.
# Cada lista contempla um hospital em dado mes e ano.
# Valores, em ordem:
# [year, month, CNES (Hospital), region (estado), quarter, time_index, sin_month, cos_month,
# J_count, J_morte_share, J_dias_perm_mean, J_dias_perm_p90, J_uti_share, J_uti_days_mean,
# J_val_tot_mean, J_val_tot_p90, J_val_uti_share, J_sex_f_share, J_sex_m_share, J_age_60p_share,
# J_missing_raca_share, J00_06_share, J09_18_share, J20_22_share, J40_47_share, J_bucket_entropy,
# catchment_munic_unique, catchment_top1_share, catchment_entropy, catchment_outside_local_share,
# J_missing_diag_sec_share, J_missing_proc_share]
dados_por_mes_e_hospital = []


mes = 1
ano = 2022

# Loop de 2022/01 ate 2025/11, nao ha informacao de 2025/12 a diante
while ano < 2025 or mes < 12:
    # Impressao para acompanhamento do progresso do script
    print(ano, "/", mes)

    df = get_df_mes_ano(mes, ano)

    # Calculos por hospital
    cnes = df["CNES"].unique()
    for hos in cnes:
        h_df = df[df.CNES == hos]
        sizeh = h_df.shape[0]

        # Calculos adicionais
        uti_mean = 0
        if not h_df["UTI_MES_TO"].isnull().values.any():
            uti_mean = h_df["UTI_MES_TO"].mean()

        bucket_1 = (
            h_df["DIAG_PRINC"][
                h_df.DIAG_PRINC.str.contains(r"J0[0-6]", na=False)
            ].shape[0]
            / sizeh
        )
        bucket_2 = (
            h_df["DIAG_PRINC"][
                h_df.DIAG_PRINC.str.contains(r"J09|J1[0-8]", na=False)
            ].shape[0]
            / sizeh
        )
        bucket_3 = (
            h_df["DIAG_PRINC"][
                h_df.DIAG_PRINC.str.contains(r"J2[0-2]", na=False)
            ].shape[0]
            / sizeh
        )
        bucket_4 = (
            h_df["DIAG_PRINC"][
                h_df.DIAG_PRINC.str.contains(r"J4[0-7]", na=False)
            ].shape[0]
            / sizeh
        )

        munic_uni = h_df["MUNIC_RES"].unique()

        dados_por_mes_e_hospital.append(
            [
                ano,  # year
                mes,  # month
                hos,  # CNES
                h_df["region"].values[0],  # region
                int((mes - 1) / 3 + 1),  # quarter
                ano * 12 + mes,  # time_index
                np.sin(2 * np.pi * mes / 12),  # sin_month
                np.cos(2 * np.pi * mes / 12),  # cos_month
                h_df.shape[0],  # J_count
                h_df["MORTE"][h_df.MORTE == 1].shape[0] / sizeh,  # J_morte_share
                h_df["DIAS_PERM"].mean(),  # J_dias_perm_mean
                np.percentile(h_df["DIAS_PERM"], 90),  # J_dias_perm_p90
                h_df["UTI_MES_TO"][h_df.UTI_MES_TO > 0].shape[0] / sizeh,  # J_uti_share
                uti_mean,  # J_uti_days_mean
                h_df["VAL_TOT"].mean(),  # J_val_tot_mean
                np.percentile(h_df["VAL_TOT"], 90),  # J_val_tot_p90
                h_df["VAL_UTI"][h_df.VAL_UTI > 0].shape[0] / sizeh,  # J_val_uti_share
                h_df["SEXO"][(h_df.SEXO == "F") | (h_df.SEXO == 3)].shape[0]
                / sizeh,  # J_sex_f_share
                h_df["SEXO"][(h_df.SEXO == "M") | (h_df.SEXO == 1)].shape[0]
                / sizeh,  # J_sex_m_share
                h_df["age_years"][h_df.age_years >= 60].shape[0]
                / sizeh,  # J_age_60p_share
                h_df["age_years"][(h_df.age_years < 60) & (h_df.age_years >= 15)].shape[
                    0
                ]
                / sizeh,  # J_age_15_59_share
                h_df["age_years"][h_df.age_years < 15].shape[0]
                / sizeh,  # J_age_0_14_share
                h_df["RACA_COR"][
                    (h_df.RACA_COR.isnull())
                    | (h_df.RACA_COR == 0)
                    | (h_df.RACA_COR >= 6)
                ].shape[0]
                / sizeh,  # J_missing_raca_share
                h_df["RACA_COR"][h_df.RACA_COR == 1].shape[0]
                / sizeh,  # J_raca_branca_share
                h_df["RACA_COR"][h_df.RACA_COR == 2].shape[0]
                / sizeh,  # J_raca_negra_share
                h_df["RACA_COR"][(h_df.RACA_COR >= 3) & (h_df.RACA_COR <= 5)].shape[0]
                / sizeh,  # J_raca_outras_share
                bucket_1,  # J00_06_share
                bucket_2,  # J09_18_share
                bucket_3,  # J20_22_share
                bucket_4,  # J40_47_share
                calculo_entropia(
                    [bucket_1, bucket_2, bucket_3, bucket_4]
                ),  # J_bucket_entropy
                len(munic_uni),  # catchment_munic_unique
                max(
                    [
                        h_df["MUNIC_RES"][h_df.MUNIC_RES == m].shape[0] / sizeh
                        for m in munic_uni
                    ]
                ),  # catchment_top1_share
                calculo_entropia(
                    [h_df["MUNIC_RES"][h_df.MUNIC_RES == m].shape[0] for m in munic_uni]
                ),  # catchment_entropy
                h_df[["MUNIC_RES", "MUNIC_MOV"]][
                    h_df.MUNIC_RES != h_df.MUNIC_MOV
                ].shape[0]
                / sizeh,  # catchment_outside_local_share
                h_df["DIAG_SECUN"][
                    (h_df.DIAG_SECUN.isnull()) | (h_df.DIAG_SECUN == "")
                ].shape[0]
                / sizeh,  # J_missing_diag_sec_share
                h_df["PROC_REA"][
                    (h_df.PROC_REA.isnull()) | (h_df.PROC_REA == "")
                ].shape[0]
                / sizeh,  # J_missing_proc_share
            ]
        )

    mes += 1
    if mes > 12:
        mes -= 12
        ano += 1

df_final = pd.DataFrame(
    dados_por_mes_e_hospital,
    columns=[
        "year",
        "month",
        "CNES",
        "region",
        "quarter",
        "time_index",
        "sin_month",
        "cos_month",
        "J_count",
        "J_morte_share",
        "J_dias_perm_mean",
        "J_dias_perm_p90",
        "J_uti_share",
        "J_uti_days_mean",
        "J_val_tot_mean",
        "J_val_tot_p90",
        "J_val_uti_share",
        "J_sex_f_share",
        "J_sex_m_share",
        "J_age_60p_share",
        "J_age_15_59_share",
        "J_age_0_14_share",
        "J_missing_raca_share",
        "J_raca_branca_share",
        "J_raca_preta_share",
        "J_raca_outras_share",
        "J00_06_share",
        "J09_18_share",
        "J20_22_share",
        "J40_47_share",
        "J_bucket_entropy",
        "catchment_munic_unique",
        "catchment_top1_share",
        "catchment_entropy",
        "catchment_outside_local_share",
        "J_missing_diag_sec_share",
        "J_missing_proc_share",
    ],
)
df_final.to_csv("./Tabela_Agregada.csv", index=False)
