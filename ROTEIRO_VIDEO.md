# Roteiro do Vídeo — Projeto Teoria dos Grafos
## Caronas Mackenzie — Otimização de Rotas na Malha Viária SP
**Tempo máximo:** 5 minutos  
**Integrantes:** Daniela Pereira · Eduardo Takashi · Ricardo Lins Pires

---

## ⏱️ Distribuição do Tempo

| Parte | Conteúdo | Tempo sugerido |
|-------|----------|----------------|
| 1 | Apresentação do título, integrantes, instituição | 0:00 – 0:40 |
| 2 | Definição do problema real | 0:40 – 1:20 |
| 3 | Teoria dos Grafos + ODS | 1:20 – 2:20 |
| 4 | Execução da aplicação | 2:20 – 4:20 |
| 5 | GitHub | 4:20 – 5:00 |

---

## 🎬 PARTE 1 — Apresentação (0:00 a 0:40)

### O que mostrar na tela:
> Slide simples ou a tela do programa já aberto com o menu à mostra.

### Fala:
> *"Olá! Somos Daniela Pereira, Eduardo Takashi e Ricardo Lins Pires,
> estudantes do curso de Ciência da Computação da Universidade Presbiteriana Mackenzie,
> da Faculdade de Computação e Informática.*
>
> *Este é o projeto da disciplina de Teoria dos Grafos, ministrada pelo
> Professor Doutor Ivan Carlos Alcântara de Oliveira, Turma 6G.*
>
> *O título do nosso projeto é: **Caronas Mackenzie — Otimização de Rotas
> na Malha Viária de São Paulo**."*

---

## 🎬 PARTE 2 — Definição do Problema (0:40 a 1:20)

### O que mostrar na tela:
> Pode mostrar o mapa do grafo do relatório (imagem do Graph Online)
> ou simplesmente continuar com o terminal aberto.

### Fala:
> *"O problema que motivou este projeto é muito presente no dia a dia dos
> estudantes universitários de São Paulo.*
>
> *Alunos que moram na Zona Leste da cidade precisam percorrer longos
> trajetos até o Mackenzie, localizado na região central.
> Esses deslocamentos envolvem congestionamentos intensos, altos custos
> de transporte e muito tempo perdido.*
>
> *Nossa proposta é a modelagem matemática da malha viária da região
> Centro–Zona Leste como um grafo, permitindo analisar rotas e
> viabilizar o compartilhamento de caronas universitárias.*
>
> *Ou seja: o objetivo é encontrar a rota mais curta para que um
> motorista busque passageiros ao longo do caminho e chegue ao
> Mackenzie com o menor deslocamento possível."*

---

## 🎬 PARTE 3 — Teoria dos Grafos + ODS (1:20 a 2:20)

### O que mostrar na tela:
> Mostrar a imagem do grafo no relatório, ou o menu do programa.

### Fala:
> *"Para modelar esse problema, utilizamos um **grafo orientado e
> ponderado**, classificado como Tipo 6.*
>
> *Cada **vértice** representa um cruzamento real da malha viária —
> ao todo são 80 vértices, como o Cruzamento da Avenida Radial Leste
> com a Avenida Aricanduva, ou o Cruzamento da Rua Maria Antônia
> com a Rua Itambé, que é o ponto mais próximo ao Mackenzie.*
>
> *Cada **aresta** representa uma via de conexão entre dois cruzamentos,
> com direção — respeitando o sentido único das ruas — e peso,
> que é a distância em quilômetros entre os pontos.
> São 210 arestas no total.*
>
> *Com essa modelagem, aplicamos algoritmos clássicos de Teoria dos Grafos:
> Dijkstra para encontrar o caminho mínimo, análise de graus, verificação
> Euleriana, verificação Hamiltoniana e coloração do grafo.*
>
> *O projeto se alinha a dois Objetivos de Desenvolvimento Sustentável:
> o **ODS 11**, que busca cidades mais sustentáveis e mobilidade urbana eficiente,
> e o **ODS 13**, que trata da redução de emissões — pois menos carros
> circulando significa menos poluição."*

---

## 🎬 PARTE 4 — Execução da Aplicação (2:20 a 4:20)

### ⚠️ Antes de gravar, deixe o terminal pronto:
1. Abra o terminal
2. Navegue até a pasta com `cd caminho/da/pasta`
3. Execute `python caronas.py` ou `python3 caronas.py`
4. Deixe o menu aparecendo na tela

### Fala + ações na tela (execute junto com a fala):

---

**→ Carregar o grafo:**
> *"Vamos executar a aplicação. Primeiro, carregamos os dados
> do arquivo grafo.txt com a opção A."*

**[ Digite: a ]** → Mostrar: `✅ Grafo carregado com sucesso! 80 vértices e 210 arestas.`

---

**→ Dijkstra (opção J):**
> *"Agora vamos usar o algoritmo de Dijkstra, que é a solução principal
> do projeto. Ele encontra o caminho de menor distância entre
> dois cruzamentos. Vou informar como origem o vértice 79,
> que fica na Zona Leste, e como destino o vértice 2,
> próximo ao Mackenzie."*

**[ Digite: j ]**
**[ Digite origem: 79 ]**
**[ Digite destino: 2 ]**

> *"Veja que o algoritmo encontrou a rota de menor distância,
> com o trajeto detalhado cruzamento a cruzamento e a distância
> total em quilômetros. Isso permite que um motorista saiba
> exatamente qual caminho seguir para buscar passageiros."*

---

**→ Graus dos Vértices (opção K):**
> *"A opção K analisa os graus de entrada e saída de cada cruzamento.
> Cruzamentos com alto grau são os melhores pontos de encontro para caronas."*

**[ Digite: k ]**

> *"Veja que o vértice 1 — Cruzamento Rua da Consolação x Rua Piauí —
> tem o maior grau total: ele é tanto um grande distribuidor
> de rotas quanto um ponto de chegada."*

---

**→ Verificação Euleriana (opção L):**
> *"A opção L verifica se o grafo tem um circuito Euleriano,
> ou seja, se é possível percorrer todas as vias exatamente
> uma vez e voltar ao ponto de partida."*

**[ Digite: l ]**

> *"Com o grafo original, o resultado mostra que o grafo possui
> circuito Euleriano — todos os vértices têm grau de entrada
> igual ao grau de saída. Porém, ao adicionar vértices isolados,
> o grafo fica desconexo e perde essa propriedade."*

---

**→ Verificação Hamiltoniana (opção M):**
> *"A opção M verifica o ciclo Hamiltoniano — uma rota que
> passaria por todos os cruzamentos exatamente uma vez.
> Como esse é um problema NP-completo, para 80 vértices
> o resultado é inconclusivo dentro do limite computacional,
> o que demonstra a importância do Dijkstra para o nosso problema real."*

**[ Digite: m ]**

---

**→ Coloração (opção N):**
> *"Por fim, a opção N realiza a coloração do grafo.
> O resultado mostra que são necessárias 4 cores para colorir
> todos os cruzamentos sem que dois vizinhos tenham a mesma cor,
> e que o grafo não é bipartido — o que é esperado
> em uma malha viária real com ciclos de comprimento ímpar."*

**[ Digite: n ]**

---

## 🎬 PARTE 5 — GitHub (4:20 a 5:00)

### O que mostrar na tela:
> Abra o navegador e acesse o GitHub do projeto:
> `https://github.com/EduTakashi/Projeto-Grafos.git`

### Fala:
> *"Todo o projeto está disponível publicamente no GitHub,
> incluindo o código-fonte comentado, o arquivo grafo.txt
> com os dados da malha viária, e o relatório completo.*
>
> *O link é: github.com/EduTakashi/Projeto-Grafos*
>
> *Obrigado!"*

---

## 📋 Checklist Antes de Gravar

- [ ] Python instalado e funcionando
- [ ] Arquivos `caronas.py` e `grafo.txt` na mesma pasta
- [ ] Terminal aberto na pasta correta
- [ ] Programa testado antes de gravar (rode uma vez para garantir)
- [ ] GitHub atualizado com código + relatório + grafo.txt
- [ ] Microfone funcionando
- [ ] Gravador de tela ativo (OBS, Loom, ou gravador nativo do Windows/Mac)

---

## 🖥️ Como Gravar a Tela

**Windows:**
- Pressione `Win + G` para abrir o Xbox Game Bar e gravar
- Ou use `Win + Alt + R` para iniciar gravação direto

**Mac:**
- Pressione `Cmd + Shift + 5` e escolha "Gravar tela inteira"

**Ferramenta gratuita (qualquer sistema):**
- Acesse **loom.com** — grava tela + câmera ao mesmo tempo, fácil de compartilhar

---

## ✅ Dicas Finais

- Fale de forma clara e no ritmo normal — não precisa correr
- Deixe cada tela visível por 2-3 segundos antes de continuar falando
- Se errar uma parte, pause, respire, e continue — pode editar depois
- O vídeo deve ser publicado no **YouTube de forma pública**
- Não precisa aparecer o rosto — só a tela e a voz já é suficiente
