import pandas as pd
import numpy as np


def calculo_lag(ano, mes, lag):
    r_mes = mes - lag
    r_ano = ano
    if r_mes < 1:
        r_mes += 12
        r_ano -= 1
    return (r_ano, r_mes)


main_df = pd.read_csv("./Tabela_Agregada.csv")

dados_finais = []


def get_J_count_janela(df, ano, mes, tam):
    ano_piso, mes_piso = calculo_lag(ano, mes, tam)
    return df[
        ((df.year > ano_piso) | ((df.year == ano_piso) & (df.month >= mes_piso)))
        & ((df.year < ano) | ((df.year == ano) & (df.month < mes)))
    ]["J_count"]


ano = 2022
mes = 1

while ano < 2025 or mes < 12:
    print(ano, "/", mes)
    df_temp = main_df[(main_df.year == ano) & (main_df.month == mes)]
    hos_all = df_temp.CNES.unique()

    for hos in hos_all:
        hos_df = main_df[main_df.CNES == hos]

        # [0 - 6]
        val = [
            ano,  # year
            mes,  # month
            hos,  # CNES
            int((mes - 1) / 3 + 1),  # quarter
            ano * 12 + mes,  # time_index
            np.sin(2 * np.pi * mes / 12),  # sin_month
            np.cos(2 * np.pi * mes / 12),  # cos_month
        ]

        # LAG 1
        (l_ano, l_mes) = calculo_lag(ano, mes, 1)
        lag_1 = hos_df[(hos_df.year == l_ano) & (hos_df.month == l_mes)]

        # [7 - 29]
        if lag_1.empty:
            val.extend([np.nan for _ in range(0, 23)])
        else:
            val.extend(
                [
                    lag_1.J_count.values[0],  # J_count_lag1
                    lag_1.J00_06_share.values[0],  # J00_06_share_lag1
                    lag_1.J09_18_share.values[0],  # J09_18_share_lag1
                    lag_1.J20_22_share.values[0],  # J20_22_share_lag1
                    lag_1.J40_47_share.values[0],  # J40_47_share_lag1
                    lag_1.J_bucket_entropy.values[0],  # J_bucket_entropy_lag1
                    lag_1.J_morte_share.values[0],  # J_morte_share_lag1
                    lag_1.J_dias_perm_mean.values[0],  # J_dias_perm_mean_lag1
                    lag_1.J_dias_perm_p90.values[0],  # J_dias_perm_p90_lag1
                    lag_1.J_uti_share.values[0],  # J_uti_share_lag1
                    lag_1.J_uti_days_mean.values[0],  # J_uti_days_mean_lag1
                    lag_1.J_val_tot_mean.values[0],  # J_val_tot_mean_lag1
                    lag_1.J_val_tot_p90.values[0],  # J_val_tot_p90_lag1
                    lag_1.J_val_uti_share.values[0],  # J_val_uti_share_lag1
                    lag_1.J_sex_m_share.values[0],  # J_sex_m_share_lag1
                    lag_1.J_age_60p_share.values[0],  # J_age_60p_share_lag1
                    lag_1.J_missing_raca_share.values[0],  # J_missing_raca_share_lag1
                    lag_1.catchment_munic_unique.values[
                        0
                    ],  # catchment_munic_unique_lag1
                    lag_1.catchment_top1_share.values[0],  # catchment_top1_share_lag1
                    lag_1.catchment_entropy.values[0],  # catchment_entropy_lag1
                    lag_1.catchment_outside_local_share.values[
                        0
                    ],  # catchment_outside_local_share_lag1
                    lag_1.J_missing_diag_sec_share.values[
                        0
                    ],  # J_missing_diag_sec_share_lag1
                    lag_1.J_missing_proc_share.values[0],  # J_missing_proc_share_lag1
                ]
            )

        # LAG 2
        (l_ano, l_mes) = calculo_lag(ano, mes, 2)
        lag_2 = hos_df[(hos_df.year == l_ano) & (hos_df.month == l_mes)]

        # [30 - 35]
        if lag_2.empty:
            val.extend([np.nan for _ in range(0, 6)])
        else:
            val.extend(
                [
                    lag_2.J_count.values[0],  # J_count_lag2
                    lag_2.J00_06_share.values[0],  # J00_06_share_lag2
                    lag_2.J09_18_share.values[0],  # J09_18_share_lag2
                    lag_2.J20_22_share.values[0],  # J20_22_share_lag2
                    lag_2.J40_47_share.values[0],  # J40_47_share_lag2
                    lag_2.J_bucket_entropy.values[0],  # J_bucket_entropy_lag2
                ]
            )

        # LAG 3
        (l_ano, l_mes) = calculo_lag(ano, mes, 3)
        lag_3 = hos_df[(hos_df.year == l_ano) & (hos_df.month == l_mes)]

        # [36 - 58]
        if lag_3.empty:
            val.extend([np.nan for _ in range(0, 23)])
        else:
            val.extend(
                [
                    lag_3.J_count.values[0],  # J_count_lag3
                    lag_3.J00_06_share.values[0],  # J00_06_share_lag3
                    lag_3.J09_18_share.values[0],  # J09_18_share_lag3
                    lag_3.J20_22_share.values[0],  # J20_22_share_lag3
                    lag_3.J40_47_share.values[0],  # J40_47_share_lag3
                    lag_3.J_bucket_entropy.values[0],  # J_bucket_entropy_lag3
                    lag_3.J_morte_share.values[0],  # J_morte_share_lag3
                    lag_3.J_dias_perm_mean.values[0],  # J_dias_perm_mean_lag3
                    lag_3.J_dias_perm_p90.values[0],  # J_dias_perm_p90_lag3
                    lag_3.J_uti_share.values[0],  # J_uti_share_lag3
                    lag_3.J_uti_days_mean.values[0],  # J_uti_days_mean_lag3
                    lag_3.J_val_tot_mean.values[0],  # J_val_tot_mean_lag3
                    lag_3.J_val_tot_p90.values[0],  # J_val_tot_p90_lag3
                    lag_3.J_val_uti_share.values[0],  # J_val_uti_share_lag3
                    lag_3.J_sex_m_share.values[0],  # J_sex_m_share_lag3
                    lag_3.J_age_60p_share.values[0],  # J_age_60p_share_lag3
                    lag_3.J_missing_raca_share.values[0],  # J_missing_raca_share_lag3
                    lag_3.catchment_munic_unique.values[
                        0
                    ],  # catchment_munic_unique_lag1
                    lag_3.catchment_top1_share.values[0],  # catchment_top1_share_lag3
                    lag_3.catchment_entropy.values[0],  # catchment_entropy_lag3
                    lag_3.catchment_outside_local_share.values[
                        0
                    ],  # catchment_outside_local_share_lag1
                    lag_3.J_missing_diag_sec_share.values[
                        0
                    ],  # J_missing_diag_sec_share_lag1
                    lag_3.J_missing_proc_share.values[0],  # J_missing_proc_share_lag3
                ]
            )

        # LAG 6
        (l_ano, l_mes) = calculo_lag(ano, mes, 6)
        lag_6 = hos_df[(hos_df.year == l_ano) & (hos_df.month == l_mes)]

        # [59 - 64]
        if lag_6.empty:
            val.extend([np.nan for _ in range(0, 6)])
        else:
            val.extend(
                [
                    lag_6.J_count.values[0],  # J_count_lag6
                    lag_6.J00_06_share.values[0],  # J00_06_share_lag6
                    lag_6.J09_18_share.values[0],  # J09_18_share_lag6
                    lag_6.J20_22_share.values[0],  # J20_22_share_lag6
                    lag_6.J40_47_share.values[0],  # J40_47_share_lag6
                    lag_6.J_bucket_entropy.values[0],  # J_bucket_entropy_lag6
                ]
            )

        # LAG 12
        (l_ano, l_mes) = calculo_lag(ano, mes, 12)
        lag_12 = hos_df[(hos_df.year == l_ano) & (hos_df.month == l_mes)]

        # [65 - 87]
        if lag_12.empty:
            val.extend([np.nan for _ in range(0, 23)])
        else:
            val.extend(
                [
                    lag_12.J_count.values[0],  # J_count_lag12
                    lag_12.J00_06_share.values[0],  # J00_06_share_lag12
                    lag_12.J09_18_share.values[0],  # J09_18_share_lag12
                    lag_12.J20_22_share.values[0],  # J20_22_share_lag12
                    lag_12.J40_47_share.values[0],  # J40_47_share_lag12
                    lag_12.J_bucket_entropy.values[0],  # J_bucket_entropy_lag12
                    lag_12.J_morte_share.values[0],  # J_morte_share_lag12
                    lag_12.J_dias_perm_mean.values[0],  # J_dias_perm_mean_lag12
                    lag_12.J_dias_perm_p90.values[0],  # J_dias_perm_p90_lag12
                    lag_12.J_uti_share.values[0],  # J_uti_share_lag12
                    lag_12.J_uti_days_mean.values[0],  # J_uti_days_mean_lag12
                    lag_12.J_val_tot_mean.values[0],  # J_val_tot_mean_lag12
                    lag_12.J_val_tot_p90.values[0],  # J_val_tot_p90_lag12
                    lag_12.J_val_uti_share.values[0],  # J_val_uti_share_lag12
                    lag_12.J_sex_m_share.values[0],  # J_sex_m_share_lag12
                    lag_12.J_age_60p_share.values[0],  # J_age_60p_share_lag12
                    lag_12.J_missing_raca_share.values[0],  # J_missing_raca_share_lag12
                    lag_12.catchment_munic_unique.values[
                        0
                    ],  # catchment_munic_unique_lag12
                    lag_12.catchment_top1_share.values[0],  # catchment_top1_share_lag12
                    lag_12.catchment_entropy.values[0],  # catchment_entropy_lag12
                    lag_12.catchment_outside_local_share.values[
                        0
                    ],  # catchment_outside_local_share_lag12
                    lag_12.J_missing_diag_sec_share.values[
                        0
                    ],  # J_missing_diag_sec_share_lag12
                    lag_12.J_missing_proc_share.values[0],  # J_missing_proc_share_lag12
                ]
            )

        # Usado para calculo do moving average
        df_ma = main_df[["year", "month", "CNES", "J_count"]][main_df.CNES == hos]
        ma3 = get_J_count_janela(df_ma, ano, mes, 3)
        ma6 = get_J_count_janela(df_ma, ano, mes, 6)
        ma12 = get_J_count_janela(df_ma, ano, mes, 12)

        val_ma3 = np.nan
        if ma3.shape[0] == 3:
            val_ma3 = ma3.mean()

        val_ma6 = np.nan
        if ma6.shape[0] == 6:
            val_ma6 = ma6.mean()

        val_ma12 = np.nan
        if ma12.shape[0] == 12:
            val_ma12 = ma12.mean()

        val.extend(
            [
                val_ma3,  # J_count_ma3_lag1
                val_ma6,  # J_count_ma6_lag1
                val_ma12,  # J_count_ma12_lag1
                val[7] - val[30],  # J_growth_1m_lag1
                hos_df.J_count.values[0],  # J_count
            ]
        )

        dados_finais.append(val)

    mes += 1
    if mes > 12:
        mes -= 12
        ano += 1


df_final = pd.DataFrame(
    dados_finais,
    columns=[
        "year",
        "month",
        "CNES",
        "quarter",
        "time_index",
        "sin_month",
        "cos_month",
        "J_count_lag1",
        "J00_06_share_lag1",
        "J09_18_share_lag1",
        "J20_22_share_lag1",
        "J40_47_share_lag1",
        "J_bucket_entropy_lag1",
        "J_morte_share_lag1",
        "J_dias_perm_mean_lag1",
        "J_dias_perm_p90_lag1",
        "J_uti_share_lag1",
        "J_uti_days_mean_lag1",
        "J_val_tot_mean_lag1",
        "J_val_tot_p90_lag1",
        "J_val_uti_share_lag1",
        "J_sex_m_share_lag1",
        "J_age_60p_share_lag1",
        "J_missing_raca_share_lag1",
        "catchment_munic_unique_lag1",
        "catchment_top1_share_lag1",
        "catchment_entropy_lag1",
        "catchment_outside_local_share_lag1",
        "J_missing_diag_sec_share_lag1",
        "J_missing_proc_share_lag1",
        "J_count_lag2",
        "J00_06_share_lag2",
        "J09_18_share_lag2",
        "J20_22_share_lag2",
        "J40_47_share_lag2",
        "J_bucket_entropy_lag2",
        "J_count_lag3",
        "J00_06_share_lag3",
        "J09_18_share_lag3",
        "J20_22_share_lag3",
        "J40_47_share_lag3",
        "J_bucket_entropy_lag3",
        "J_morte_share_lag3",
        "J_dias_perm_mean_lag3",
        "J_dias_perm_p90_lag3",
        "J_uti_share_lag3",
        "J_uti_days_mean_lag3",
        "J_val_tot_mean_lag3",
        "J_val_tot_p90_lag3",
        "J_val_uti_share_lag3",
        "J_sex_m_share_lag3",
        "J_age_60p_share_lag3",
        "J_missing_raca_share_lag3",
        "catchment_munic_unique_lag3",
        "catchment_top1_share_lag3",
        "catchment_entropy_lag3",
        "catchment_outside_local_share_lag3",
        "J_missing_diag_sec_share_lag3",
        "J_missing_proc_share_lag3",
        "J_count_lag6",
        "J00_06_share_lag6",
        "J09_18_share_lag6",
        "J20_22_share_lag6",
        "J40_47_share_lag6",
        "J_bucket_entropy_lag6",
        "J_count_lag12",
        "J00_06_share_lag12",
        "J09_18_share_lag12",
        "J20_22_share_lag12",
        "J40_47_share_lag12",
        "J_bucket_entropy_lag12",
        "J_morte_share_lag12",
        "J_dias_perm_mean_lag12",
        "J_dias_perm_p90_lag12",
        "J_uti_share_lag12",
        "J_uti_days_mean_lag12",
        "J_val_tot_mean_lag12",
        "J_val_tot_p90_lag12",
        "J_val_uti_share_lag12",
        "J_sex_m_share_lag12",
        "J_age_60p_share_lag12",
        "J_missing_raca_share_lag12",
        "catchment_munic_unique_lag12",
        "catchment_top1_share_lag12",
        "catchment_entropy_lag12",
        "catchment_outside_local_share_lag12",
        "J_missing_diag_sec_share_lag12",
        "J_missing_proc_share_lag12",
        "J_count_ma3_lag1",
        "J_count_ma6_lag1",
        "J_count_ma12_lag1",
        "J_growth_1m",
        "J_count",
    ],
)


df_final.to_csv("./Tabela_lag_Final.csv", index=False)
