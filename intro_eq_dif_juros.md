## O que são Equações Diferenciais?

Uma equação diferencial é uma equação que relaciona uma função desconhecida com suas derivadas. Em termos simples, ela descreve como uma quantidade muda em relação a outra. No nosso caso, estudaremos como o dinheiro cresce ao longo do tempo quando sujeito a juros continuamente compostos.

## Do Discreto ao Contínuo: A Evolução dos Juros

### Juros Simples
No regime de juros simples, o capital cresce linearmente:
$$
M(t) = C_0(1 + rt)
$$
onde $C_0$ é o capital inicial, $r$ é a taxa de juros e $t$ é o tempo.

### Juros Compostos Discretos
Com capitalização em períodos discretos (anual, mensal, diário), temos:
$$
M(t) = C_0(1 + r/n)^{nt}
$$
onde $n$ é o número de capitalizações por unidade de tempo.

### O Limite: Juros Continuamente Compostos
Quando n → ∞, obtemos a capitalização contínua:
$$
M(t) = C_0e^{rt}
$$

## Derivando a Equação Diferencial

A beleza dos juros continuamente compostos está no fato de que a taxa de crescimento do capital é proporcional ao próprio capital em cada instante.

Se $M(t)$ representa o montante no tempo $t$, então:
- A taxa de variação instantânea é $dM/dt$
- Esta taxa é proporcional ao montante atual: $dM/dt = rM(t)$

Chegamos assim à nossa primeira equação diferencial:
$$
\frac{dM}{dt} = rM
$$
Esta é uma equação diferencial ordinária de primeira ordem, linear e homogênea.

## Resolvendo a Equação Diferencial

### Método de Separação de Variáveis

Reorganizando a equação:
$$
dM/dt = rM
$$
$$
dM/M = r dt
$$

Integrando ambos os lados:
$$
\int  dM/M = \int r dt
$$
$\ln|M| = rt + C'$.

Aplicando a exponencial:
$$
M(t) = Ae^{rt}
$$
onde $A = e^{C'}$ é uma constante a ser determinada pelas condições iniciais.

### Condições Iniciais

Se no tempo $t = 0$ temos um capital inicial $M(0) = M₀$, então:
$$
M₀ = Ae^{r·0} = A
$$

Portanto, a solução geral é: $M(t) = M₀e^{rt}$.

## Interpretação

### Propriedades da Solução Exponencial
1. **Crescimento acelerado**: A função cresce cada vez mais rapidamente
2. **Tempo de duplicação**: O capital dobra a cada $\ln(2)/r$ unidades de tempo
3. **Nunca atinge zero**: Para $r > 0$, $M(t) > 0$ para todo $t \geq 0$

## Exemplos

Um capital de R$ 1.000 é aplicado a 5% ao ano com capitalização contínua.
- M₀ = 1000, r = 0,05
- M(t) = 1000e^(0,05t)
- Após 10 anos: M(10) = 1000e^(0,5) ≈ R$ 1.649

Capital inicial: R$ 1.000, taxa: 10% ao ano, período: 5 anos

- Juros simples: M = 1000(1 + 0,1×5) = R$ 1.500
- Juros compostos anuais: M = 1000(1,1)⁵ ≈ R$ 1.611
- Juros contínuos: M = 1000e^(0,5) ≈ R$ 1.649

### Taxa Variável no Tempo
Se a taxa de juros varia com o tempo r(t), a equação se torna:
$$
\frac{dM}{dt} = r(t)M
$$
Solução: $M(t) = M₀ \exp\left(\int∫_0^t r(s)ds\right)$.

## Conceitos Fundamentais das Equações Diferenciais

### Classificação
- **Ordem**: Maior derivada presente (nossa equação é de 1ª ordem)
- **Linearidade**: Coeficientes são funções de t apenas
- **Homogeneidade**: Ausência de termo independente

### Métodos de Solução
1. **Separação de variáveis** (usado aqui)
2. **Fator integrante** (para equações lineares)
3. **Métodos numéricos** (para casos complexos)

### Condições Iniciais vs. Condições de Contorno
- **Inicial**: Valor da função em um ponto (M(0) = M₀)
- **Contorno**: Valores em múltiplos pontos

## Aplicações Além das Finanças

O modelo dM/dt = rM aparece em diversos contextos:

### Crescimento Populacional
```
dP/dt = kP
```
P(t) = P₀e^(kt), onde k é a taxa de natalidade líquida.

### Decaimento Radioativo
```
dN/dt = -λN
```
N(t) = N₀e^(-λt), onde λ é a constante de decaimento.

### Resfriamento de Newton
```
dT/dt = -k(T - T_ambiente)
```

### Crescimento de Bactérias
Em condições ideais, bactérias seguem crescimento exponencial.

## Limitações do Modelo Exponencial

### No Contexto Financeiro
1. **Inflação**: Pode corroer o valor real do dinheiro
2. **Risco**: Taxas reais podem flutuar
3. **Impostos**: Reduzem o retorno efetivo
4. **Custos de transação**: Impactam o crescimento

### Modelos Mais Realistas
- Incorporação de volatilidade (Movimento Browniano)
- Taxas estocásticas
- Efeitos macroeconômicos


O estudo dos juros continuamente compostos oferece uma porta de entrada natural e intuitiva ao mundo das equações diferenciais. A equação dM/dt = rM, apesar de sua simplicidade, encapsula conceitos fundamentais que aparecem em física, biologia, economia e engenharia.

A solução exponencial M(t) = M₀e^(rt) não é apenas uma fórmula matemática, mas uma descrição precisa de como quantidades crescem quando sua taxa de variação é proporcional ao seu valor atual. Esta é uma das ideias mais poderosas e recorrentes em toda a matemática aplicada.

Ao dominar este exemplo introdutório, você desenvolveu intuição para reconhecer quando processos naturais podem ser modelados por equações diferenciais, adquiriu ferramentas básicas de resolução e compreendeu a importância das condições iniciais na determinação de soluções únicas.

Este é apenas o começo de uma jornada fascinante através do universo das equações diferenciais, onde cada novo problema revela conexões profundas entre matemática e realidade.