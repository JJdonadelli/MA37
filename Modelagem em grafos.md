# Modelagem em grafos

Muitos problemas práticos relativos a relacionamentos, redes, escalonamento ou atribuições podem ser
modelados matematicamente na linguagem da teoria dos grafos. Neste capítulo, apresentamos alguns
conceitos básicos da teoria dos grafos e um problema de exemplo com uma solução algorítmica elegante.

## EXEMPLO INTRODUTÓRIO

No GoogleMaps, assim como em muitos carros modernos, você tem a possibilidade de inserir duas
localizações geográficas, A e B, e obter a "rota mais curta" de A a B. Geralmente, há diferentes opções para
interpretar "mais curto". É claro que, na maioria dos casos, isso não significará "distância euclidiana mais
curta", porque nesse caso a solução seria trivial, portanto desinteressante, ou seja, a linha reta passando
por A e B. O que torna o problema interessante e não trivial é a "rede de ruas" subjacente, onde uma "rota"
de A a B só pode seguir essas ruas. Além disso, "mais curto" pode significar "comprimento mínimo" ou
"duração mínima", ou seja, a rota "mais rápida". Por último, mas não menos importante, vários critérios
podem ser aplicados para escolher ruas apropriadas, por exemplo, evitar pedágios, evitar rodovias, preferir estradas cênicas, calcular rotas de bicicleta, etc. Como exemplo, veja a Figura 2.1, que mostra a rota de bicicleta mais rápida da JKU Linz até o Instituto RISC em Hagenberg1 .

![image-20250509112516630](/home/yair/.config/Typora/typora-user-images/image-20250509112516630.png)

## TEORIA DOS GRAFOS

Os grafos se tornarão um modelo matemático apropriado para uma “rede de ruas”, conforme necessário no exemplo de roteamento da Seção 2.1. Informalmente, no cerne do conceito de um grafo está uma coleção de entidades, chamadas vértices, com conexões entre elas, chamadas arestas ou arcos, veja a Figura 2.2. Existem diferentes tipos de grafos, dependendo se, por exemplo
• as conexões são orientadas ou não,
• pode haver mais de uma aresta entre dois vértices,
• os vértices conectados por uma aresta devem ser distintos,
• as arestas têm valores associados,
• os vértices têm valores associados,
• etc. etc.

![image-20250509112639918](/home/yair/.config/Typora/typora-user-images/image-20250509112639918.png)

Um **grafo** é uma coleção de vértices (ou nós) conectados por arestas (ou arcos). As definições a seguir formalizam diferentes tipos de grafos.

**Grafo Simples Não-Direcionado e Grafo Simples Direcionado**

Seja $V$ um conjunto. O par $G = (V, E)$ é um grafo simples não-direcionado se e somente se:
$$
E \subseteq \mathcal{P}(V) \quad \text{e} \quad \forall a \in E, \ |a| = 2.
$$
O par $G = (V, E)$  é um **grafo simples direcionado** se e somente se:
$$
E \subseteq V^2 \quad \text{e} \quad \forall a = (a_1, a_2) \in E, \ a_1 \neq a_2.
$$
Observe que usamos conjuntos para representar arestas, o que implica que não pode haver múltiplas
arestas entre dois vértices. Para certas aplicações, no entanto, é necessário permitir múltiplas arestas entre vértices. Nestes casos, as arestas E podem ser definidas como multiconjuntos.



**Vizinhança**

O vértice \( v \) é vizinho de \( u \) se \( uv \in E(G) \). A vizinhança de \( u \) é:
\[
N_G(u) := \{ v \in V(G) \mid uv \in E(G) \}.
\]

\subsection*{Definição 2.5: Caminhada, Trilha, Caminho}

Uma sequência finita alternada de vértices e arestas é uma:

\begin{itemize}[noitemsep]
  \item \textbf{Caminhada} de comprimento \( n \): pode repetir vértices e arestas.
  \item \textbf{Trilha}: uma caminhada sem repetição de arestas.
  \item \textbf{Caminho}: uma trilha sem repetição de vértices.
\end{itemize}

\subsection*{Definição 2.7: Grafo Ponderado}

Um grafo ponderado é um triplo \( G = (V, E, c) \) tal que \( (V, E) \) é um grafo e \( c : E \rightarrow \mathbb{R} \) é a função de custo associada às arestas.

\subsection*{Definição 2.8: Distância}

A distância entre dois vértices \( a \) e \( b \) em \( G \) é:
\[
\mathrm{dist}_G(a, b) := \min \left\{ \sum_{e \in E(w)} c(e) \mid w \text{ é uma caminhada de } a \text{ até } b \right\}.
\]