# SIHSUS - Internações por doenças respiratórias

Dados processados a partir dos dados do DataSUS, filtrados por doenças respiratórias.
Usados para criar um modelo de ML para predição de internações
para um hospital em um mês.

#### Dataset Link
<!-- info: Provide a link to the dataset: -->
<!-- width: half -->
<https://github.com/Nefex-Shadow/Toy_Example_NIAR/blob/main/SIH_Dados/Tabela_lag_Final.zip>

#### Data Card Author(s)
<!-- info: Select **one role per** Data Card Author:

(Usage Note: Select the most appropriate choice to describe the author's role
in creating the Data Card.) -->
<!-- width: half -->
- **Luís Eduardo Limas Brito, NIAR:** Owner

## Authorship

### Publishers

#### Publishing Organization(s)
<!-- scope: telescope -->
<!-- info: Provide the names of the institution or organization responsible
for publishing the dataset: -->
NIAR, UFMG

#### Industry Type(s)
<!-- scope: periscope -->
<!-- info: Select **all applicable** industry types to which the publishing
organizations belong: -->
- Grupo de Pesquisa - Tech

#### Contact Detail(s)
<!-- scope: microscope -->
<!-- info: Provide publisher contact details: -->
- **Affiliation:** UFMG
- **Contact:** <lelimasbrito@gmail.com>

### Dataset Owners

#### Team(s)
<!-- scope: telescope -->
<!-- info: Provide the names of the groups or team(s) that own the dataset: -->
DataSUS

#### Contact Detail(s)
<!-- scope: periscope -->
<!-- info: Provide pathways to contact dataset owners: -->
- **Dataset Owner(s):** Luís Eduardo Limas Brito
- **Affiliation:** NIAR Saúde
- **Contact:** <lelimasbrito@gmail.com>

## Dataset Overview

#### Data Subject(s)
<!-- scope: telescope -->
<!-- info: Select ***all applicable**** subjects contained the dataset: -->
- Sensitive Data about people
- Non-Sensitive Data about people
- Data about places and objects
- Data about monthly happenings

#### Dataset Snapshot
<!-- scope: periscope -->
<!-- info: Provide a snapshot of the dataset:<br><br>(Use the additional notes
to include relevant information, considerations, and links to table(s) with
more detailed breakdowns.) -->
Category | Data
--- | ---
Size of Dataset | 128.6 MB
Number of Instances | 161585
Number of Fields | 94
Labeled Classes | 0

**Above:** Informações de Tabela_lag_Final.csv.

#### Content Description
<!-- scope: microscope -->
<!-- info: Provide a short description of the content in a data point: -->
Dados criados a partir dos dados disponibilizados pelo DataSUS. Eles foram passados por uma etapa de pré processamento, onde foram agrupadas em valores totais, médias ou razões. Além disso, por ser um modelo de previsão, cada linha contém dados de meses passados.

**Additional Notes:** Os dados foram agrupados por hospitais, em um dado mês/ano.

#### Descriptive Statistics
<!-- width: full -->
<!-- info: Provide basic descriptive statistics for each field.

Use additional notes to capture any other relevant information or
considerations.

Usage Note: Some statistics will be relevant for numeric data, for not for
strings. -->

Statistic | J_count | J_dias_perm_mean_lag1 | J_bucket_entropy_lag2 | J_val_tot_mean_lag3 | J00_06_share_lag6 | Field Name
--- | --- | --- | --- | --- | --- | ---
count | 161584.000000 | 156500.000000 | 152801.000000 | 149152.000000 | 138358.000000 | 117347.000000
mean | 31.296601 | 5.606571 | 0.549438 | 1211.331608 | 0.033241 | 0.819023
std | 35.106042 | 3.825802 | 0.359922 | 1489.730747 | 0.087863 | 0.225511
min | 1.000000 | 0.000000 | 0.000000 | 40.380000 | 0.000000 | 0.056818
25% | 10.000000 | 3.333333 | 0.295439 | 541.308549 | 0.000000 | 0.681818
50% | 21.000000 | 4.769231 | 0.585953 | 599.880833 | 0.000000 | 0.923077
75% | 40.000000 | 6.888889 | 0.808270 | 1319.003567 | 0.027027 | 1.000000
max | 546.000000 | 341.000000 | 1.386294 | 64671.010000 | 1.000000 | 1.000000

**Above:** Tabela contendo exemplos de atributos usados para o treinar o modelo final.

### Sensitivity of Data

#### Sensitivity Type(s)
<!-- scope: telescope -->
<!-- info: Select ***all applicable*** data types present in the dataset: -->
- User Content
- User Metadata
- User Activity Data
- Identifiable Data
- Health Data

#### Risk Type(s)
<!-- scope: telescope -->
<!-- info: Select **all applicable** risk types presenting from the
dataset: -->
- Indirect Risk

#### Supplemental Link(s)
<!-- scope: periscope -->
<!-- info: Provide link(s) for documentation pertaining to sensitive data in
the dataset: -->
**Link Name or Document Type:** <https://datasus.saude.gov.br/informacoes-de-saude-tabnet/>

### Dataset Version and Maintenance

#### Maintenance Status
<!-- scope: telescope -->
<!-- info: Select **one:** -->
**Limited Maintenance** - The data will not be updated,
but any technical issues will be addressed.

#### Version Details
<!-- scope: periscope -->
<!-- info: Provide details about **this** version of the dataset: -->
**Current Version:** 1.0

**Last Updated:** 01/2026

**Release Date:** 01/2026

#### Maintenance Plan
<!-- scope: microscope -->
<!-- info: Summarize the maintenance plan for the dataset:

Use additional notes to capture any other relevant information or
considerations. -->
**Additional Notes:** Novos modelos serão criados usando o mesmo dataset,
a fim de comparação e análises.

#### Primary Data Modality
<!-- scope: telescope -->
<!-- info: Select **one**: -->
- Time Series

## Motivations & Intentions

### Motivations

#### Purpose(s)
<!-- scope: telescope -->
<!-- info: Select **one**: -->
- Research

#### Domain(s) of Application
<!-- scope: periscope -->
<!-- info: Provide a list of key domains of application that the dataset has
been designed for:<br><br>(Usage Note: Use comma-separated keywords.) -->
For example: `Machine Learning`, `Computer Vision`, `Object Detection`.

`Machine Learning`, `Time-Series`

#### Motivating Factor(s)
<!-- scope: microscope -->
<!-- info: List the primary motivations for creating or curating this dataset:

(Usage Note: use this to describe the problem space and corresponding
motivations for the dataset.) -->

Usar dados reais para implementação de um modelo de previsão.

### Intended Use

#### Dataset Use(s)
<!-- scope: telescope -->
<!-- info: Select **one**: -->
- Safe for research use

#### Suitable Use Case(s)
<!-- scope: periscope -->
<!-- info: Summarize known suitable and intended use cases of this dataset.

Use additional notes to capture any specific patterns that readers should
look out for, or other relevant information or considerations. -->
**Suitable Use Case:** Modelo de previsão.

**Suitable Use Case:** Estudos de histórico de hospitais.

**Additional Notes:** Apenas hospitais cadastrados no dataSUS estão presentes.

#### Unsuitable Use Case(s)
<!-- scope: microscope -->
<!-- info: Summarize known unsuitable and unintended use cases of this dataset.

Use additional notes to capture any specific patterns that readers should look
out for, or other relevant information or considerations. -->
**Unsuitable Use Case:** Estudos em cima de casos específicos de um paciente individual.

**Additional Notes:** O dataset contém apenas informações agregadas,
sem conter casos isolados.

## Access

#### Access Type
<!-- scope: telescope -->
<!-- info: Select **one**: -->
- External - Open Access

## Provenance

### Collection

#### Method(s) Used
<!-- scope: telescope -->
<!-- info: Select **all applicable** methods used to collect data: -->
- Taken from other existing datasets

#### Methodology Detail(s)
<!-- scope: periscope -->
<!-- info: Provide a description of each collection method used.

Use additional notes to capture any other relevant information or
considerations.

(Usage Note: Duplicate and complete the following for collection method
type.) -->
**Collection Type**

**Source:** Conexão ftp disponibilizado pelo dataSUS.

**Link:** ftp.datasus.gov.br

**Dates of Collection:** [01 2022 - 11 2025]

**Primary modality of collection data:**

- Tabular Data

**Update Frequency for collected data:**

*Usage Note: Select one for this collection type.*

- Monthly

**Additional Notes:**

#### Source Description(s)
<!-- scope: microscope -->
<!-- info: Provide a description of each upstream source of data.

Use additional notes to capture any other relevant information or
considerations. -->
- Os arquivos usados foram encontrados dentro da pasta
"/dissemin/publicos/SIHSUS/200801_/Dados/".
- Apenas arquivos que começam com RD foram usados.
- Foram usados arquivos de 2022/01 até 2025/11.
- Exceção: Os arquivos RDAC2511.dbc e RDRR2511.dbc não estavam disponíveis
quando os dados foram coletados.

#### Collection Cadence
<!-- scope: telescope -->
<!-- info: Select **all applicable**: -->
**Static:** Data was collected once from single or multiple sources.

#### Data Processing
<!-- scope: microscope -->
<!-- info: Summarize how data from different sources or methods aggregated,
processed, or connected.

Use additional notes to capture any other
relevant information or considerations.

(Usage Note: Duplicate and complete the following for each source OR
collection method.) -->
**Description:** Os dados foram transformados para ".csv" e, em seguida, filtrados baseados em colunas de interesse. As colunas foram usadas para calcular valores agregados que são usados na tabela final. A tabela final, no entanto, junta os dados de um mês com valores de dados passados.

**Methods employed:** Foram usados cinco scripts (python) para o processamento.
Um transforma os arquivos de ".dbc" para ".dbf" e outro de ".dbf" para ".csv".
Um terceiro faz a filtragem das colunas (com valores de interesse) e
linhas (cujo diagnóstico começa com "J", ou seja,
diagnóstico de doença respiratória).
Um quarto faz os cálculos, agregando os valores de cada coluna pelo hospital e pelo mês.
Finalmente, um último agrupa os valores mensais com defasagens temporais,
assim preparando o dataset final usado para treinar o modelo.

**Tools or libraries:**

- pyreaddbc: <https://pypi.org/project/pyreaddbc/>
- dbfread: <https://pypi.org/project/dbfread/>
- pandas: <https://pandas.pydata.org/>
- numpy: <https://numpy.org/>
