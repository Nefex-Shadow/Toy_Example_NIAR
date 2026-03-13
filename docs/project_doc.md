# FIAR Saúde - Documentação Inicial do Projeto

Este documento corresponde à fase de **Documentação inicial** no ciclo de auditoria do FIAR.

Objetivos:

1. Registrar o **contexto institucional e escopo do sistema de IA**
2. Identificar **riscos iniciais**
3. Mapear **evidências preliminares de Responsible AI**
4. Referenciar os **artefatos técnicos do projeto**

Cada item de verificação corresponde a um **controle de Responsible AI** que poderá ser avaliado durante auditorias futuras.


Status indica o **estágio de implementação** do controle:


| Status         | Significado                    |
| -------------- | ------------------------------ |
| Concluído    | Evidência documentada          |
| Parcial      | Implementação incompleta       |
| Não iniciado | Evidência ainda não disponível |


## 1. Informações Gerais

| Item | Descrição |
| :--- | :--- |
| **Título do projeto** | Previsão de Internações Respiratórias no SUS com IA Responsável |
| **Objetivo** | Desenvolver um modelo preditivo para estimar internações respiratórias mensais no SUS |
| **Uso pretendido**| Apoiar planejamento hospitalar e monitoramento epidemiológico |
| **Instituição / Unidade / Laboratório** | DCC/UFMG/NIAR |
| **Equipe Responsável** | NIAR |
| **Versão do documento** | 1.0 |
| **Data** | 12/03/2026 |


---

## 2. Contexto do Sistema

Esta seção descreve o **contexto institucional e o perfil de risco do sistema de IA**.

   
| Campo                             | Descrição                                                                     |
| --------------------------------- | ----------------------------------------------------------------------------- |
| **Domínio de aplicação**          | Saúde pública                                                                 |
| **Uso operacional**               |                                                                               |
| **Escala geográfica**             | nacional  (Brasil)                                                            |
| **Fonte principal de dados**      | SIH/SUS – DataSUS                                                             |
| **Stakeholders principais**       | Gestores do SUS, secretarias estaduais, planejamento hospitalar               |
| **Tipo de impacto**               | Planejamento e alocação de recursos                                           |
| **Nível de risco estimado**       | Médio                                                                         |
| **Riscos potenciais identificados**             | Disparidades regionais, previsões menos precisas em regiões sub-representadas |


---

## 3. Escopo do Modelo

| Campo | Descrição |
| :--- | :--- |
| **Uso pretendido** | Modelo de exemplo para testes internos e demonstração de auditoria. |
| **Tipo de modelo** | Regressão de contagem com Gradient Boosting |
| **Unidade de análise** | Hospital x mês| 
| **Variável alvo** | Número mensal de internações respiratórias (CID-10 capítulo J)| 
| **Dados utilizados** | Dados públicos do SIH/SUS (DataSUS), de janeiro de 2022 a novembro de 2025 |
| **Variáveis principais** | Histórico de internações, indicadores hospitalares, variáveis demográficas agregadas |
| **Limitações conhecidas** | Disparidades regionais residuais; ausência de inferência causal; dados agregados que limitam interpretações individuais |



---

## 4. Mapeamento Inicial por Dimensão de Responsible AI

Preencha as evidências, observações ou links para relatórios/artefatos correspondentes.

---

### 4.1 Auditabilidade

| ID     | Item de Verificação                          | Evidência / Artefato              | Link | Status | Responsável | Observações |
| ------ | -------------------------------------------- | --------------------------------- | ---- | ------ | ----------- | ----------- |
| AUD-01 | Identificação do modelo (nome, versão, data) | Model Card                        | [Model Cards](Model_Card)      |        | equipe de modelagem           |             |
| AUD-02 | Origem e escopo dos dados documentados       | Data Card                         | [Data Cards](Data_Card)      |        | equipe de dados            |             |
| AUD-03 | Rastreamento de datasets                     | Versionamento de dados            | scripts/     |        | equipe de dados           |             |
| AUD-04 | Decisões de modelagem justificadas           | Documentação experimental         |      |        | equipe de modelagem            |             |
| AUD-05 | Scripts ou notebooks disponíveis             | Repositório do projeto            |      |        | equipe técnica            |             |
| AUD-06 | Reprodutibilidade experimental               | Seeds fixos e ambiente versionado |      |        | coordenação FIAR            |             |

---

### 4.2 Explicabilidade

| ID     | Item de Verificação                        | Evidência / Artefato         | Link | Status | Responsável | Observações |
| ------ | ------------------------------------------ | ---------------------------- | ---- | ------ | ----------- | ----------- |
| EXP-01 | Tipo de modelo e lógica geral documentados | Model Card                   |      |        |             |             |
| EXP-02 | Explicações globais                        | SHAP summary plot            |      |        |             |             |
| EXP-03 | Explicações locais                         | SHAP waterfall plots         |      |        |             |             |
| EXP-04 | Interpretação das variáveis relevantes     | Relatório de explicabilidade |      |        |             |             |
| EXP-05 | Limitações explicativas documentadas       | Seção de limitações          |      |        |             |             |
| EXP-06 |  Adequação ao público-alvo                 |                              |      |        |             |             |    

---

### 4.3 Justiça (Fairness)

| ID     | Item de Verificação                    | Evidência / Artefato             | Link | Status | Responsável | Observações |
| ------ | -------------------------------------- | -------------------------------- | ---- | ------ | ----------- | ----------- |
| FAI-01 | Grupos relevantes definidos            | Documento de definição de grupos |      |        |             |             |
| FAI-02 | Justificativa contextual dos grupos    | Relatório metodológico           |      |        |             |             |
| FAI-03 | Métricas por subgrupo                  | Relatório de fairness            |      |        |             |             |
| FAI-04 | Análise de disparidades                | Relatório de avaliação           |      |        |             |             |
| FAI-05 | Decisões de mitigação documentadas     | Fairness report                  |      |        |             |             |
| FAI-06 | Estratégias de mitigação implementadas | Reamostragem ou ajuste           |      |        |             |             |


---

### 4.4 Privacidade

| ID     | Item de Verificação              | Evidência / Artefato   | Link | Status | Responsável | Observações |
| ------ | -------------------------------- | ---------------------- | ---- | ------ | ----------- | ----------- |
| PRI-01 | Identificação de dados sensíveis | Data Card              |      |        |             |             |
| PRI-02 | Procedimentos de anonimização    | Documentação de dados  |      |        |             |             |
| PRI-03 | Conformidade com LGPD            | Avaliação legal        |      |        |             |             |
| PRI-04 | Controle de acesso aos dados     | Política institucional |      |        |             |             |
| PRI-05 | Política de retenção de dados    | Política de dados      |      |        |             |             |


---

### 4.5 Governança

| ID     | Item de Verificação                           | Evidência / Artefato | Link | Status | Responsável | Observações |
| ------ | --------------------------------------------- | -------------------- | ---- | ------ | ----------- | ----------- |
| GOV-01 | Definição de responsabilidades institucionais | Documento do projeto |      |        |             |             |
| GOV-02 | Monitoramento do projeto                      | Plano de supervisão  |      |        |             |             |
| GOV-03 | Conformidade regulatória                      | Avaliação jurídica   |      |        |             |             |
| GOV-04 | Protocolos de auditoria                       | Procedimentos FIAR   |      |        |             |             |
| GOV-05 | Planos de mitigação e melhoria                | Plano de ação        |      |        |             |             |


---

## 5. Artefatos e Estrutura do Projeto

Indique quais artefatos estão disponíveis e adicione links ou anexos.

| Artefato | Link  |
| :--- | :--- |
| **Model Card** | [Model Cards](Model_Card)  |
| **Data Card** | [Data Cards](Data_Card)  |
| **Metrics Report** | `docs/metrics_report.md` |
| **Fairness Report** | `docs/Justica/fairness_report.md` |
| **Explainability Report** | `docs/Explicabilidade/explainability_report.md` |
| **Privacy Report** | `docs/privacy_report.md` |
| **Governance Report** | `docs/governance_report.md` |
| **Scripts e Notebooks** | `notebooks/` |

---

## 6. Observações Adicionais

* Este documento é a porta de entrada para o ciclo de auditoria FIAR.
* Evidências detalhadas devem ser registradas nos relatórios específicos de artefatos.
* Se houver alguma atualização no documento ele deve ser **versionado**. 


---

## 7. Histórico de Revisões

| Versão | Data | Alterações | Autor |
| :--- | :--- | :--- | :--- |
| 1.0 | 12/03/2026 | Consolidação do estudo de caso | Coordenação FIAR |
