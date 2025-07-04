# 2ª Entrega–Exercícios de MA 37 (2025-1)

1. Consideremos agora três urnas, digamos $A$, $B$ e $C$, cada uma com a mesma probabilidade de ser  escolhida, $1/3$. Em cada uma das urnas há seis bolas, cada uma com a mesma probabilidade de ser  escolhida, $1/6$. Na urna $A$ temos três bolas pretas e três bolas vermelhas; na urna $B$ temos duas bolas  pretas e quatro vermelhas; na urna $C$ todas as bolas são pretas.  Uma urna é escolhida aleatoriamente  e, em seguida, uma bola é escolhida aleatoriamente e observamos a cor dessa bola. Qual é a probabilidade da bola sorteada ser preta? Essa probabilidade depende do número de bolas na urna $C$?
2. Suponha que *probabilite* é um vírus que afeta $10\%$ da população de estudantes universitários (essa taxa é conhecida, em epidemiologia,  como *prevalência* da doença). Um  professor de Probabilidade aplica um teste que detecta *probabilite* mas eventualmente se engana: $3\%$ de falsos positivos ($97\%$ é a *especificidade* do teste) e $1\%$ de falsos negativos ($99\%$ é a *especificidade*).  Se for detectado *probabilite* em um indivíduo escolhido ao acaso nessa população, qual é a probabilidade que ele tenha o vírus?  
3. Agora, supondo que *probabilite*  seja uma contaminação muito rara,  digamos que apena $0{,}5\%$ da  população universitária tenha o vírus, e que o teste seja um pouco mais acurado, só há $1\%$ de chance de falsos positivos e falsos negativos.  Qual o valor preditivo positivo (probabilidade de ter o vírus dado que o teste foi positivo) do teste? A acurácia do teste garante utilidade diagnóstica nos casos em que a prevalência for muito baixa?
4. Um departamento universitário oferece dois cursos: **Curso A** (difícil) e **Curso B** (fácil). Dois grupos de estudantes — **Grupo 1** e **Grupo 2** — fizeram os dois cursos. A tabela abaixo mostra as taxas de aprovação: 

  | Curso   | Grupo   | Aprovados | Total | Taxa de Aprovação |
  | ------- | ------- | --------- | ----- | ----------------- |
  | Curso A | Grupo 1 | 672       | 800   | 84%               |
  | Curso A | Grupo 2 | 160       | 200   | 80%               |
  | Curso B | Grupo 1 | 170       | 200   | 85%               |
  | Curso B | Grupo 2 | 648       | 800   | 81%               |

  Qual **curso** teve maior taxa de aprovação em cada grupo, separadamente?

  Qual é a taxa total de aprovação de cada **curso**, considerando os dois grupos juntos?

  Explique o resultado obtido e por que ele é considerado paradoxal.

5. Sociólogos reconhecem um fenômeno chamado *difusão social*, que é a propagação de uma informação em uma população. Os membros da população podem ser divididos em duas classes: aqueles que possuem a informação e aqueles que ainda não a possuem.  Em uma população fixa de tamanho conhecido $N$, é razoável supor que a taxa de difusão seja proporcional ao número de indivíduos que possuem a informação vezes o número de indivíduos que ainda não a receberam. Se $X(t)$ denota o número de indivíduos que possuem a informação em uma população de tamanho $N$, então o modelo matemático para a difusão social é dado por:
   $$
   \frac{\text dX}{\text dt} = k X (N - X)
   $$
   onde $t$ representa o tempo e $k$ é uma constante positiva.
   
   (a) Resolva o modelo.
   
   (b) Em que instante a informação se espalha mais rapidamente?

   (c) Quantas pessoas eventualmente receberão a informação?

5. Os seguintes dados foram obtidos para o crescimento de uma população de ovelhas introduzida em um novo ambiente na ilha da Tasmânia (adaptado de Davidson, *On the Growth of the Sheep Population in Tasmania*, Trans. R. Soc. S. Australia 62 (1938): 342--346)
   $$
   \begin{array}{c|ccccccc}
   t \, (\text{ano}) & 1814 & 1824 & 1834 & 1844 & 1854 & 1864 \\
   \hline
   P(t) & 125 & 275 & 830 & 1200 & 1750 & 1650 \\
   \end{array}
   $$
   

   (a) Faça uma estimativa de $M$ através da plotagem de $P(t)$.

   (b) Plote $\ln \left(\frac{P}{M - P} \right)$ contra $t$. 

   (c) Estime $rM$ e $t^*$ (o instante em que $P'(t)$ é máximo).

​	
