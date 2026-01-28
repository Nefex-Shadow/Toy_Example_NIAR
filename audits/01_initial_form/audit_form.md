# Formulário de Auditoria de Inteligência Artificial Responsável

## NIAR-Saúde — Toy Example (Etapa Inicial: Modelo sem Dimensões Implementadas)

---

### Objetivo do Formulário

Este formulário registra o **primeiro ciclo de auditoria** de um projeto de IA que **ainda não implementou** explicitamente as dimensões de Auditabilidade, Explicabilidade, Transparência e Justiça. O objetivo é:

* Tornar explícitas as **lacunas de evidência**;
* Orientar o projeto sobre **quais artefatos devem ser produzidos**;
* Servir como instrumento pedagógico para calibração de avaliadores.

Este formulário **não tem caráter sancionatório**. Ele documenta o estado atual do projeto e orienta os próximos passos.

---

## 1. Identificação do Projeto

* **Título do projeto:** Toy Example - NIAR Saúde
* **Coordenação responsável:** Joe Smith 
* **Equipe técnica:** Emily Johnson, Michael Brown
* **Instituição / Unidade:** UFMG/DCC
* **Data da auditoria:** 28/01/2026
* **Versão do formulário:** 1.0 (Toy Example)
* **Auditor(es):** Sarah Davis, Robert Wilson

---

## 2. Artefatos Recebidos na Submissão Inicial

Marque os artefatos efetivamente entregues pelo projeto no momento da auditoria.

* ☑ `project_doc.md` — Documento de definição do Toy Example
* ☐ `model_card.md`
* ☐ `data_card.md`
* ☐ `metrics_report.md`
* ☐ `fairness_report.md`
* ☐ `explainability_report.md`
* ☐  Run_manifest / scripts / notebooks
* ☑ Repositório versionado


**Observação do auditor:**
O projeto apresentou apenas o documento de definição (`project_doc.md`). Nenhum artefato relacionado às dimensões de IA responsável foi fornecido até o momento.


---

## 3. Avaliação por Dimensão

### 3.1 Auditabilidade

**Pergunta-chave:** É possível reconstruir e inspecionar o sistema a partir das evidências fornecidas?

| Item de Verificação                                | Evidência apresentada? | Observações do auditor |
| -------------------------------------------------- | ---------------------- | ---------------------- |
| Identificação clara do modelo (nome, versão, data) | ☑ Parcial ☐ Sim ☐ Não  | `project_doc.md` menciona o modelo, mas não detalha versões ou data completa. |
| Origem e escopo dos dados documentados             | ☐ Sim ☑ Parcial ☐ Não  | Alguns dados gerais são mencionados, sem rastreabilidade completa. |
| Decisões de modelagem justificadas                 | ☑ Parcial ☐ Sim ☐ Não  | Estratégia do modelo descrita no documento, mas não há scripts ou logs. |
| Scripts ou notebooks disponíveis                   | ☐ Sim ☐ Parcial ☑ Não  | Nenhum script ou notebook submetido. |
| Possibilidade de auditoria retrospectiva           | ☐ Sim ☐ Parcial ☑ Não  | Sem evidência de rastreabilidade histórica. |

**Síntese da dimensão – Auditabilidade:**  
Evidência parcial apenas no nível conceitual, sem artefatos reproduzíveis.


---

### 3.2 Explicabilidade

**Pergunta-chave:** O funcionamento e os resultados do modelo são inteligíveis para seu uso declarado?

| Item de Verificação                               | Evidência apresentada? | Observações do auditor |
| ------------------------------------------------- | ---------------------- | ---------------------- |
| Tipo de modelo e lógica geral descritos           | ☐ Sim ☑ Parcial ☐ Não  | `project_doc.md` descreve a arquitetura geral. |
| Explicações globais do comportamento              | ☐ Sim ☑ Parcial ☐ Não  | Há menção conceitual, mas sem métricas ou visualizações. |
| Explicações condicionais (tempo, grupo, variável) | ☐ Sim ☐ Parcial ☑ Não  | Nenhuma evidência fornecida. |
| Limitações explicativas explicitadas              | ☐ Sim ☑ Parcial ☐ Não  | Limitações gerais mencionadas, mas não detalhadas. |
| Adequação ao público-alvo                         | ☐ Sim ☑ Parcial ☐ Não  | Documento sugere público, mas sem documentação adaptada. |

**Síntese da dimensão – Explicabilidade:**  
Informações apenas conceituais; sem relatórios ou visualizações detalhadas.

---

### 3.3 Transparência

**Pergunta-chave:** O sistema comunica claramente seu propósito, limites e riscos?

| Item de Verificação                | Evidência apresentada? | Observações do auditor |
| ---------------------------------- | ---------------------- | ---------------------- |
| Propósito do modelo explicitado    | ☐ Sim ☑ Parcial ☐ Não  | Propósito do modelo descrito no `project_doc.md`. |
| Usos não recomendados documentados | ☐ Sim ☐ Parcial ☑ Não  | Nenhum uso não recomendado formalmente listado. |
| Suposições do modelo descritas     | ☐ Sim ☑ Parcial ☐ Não  | Algumas suposições conceituais mencionadas. |
| Métricas reportadas e justificadas | ☐ Sim ☐ Parcial ☑ Não  | Sem métricas formais submetidas. |
| Riscos e incertezas documentados   | ☐ Sim ☐ Parcial ☑ Não  | Nenhuma documentação detalhada. |

**Síntese da dimensão – Transparência:**  
Evidência limitada, apenas conceitual; não há métricas nem análise de risco formal.


---

### 3.4 Justiça (Fairness)

**Pergunta-chave:** O projeto avaliou e documentou possíveis impactos desiguais entre grupos relevantes?

| Item de Verificação                  | Evidência apresentada? | Observações do auditor |
| ------------------------------------ | ---------------------- | ---------------------- |
| Grupos relevantes definidos          | ☐ Sim ☐ Parcial ☑ Não  | Nenhuma definição formal de subgrupos. |
| Justificativa contextual dos grupos  | ☐ Sim ☐ Parcial ☑ Não  | Não fornecido. |
| Métricas calculadas por grupo        | ☐ Sim ☐ Parcial ☑ Não  | Nenhuma métrica de fairness apresentada. |
| Análise de disparidades apresentada  | ☐ Sim ☐ Parcial ☑ Não  | Nenhuma análise de disparidade realizada. |
| Interpretação e decisão documentadas | ☐ Sim ☐ Parcial ☑ Não  | Não aplicável neste estágio. |

**Síntese da dimensão – Justiça:**  
Nenhuma evidência de avaliação de fairness apresentada; a dimensão ainda não foi implementada.

---

## 4. Consolidação Geral da Auditoria

### 4.1 Síntese Integrada

* **Principais lacunas identificadas:** Falta de relatórios formais (`model_card.md`, `fairness_report.md`, etc.) e ausência de scripts ou métricas detalhadas.  
* **Dimensões não evidenciadas:** Auditabilidade (parcial), Explicabilidade (parcial), Transparência (parcial), Justiça (ausente).  
* **Riscos institucionais potenciais:** Diferença entre documentação conceitual e evidências reproduzíveis pode gerar risco de interpretação errônea ou falta de rastreabilidade.


### 4.2 Boas Práticas Observadas (se houver)


* Documentação conceitual do modelo (`project_doc.md`) é clara e organizada, fornecendo uma **base inicial** para o ciclo de auditoria.


---

## 5. Recomendações para o Próximo Ciclo

| Dimensão        | Artefato recomendado             | Prioridade | Observação |
| --------------- | -------------------------------- | ---------- | ---------- |
| Auditabilidade  | `model_card.md` completo / scripts | Alta       | Necessário detalhar versões, dados e logs. |
| Explicabilidade | `explainability_report.md`         | Média      | Incluir métricas, visualizações e limitações detalhadas. |
| Transparência   | Revisão de escopo e limitações    | Alta       | Documentar riscos e métricas de forma formal. |
| Justiça         | `fairness_report.md`               | Alta       | Definir subgrupos, métricas e análise de disparidade. |


---

## 6. Declaração Final do Auditor

> Este formulário documenta o estado inicial do projeto no que se refere às dimensões de Inteligência Artificial Responsável. A ausência de evidências nesta etapa é esperada no toy example e serve como base para orientar a evolução progressiva do projeto em ciclos subsequentes de auditoria.

**Assinatura do auditor:**
**Data:**
