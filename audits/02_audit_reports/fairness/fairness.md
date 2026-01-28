# Checklist Detalhada – Justiça / Fairness

**Objetivo:** Garantir que o modelo trate de forma justa diferentes subgrupos relevantes, documentando evidências claras para auditoria.

---

## Passo 1: Identificação de grupos relevantes
- [ ] Liste todos os **subgrupos relevantes** para o contexto clínico ou operacional.  
      Ex.: gênero, idade, região, comorbidades.  
      **Arquivo / link:** __________________________  
- [ ] Justifique a escolha de cada grupo em termos de **impacto clínico, ético ou regulatório**.  
      **Arquivo / link:** __________________________  

---

## Passo 2: Preparação dos dados
- [ ] Certifique-se de que **cada subgrupo possui amostra suficiente** para análise estatística.  
- [ ] Trate desbalanceamentos usando **reamostragem ou ponderação** se necessário.  
      Ferramenta sugerida: `SMOTE`, `SMOTEENN`, ou `FairLearn.preprocessing`.  
      **Arquivo / link:** __________________________  

---

## Passo 3: Cálculo de métricas por grupo
- [ ] Selecione métricas relevantes de desempenho:  
      - Classificação: `Accuracy`, `F1-score`, `Sensitivity`, `Specificity`  
      - Probabilísticas: `Brier Score`, `Calibration`  
- [ ] Calcule métricas **individualmente para cada grupo**.  
      Ferramentas sugeridas: `Aequitas`, `FairLearn`.  
      **Arquivo / link:** __________________________  

---

## Passo 4: Auditoria de disparidade
- [ ] Compare métricas entre grupos para identificar **disparidades significativas**.  
- [ ] Documente diferenças numéricas e interpretação ética.  
      **Arquivo / link:** __________________________  

---

## Passo 5: Mitigação de viés (se necessário)
- [ ] Se houver disparidade acima do limiar aceitável:  
      - Aplique **técnicas de mitigação de viés**: reamostragem, ponderação, algoritmos fairness-aware (ex.: `FairLearn mitigation`)  
      - Recalcule métricas pós-mitigação  
      **Arquivo / link:** __________________________  

---

## Passo 6: Documentação e relatório
- [ ] Gere um **Fairness Report** consolidando:  
      - Grupos analisados  
      - Métricas por grupo antes e depois da mitigação  
      - Interpretação dos resultados  
      - Decisões tomadas e justificativas  
      **Arquivo / link:** `fairness_report.md`  
- [ ] Inclua links ou screenshots de gráficos, tabelas e análises relevantes  

---

## Observações do Desenvolvedor
> Anote decisões, limitações ou pontos críticos do processo.
