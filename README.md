# Projeto-Grafos

# 🚗 Caronas Mackenzie — Otimização de Rotas na Malha Viária de São Paulo

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Teoria dos Grafos](https://img.shields.io/badge/Teoria%20dos%20Grafos-Turma%206G-red)
![Mackenzie](https://img.shields.io/badge/Universidade-Mackenzie-darkred)
![Status](https://img.shields.io/badge/Status-Concluído-green)

</div>

---

## 👥 Integrantes

| Nome | RA |
|------|----|
| Daniela Pereira | 10410906 |
| Eduardo Takashi | 10417877 |
| Ricardo Lins Pires | 10419394 |

**Disciplina:** Teoria dos Grafos — Turma 6G  
**Professor:** Prof. Dr. Ivan Carlos Alcântara de Oliveira  
**Instituição:** Universidade Presbiteriana Mackenzie — Faculdade de Computação e Informática

---

## 📌 Sobre o Projeto

O deslocamento diário de estudantes universitários da **Zona Leste de São Paulo** até o **Mackenzie**, localizado na região central, representa um dos maiores desafios da mobilidade urbana da cidade.

Este projeto propõe a **modelagem matemática da malha viária** da região Centro–Zona Leste como um grafo orientado e ponderado, permitindo:

- Analisar rotas entre cruzamentos reais da cidade
- Encontrar o **caminho de menor distância** para caronas universitárias
- Estudar propriedades estruturais da malha viária com algoritmos clássicos de Teoria dos Grafos

> A proposta não é um aplicativo dinâmico de caronas, mas uma **análise estática da infraestrutura viária**, aplicando técnicas consolidadas da disciplina.

---

## 🗺️ Modelagem do Grafo

| Propriedade | Valor |
|-------------|-------|
| Tipo | 6 — Orientado com peso na aresta |
| Vértices | 80 cruzamentos reais |
| Arestas | 210 conexões viárias |
| Peso das arestas | Distância em km entre cruzamentos |

**Exemplos de vértices:**

| ID | Cruzamento |
|----|------------|
| 0  | Rua Maria Antônia x Rua Itambé *(próximo ao Mackenzie)* |
| 9  | Avenida Radial Leste x Rua Tuiuti |
| 12 | Avenida Aricanduva x Avenida Radial Leste |
| 17 | Avenida Ragueb Chohfi x Avenida Jacu Pêssego |
| 79 | Avenida Radial Leste x Viaduto Alberto Badra |

A região abrange bairros como **Penha, Aricanduva, Itaquera, Sapopemba, Jacu-Pêssego e Mooca**.

---

## 🧮 Algoritmos Implementados

### Parte 1 e 2 — Estrutura Base e Conectividade
| Opção | Funcionalidade |
|-------|----------------|
| `a` | Ler dados do arquivo `grafo.txt` |
| `b` | Gravar dados no arquivo `grafo.txt` |
| `c` | Inserir vértice |
| `d` | Inserir aresta |
| `e` | Remover vértice |
| `f` | Remover aresta |
| `g` | Mostrar conteúdo do grafo |
| `h` | Mostrar lista de adjacência |
| `i` | Conexidade e grafo reduzido (FCONEX) |

### Parte 3 — Solução e Características
| Opção | Funcionalidade | Tipo |
|-------|----------------|------|
| `j` | **Dijkstra** — Caminho mínimo entre cruzamentos | Solução Principal |
| `k` | Análise de graus dos vértices | Característica 1 |
| `l` | Verificação Euleriana | Característica 2 |
| `m` | Verificação Hamiltoniana | Característica 3 |
| `n` | Coloração e bipartição | Característica 4 |
| `o` | Encerrar a aplicação | — |

---

## ⚙️ Como Executar

### Pré-requisito
- **Python 3.x** instalado ([python.org/downloads](https://python.org/downloads))

### Passo a passo

**1. Clone o repositório:**
```bash
git clone https://github.com/EduTakashi/Projeto-Grafos.git
cd Projeto-Grafos
```

**2. Verifique que os arquivos estão na mesma pasta:**
```
📁 Projeto-Grafos/
├── caronas.py
├── grafo.txt
└── README.md
```

**3. Execute o programa:**
```bash
python caronas.py
```
ou no Mac/Linux:
```bash
python3 caronas.py
```

**4. Carregue o grafo:**
```
Digite a opção (a-o): a
✅ Grafo carregado com sucesso! 80 vértices e 210 arestas.
```

---

## 🔍 Exemplos de Uso

### Dijkstra — Caminho mínimo (Opção J)
```
Digite a opção (a-o): j
Vértice de ORIGEM  (número): 79
Vértice de DESTINO (número): 2

ORIGEM  : [79] Cruzamento Avenida Radial Leste x Viaduto Alberto Badra
DESTINO : [ 2] Cruzamento Rua Sergipe x Rua da Consolação

Distância mínima: 10.70 km
Número de cruzamentos no trajeto: 9

Trajeto detalhado:
  [79] Cruzamento Avenida Radial Leste x Viaduto Alberto Badra  ← PARTIDA
  [65] Cruzamento Avenida Radial Leste x Viaduto Pires do Rio   (+1.1 km)
  [ 9] Cruzamento Avenida Radial Leste x Rua Tuiuti             (+0.7 km)
  ...
  [ 2] Cruzamento Rua Sergipe x Rua da Consolação               ← CHEGADA
```

### Análise de Graus (Opção K)
```
Digite a opção (a-o): k

  ID    Grau Saída    Grau Entrada    Grau Total  Cruzamento
  [ 1]           6               6          12   Rua da Consolação x Rua Piauí  ◄ MAIOR GRAU TOTAL
  ...
  Vértice com MAIOR grau de saída : [1] Rua da Consolação x Rua Piauí (saída=6)
```

### Verificação Euleriana (Opção L)
```
Digite a opção (a-o): l

  Vértices com grau_saída = grau_entrada: 80
  RESULTADO: POSSUI CIRCUITO EULERIANO ✅
```

### Coloração (Opção N)
```
Digite a opção (a-o): n

  Total de vértices    : 80
  Bipartido            : Não ❌
  Cores usadas (guloso): 4   (χ(G) ≤ 4)

  Cor 0: 32 vértice(s)  →  [0, 4, 6, 9, 10 … (+27 mais)]
  Cor 1: 29 vértice(s)  →  [1, 5, 7, 8, 11 … (+24 mais)]
  Cor 2: 17 vértice(s)  →  [2, 3, 23, 32, 34 … (+12 mais)]
  Cor 3:  2 vértice(s)  →  [35, 79]
```

---

## 🌱 Objetivos de Desenvolvimento Sustentável (ODS)

<table>
  <tr>
    <td><b>ODS 11</b> — Cidades e Comunidades Sustentáveis</td>
    <td>A modelagem e otimização de rotas contribui para mobilidade urbana mais eficiente, reduzindo congestionamentos e promovendo o uso compartilhado de veículos.</td>
  </tr>
  <tr>
    <td><b>ODS 13</b> — Ação contra a Mudança Global do Clima</td>
    <td>Caronas compartilhadas reduzem o número de veículos em circulação, diminuindo a emissão de gases poluentes.</td>
  </tr>
</table>

---

## 📁 Estrutura do Repositório

```
📁 Projeto-Grafos/
├── caronas.py          # Código-fonte principal
├── grafo.txt           # Dados do grafo (80 vértices, 210 arestas)
├── README.md           # Este arquivo
└── Relatorio/
    └── RelatorioGrafos.pdf   # Relatório completo do projeto
```

---

## 📄 Formato do arquivo `grafo.txt`

```
6                          ← tipo do grafo
80                         ← número de vértices
0 "Nome do cruzamento" 0   ← id "rótulo" peso_vértice
...
210                        ← número de arestas
0 1 0.4                    ← origem destino distância_km
...
```

---

## 🔗 Links

- 📁 **GitHub:** [github.com/EduTakashi/Projeto-Grafos](https://github.com/EduTakashi/Projeto-Grafos)
- 🎥 **Vídeo no YouTube:** [*(Vídeo do projeto*](https://youtu.be/5tUSxaQ9HYk)

---

## 📚 Fundamentação Teórica

| Conceito | Aplicação no Projeto |
|----------|---------------------|
| Grafo orientado e ponderado | Modelagem das vias com sentido e distância |
| Algoritmo de Dijkstra | Encontrar a rota mais curta para caronas |
| Algoritmo FCONEX | Verificar forte conexidade da malha |
| Grau de vértices | Identificar melhores pontos de encontro |
| Verificação Euleriana | Analisar se é possível percorrer todas as vias sem repetir |
| Verificação Hamiltoniana | Analisar rota que passa por todos os cruzamentos |
| Coloração de grafos | Agrupar cruzamentos por categorias de conectividade |

---

<div align="center">
  <sub>Universidade Presbiteriana Mackenzie · Faculdade de Computação e Informática · 2026</sub>
</div>
