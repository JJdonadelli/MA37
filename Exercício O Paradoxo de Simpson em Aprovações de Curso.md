### **Exercício: O Paradoxo de Simpson em Aprovações de Curso**

Um departamento universitário oferece dois cursos: **Curso A** (difícil) e **Curso B** (fácil). Dois grupos de estudantes — **Grupo 1** e **Grupo 2** — fizeram os dois cursos. A tabela abaixo mostra as taxas de aprovação:

#### Tabela de aprovações por curso:

| Curso   | Grupo   | Aprovados | Total | Taxa de aprovação |
| ------- | ------- | --------- | ----- | ----------------- |
| Curso A | Grupo 1 | 30        | 100   | 30%               |
| Curso A | Grupo 2 | 90        | 300   | 30%               |
| Curso B | Grupo 1 | 80        | 100   | 80%               |
| Curso B | Grupo 2 | 10        | 100   | 10%               |



**Pergunta 1:**
 Qual grupo teve maior taxa de aprovação em **cada curso**, separadamente?

**Pergunta 2:**
 Calcule a **taxa total de aprovação** de cada grupo, considerando os dois cursos juntos.

**Pergunta 3:**
 Explique o resultado obtido e por que ele é considerado paradoxal.

------

### ✅ **Solução Esperada**

#### Pergunta 1 — Comparação por curso:

- **Curso A:**
  - Grupo 1: 30 / 100 = **30%**
  - Grupo 2: 90 / 300 = **30%**
  - → Empate.
- **Curso B:**
  - Grupo 1: 80 / 100 = **80%**
  - Grupo 2: 10 / 100 = **10%**
  - → **Grupo 1 se saiu melhor**.

#### Pergunta 2 — Taxa total de aprovação:

- **Grupo 1:**
  - Total aprovados = 30 (A) + 80 (B) = 110
  - Total estudantes = 100 (A) + 100 (B) = 200
  - Taxa total = 110 / 200 = **55%**
- **Grupo 2:**
  - Total aprovados = 90 (A) + 10 (B) = 100
  - Total estudantes = 300 (A) + 100 (B) = 400
  - Taxa total = 100 / 400 = **25%**

→ **Grupo 1 tem taxa total maior (55%)**, mesmo tendo desempenho igual em A e muito melhor em B.

#### Pergunta 3 — Explicação do paradoxo:

Apesar de **Grupo 1 ter desempenho igual ou melhor em cada curso individualmente**, isso não garante que ele se saia melhor **no total** — o contrário pode acontecer, **dependendo da distribuição dos estudantes entre os cursos**.

Neste caso:

- **Grupo 1** se concentrou no Curso B (mais fácil).
- **Grupo 2** se concentrou no Curso A (mais difícil).

O paradoxo de Simpson mostra que **as médias ponderadas podem inverter relações aparentes**, se os **pesos (número de alunos)** forem distribuídos de forma desigual entre subgrupos.