# Guia de Testes — Parte 3
## Caronas Mackenzie — Otimização de Rotas na Malha Viária SP
**Disciplina:** Teoria dos Grafos — Turma 6G  
**Prof.:** Dr. Ivan Carlos Alcântara de Oliveira  
**Integrantes:** Daniela Pereira · Eduardo Takashi · Ricardo Lins Pires

---

## Pré-requisito: Carregar o Grafo

Antes de qualquer teste, **sempre execute a opção `a`** para carregar o arquivo `grafo.txt`.  
Os arquivos `caronas.py` e `grafo.txt` devem estar na mesma pasta.

```
Digite a opção (a-o): a
```

**Saída esperada:**
```
✅ Grafo carregado com sucesso! 80 vértices e 210 arestas.
```

---

## Opção J — Dijkstra: Caminho Mínimo entre Cruzamentos `[SOLUÇÃO]`

### O que é?
Implementação do **Algoritmo de Dijkstra** para encontrar o **caminho de menor distância
(em km)** entre dois cruzamentos da malha viária. Esta é a solução principal do problema
de caronas: encontrar a rota mais curta para o motorista buscar passageiros e chegar ao
Mackenzie.

### Pseudocódigo utilizado
```
Início DIJKSTRA(G, s)
  Para todo v em V: dist[v] <- ∞; prev[v] <- -1
  dist[s] <- 0
  Q <- fila de prioridade com todos os vértices
  Enquanto Q ≠ ∅:
    u <- vértice em Q com menor dist[u]
    Para todo vizinho v de u:
      alt <- dist[u] + peso(u, v)
      Se alt < dist[v]: dist[v] <- alt; prev[v] <- u
Fim.
Complexidade: O((V + A) log V)
```

---

### Teste J-1 — Rota da Zona Leste ao Mackenzie

**Entrada:**
```
Digite a opção (a-o): j
Vértice de ORIGEM  (número): 14
Vértice de DESTINO (número): 0
```

- **Vértice 14:** Cruzamento Avenida Projetada x Acesso Metrô Itaquera *(Zona Leste)*
- **Vértice 0:** Cruzamento Rua Maria Antônia x Rua Itambé *(próximo ao Mackenzie)*

**Saída esperada:**
```
─────────────────────────────────────────────────────────────────
  ORIGEM  : [14] Cruzamento Avenida Projetada x Acesso Metrô Itaquera
  DESTINO : [ 0] Cruzamento Rua Maria Antônia x Rua Itambé
─────────────────────────────────────────────────────────────────
  Distância mínima: XX.XX km
  Número de cruzamentos no trajeto: X
  Trajeto detalhado:
    [14] ... ← PARTIDA
    ...
    [ 0] ... ← CHEGADA
```

---

### Teste J-2 — Outra rota da Zona Leste ao Mackenzie

**Entrada:**
```
Digite a opção (a-o): j
Vértice de ORIGEM  (número): 17
Vértice de DESTINO (número): 0
```

- **Vértice 17:** Cruzamento Avenida Ragueb Chohfi x Avenida Jacu Pêssego *(Zona Leste extrema)*
- **Vértice 0:** Cruzamento Rua Maria Antônia x Rua Itambé *(próximo ao Mackenzie)*

---

### Teste J-3 — Rota sem caminho disponível (caso de erro esperado)

**Entrada:**
```
Digite a opção (a-o): j
Vértice de ORIGEM  (número): 0
Vértice de DESTINO (número): 76
```

**Saída esperada:**
```
❌ Não existe caminho de [0] até [76].
   Isso indica que não há rota viária direta entre os cruzamentos nas direções modeladas.
```

> **Obs.:** Este teste mostra que o grafo é **direcionado** — nem sempre é possível
> ir de qualquer ponto a qualquer outro pelas vias modeladas.

---

## Opção K — Analisar Graus dos Vértices `[Característica 1]`

### O que é?
Calcula o **grau de entrada** (quantas vias chegam ao cruzamento) e o
**grau de saída** (quantas vias partem do cruzamento) de cada vértice.  
Cruzamentos com alto grau são os melhores **pontos de encontro para caronas**.

### Complexidade
`O(V + A)`

---

### Teste K-1 — Graus do grafo original

**Entrada:**
```
Digite a opção (a-o): k
```

**O que observar na saída:**
- Tabela com todos os 80 vértices, grau de saída, grau de entrada e grau total.
- Estatísticas: grau médio, vértice com maior grau de saída, maior grau de entrada.
- Indicação se há vértices isolados.

**Trecho esperado:**
```
  ID    Grau Saída    Grau Entrada    Grau Total  Cruzamento
  ───────────────────────────────────────────────────────────────
  [ 0]           4               3           7  Cruzamento Rua Maria Antônia...
  ...
  ESTATÍSTICAS:
    Total de arestas                : 210
    Grau médio de saída             : 2.63
    ...
```

---

### Teste K-2 — Graus após inserir uma nova aresta

Primeiro insira uma aresta com a opção `d`:

**Entrada:**
```
Digite a opção (a-o): d
Origem (número do vértice): 0
Destino (número do vértice): 5
Distância em km: 3.5
```

Depois rode novamente os graus:

```
Digite a opção (a-o): k
```

**O que observar:** O grau de saída do vértice `0` e o grau de entrada do vértice `5`
devem ter aumentado em 1 em relação ao Teste K-1.

---

## Opção L — Verificar Percurso/Circuito Euleriano `[Característica 2]`

### O que é?
Verifica se o grafo possui:
- **Circuito Euleriano:** percorre **todas as arestas** exatamente uma vez e **retorna** ao início.
- **Percurso Euleriano:** percorre todas as arestas exatamente uma vez, mas **sem retornar**.
- **Não Euleriano:** não satisfaz nenhuma das condições acima.

### Condições verificadas (grafo orientado)
| Caso | Condição |
|------|----------|
| Circuito Euleriano | Fortemente conexo + `grau_entrada(v) = grau_saída(v)` para todo v |
| Percurso Euleriano | Conexo + exatamente 1 vértice com Δ=+1 (início) e 1 com Δ=−1 (fim) |
| Não Euleriano | Nenhuma das anteriores |

### Complexidade
`O(V + A)`

---

### Teste L-1 — Verificação com o grafo original

**Entrada:**
```
Digite a opção (a-o): l
```

**Saída esperada (resultado provável com o grafo real):**
```
  Vértices com grau_saída = grau_entrada     : XX
  Vértices com grau_saída - grau_entrada = +1: XX
  Vértices com grau_saída - grau_entrada = -1: XX
  Vértices fortemente desequilibrados (|Δ|>1): XX

  RESULTADO: NÃO É EULERIANO
```

> A malha viária real raramente é Euleriana, pois as vias têm sentidos
> assimétricos — o resultado `NÃO É EULERIANO` é o esperado e correto.

---

### Teste L-2 — Verificação após remover uma aresta

Remova uma aresta com a opção `f`:

**Entrada:**
```
Digite a opção (a-o): f
Origem: 1
Destino: 0
```

Em seguida, rode novamente:

```
Digite a opção (a-o): l
```

**O que observar:** Os contadores de vértices desequilibrados podem mudar,
evidenciando que a condição Euleriana é sensível à estrutura das arestas.

---

## Opção M — Verificar Caminho/Ciclo Hamiltoniano `[Característica 3]`

### O que é?
Verifica se o grafo admite:
- **Ciclo Hamiltoniano:** visita **todos os vértices** exatamente uma vez e **retorna** ao início.
- **Caminho Hamiltoniano:** visita todos os vértices exatamente uma vez, sem retornar.

### Estratégia de verificação
1. Verifica **forte conexidade** (condição necessária).
2. Aplica a **Condição de Ore** adaptada para grafos dirigidos.
3. Aplica a **Condição de Dirac** adaptada para grafos dirigidos.
4. Se as condições suficientes não forem satisfeitas, executa **backtracking** com limite de 50.000 tentativas.

> **Importante:** O problema Hamiltoniano é **NP-completo**. Para grafos
> com 80 vértices, o backtracking pode atingir o limite sem conclusão —
> isso é esperado e reportado pelo programa.

### Complexidade
`O(n!)` no pior caso (backtracking)

---

### Teste M-1 — Verificação com o grafo original (80 vértices)

**Entrada:**
```
Digite a opção (a-o): m
```

**Saída esperada:**
```
  Número de vértices          : 80
  Fortemente conexo           : Sim ✅
  Condição de Ore (dirigida)  : Não satisfeita
  Condição de Dirac (dirigida): Não satisfeita

  Condições suficientes não satisfeitas.
  Executando backtracking (limitado) para verificação…

  RESULTADO: INCONCLUSIVO (limite de 50000 tentativas atingido)
  O problema Hamiltoniano é NP-completo; grafos grandes
  exigem heurísticas avançadas para verificação exata.
```

---

### Teste M-2 — Verificação após remover vértices (grafo menor)

Remova alguns vértices para criar um grafo menor e tornar o backtracking viável.  
Remova por exemplo o vértice `79`:

**Entrada:**
```
Digite a opção (a-o): e
Vértice a remover: 79
```

Depois rode novamente:

```
Digite a opção (a-o): m
```

**O que observar:** Com menos vértices, o backtracking pode chegar a uma conclusão
dentro do limite de tentativas.

> Após os testes, recarregue o grafo original com a opção `a` para restaurar
> o estado completo.

---

## Opção N — Coloração do Grafo e Bipartição `[Característica 4]`

### O que é?
Realiza duas análises no **grafo subjacente não-direcionado**:

1. **Verificação de bipartição (BFS com 2 cores):** determina se os vértices podem ser
   divididos em 2 grupos sem conexões internas — equivale a não possuir ciclos ímpares.
2. **Coloração gulosa por DFS:** atribui a menor cor possível a cada vértice de forma
   que vizinhos nunca tenham a mesma cor, obtendo um **limitante superior** para o
   número cromático χ(G).

### Complexidade
`O(V + A)`

---

### Teste N-1 — Coloração com o grafo original

**Entrada:**
```
Digite a opção (a-o): n
```

**O que observar na saída:**
- Se o grafo é ou não bipartido.
- Quantas cores foram necessárias pelo algoritmo guloso.
- Distribuição dos vértices por cor.
- Interpretação para o contexto de caronas.

**Trecho esperado:**
```
  Total de vértices    : 80
  Bipartido            : Não ❌
  Cores usadas (guloso): X
  (χ(G) ≤ X — limitante superior pelo algoritmo guloso)

  O grafo subjacente NÃO é bipartido (contém ciclo ímpar).

  Distribuição por cor (coloração gulosa — X cor(es)):
    Cor  0: XX vértice(s)  →  [0, 1, 2, ...]
    Cor  1: XX vértice(s)  →  [3, 4, 5, ...]
    ...
```

---

### Teste N-2 — Coloração após inserir novo vértice isolado

Insira um novo vértice sem conectá-lo:

**Entrada:**
```
Digite a opção (a-o): c
Nome do novo cruzamento: Teste Coloracao
```

Depois rode a coloração:

```
Digite a opção (a-o): n
```

**O que observar:** O novo vértice isolado recebe a cor `0` (menor disponível),
e o número total de vértices passa a ser 81. O número de cores pode ou não mudar.

---

## Resumo Geral dos Testes

| Opção | Função | Testes | Resultado esperado |
|-------|--------|--------|--------------------|
| `j` | Dijkstra | 14→0, 17→0, 0→76 | Caminho com distância em km / sem caminho |
| `k` | Graus | Original, após inserir aresta | Tabela de graus + estatísticas |
| `l` | Euleriano | Original, após remover aresta | Não Euleriano (malha real) |
| `m` | Hamiltoniano | Original, após remover vértice | Inconclusivo (NP-completo) |
| `n` | Coloração | Original, após inserir vértice | Não bipartido + número de cores |

---

## Observações Importantes

- **Sempre carregue o grafo com a opção `a`** antes de qualquer teste.
- Após testes destrutivos (remover vértice/aresta), recarregue com `a` para restaurar.
- **Não salve (`b`)** durante os testes, a menos que queira persistir as alterações.
- O Hamiltoniano com 80 vértices é **intencionalmente inconclusivo** — isso demonstra
  conhecimento sobre a complexidade computacional do problema.
- Tire **ao menos 2 prints de cada opção** para o relatório conforme exigido pelo enunciado.
