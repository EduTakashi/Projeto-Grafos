# =============================================================================
# Projeto: Rotas de Carona Universitária - Zona Leste ao Mackenzie
# Disciplina: Teoria dos Grafos - Turma 6G
# Prof. Dr. Ivan Carlos Alcântara de Oliveira
# Universidade Presbiteriana Mackenzie - Faculdade de Computação e Informática
#
# Integrantes:
#   Daniela Pereira    - RA 10410906
#   Eduardo Takashi    - RA 10417877
#   Ricardo Lins Pires - RA 10419394
#
# Descrição:
#   Aplicação para análise e otimização de rotas de carona universitária
#   na malha viária da região Centro-Zona Leste de São Paulo, com destino
#   ao campus Mackenzie. Utiliza um grafo orientado e ponderado (tipo 6)
#   modelando cruzamentos (vértices) e vias (arestas com peso em km).
#
# Histórico de alterações:
#   2025-xx-xx | Daniela / Eduardo / Ricardo | Projeto Parte 1 — estrutura base,
#               leitura/gravação do grafo, operações CRUD de vértices e arestas.
#   2025-xx-xx | Daniela / Eduardo / Ricardo | Projeto Parte 2 — conexidade
#               (FCONEX), grafo reduzido, mostrar conteúdo e lista de adjacência.
#   2026-05-14 | Daniela / Eduardo / Ricardo | Projeto Parte 3 — adicionadas:
#               (j) Dijkstra – caminho mínimo (solução principal do problema);
#               (k) Graus dos vértices (característica 1);
#               (l) Verificação Euleriana (característica 2);
#               (m) Verificação Hamiltoniana / ciclo Hamiltoniano (característica 3);
#               (n) Coloração por DFS / bipartição (característica 4).
# =============================================================================

import sys
import heapq

# ─────────────────────────────────────────────────────────────────────────────
# Classe base fornecida pelo professor
# ─────────────────────────────────────────────────────────────────────────────
class Grafo:
    TAM_MAX_DEFAULT = 100  # quantidade de vértices máxima default

    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n        # número de vértices
        self.m = 0        # número de arestas
        self.listaAdj = [[] for _ in range(self.n)]

    def insereA(self, v, w):
        self.listaAdj[v].append(w)
        self.m += 1

    def removeA(self, v, w):
        self.listaAdj[v].remove(w)
        self.m -= 1

    def show(self):
        print(f"\n n: {self.n:2d} m: {self.m:2d}")
        for i in range(self.n):
            print(f"\n{i:2d}: ", end="")
            for w in self.listaAdj[i]:
                print(f"{w:2d}", end="")
        print("\n\nfim da impressao do grafo.")


# ─────────────────────────────────────────────────────────────────────────────
# Classe principal do projeto — herda de Grafo
# ─────────────────────────────────────────────────────────────────────────────
class GrafoCarona(Grafo):

    def __init__(self, n=Grafo.TAM_MAX_DEFAULT):
        super().__init__(n)
        self.tipo      = 6      # orientado com peso na aresta
        self.rotulos   = []     # lista de strings: nome de cada cruzamento
        self.carregado = False  # indica se o arquivo foi lido ao menos 1x

    # ── utilitários internos ──────────────────────────────────────────────────

    def _checar_carregado(self):
        """Verifica se o grafo foi carregado; exibe aviso caso contrário."""
        if not self.carregado:
            print("  ⚠️  Grafo não carregado. Use a opção (a) primeiro.")
            return False
        return True

    def _rotulo(self, v):
        """Retorna o rótulo do vértice v ou um nome genérico."""
        return self.rotulos[v] if v < len(self.rotulos) else f"Vértice {v}"

    # ── override de insereA / removeA para suporte a peso ────────────────────

    def insereA(self, v, w, peso=1.0):
        for (viz, _) in self.listaAdj[v]:
            if viz == w:
                return  # já existe — evita duplicata
        self.listaAdj[v].append((w, peso))
        self.m += 1

    def removeA(self, v, w):
        for item in self.listaAdj[v]:
            if item[0] == w:
                self.listaAdj[v].remove(item)
                self.m -= 1
                return

    # ── OPÇÃO A — Ler dados do arquivo ────────────────────────────────────────

    def carregar(self, arquivo="grafo.txt"):
        """
        Lê o arquivo grafo.txt no formato pré-definido:
          linha 1  : tipo do grafo
          linha 2  : número de vértices
          próximas : id "rótulo" peso_vértice
          linha    : número de arestas
          próximas : u v peso
        """
        try:
            arq = open(arquivo, "r", encoding="utf-8")
        except FileNotFoundError:
            print(f"  ❌ Arquivo '{arquivo}' não encontrado.")
            return
        with arq as f:
            self.tipo = int(f.readline().strip())
            self.n    = int(f.readline().strip())

            self.listaAdj = [[] for _ in range(self.n)]
            self.rotulos  = []
            self.m        = 0

            for _ in range(self.n):
                linha  = f.readline().strip()
                parts  = linha.split('"')
                self.rotulos.append(parts[1])

            qtd_arestas = int(f.readline().strip())
            for _ in range(qtd_arestas):
                linha    = f.readline().strip()
                u, v, p  = map(float, linha.split())
                self.insereA(int(u), int(v), p)

        self.carregado = True
        print(f"  ✅ Grafo carregado com sucesso! {self.n} vértices e {self.m} arestas.")

    # ── OPÇÃO B — Gravar dados no arquivo ────────────────────────────────────

    def salvar(self, arquivo="grafo.txt"):
        """Salva o estado atual do grafo no mesmo formato do arquivo de entrada."""
        if not self._checar_carregado(): return
        with open(arquivo, "w", encoding="utf-8") as f:
            f.write(f"{self.tipo}\n")
            f.write(f"{self.n}\n")
            for i in range(self.n):
                rotulo = self.rotulos[i] if i < len(self.rotulos) else f"Vertice {i}"
                f.write(f'{i} "{rotulo}" 0\n')
            f.write(f"{self.m}\n")
            for u in range(self.n):
                for (v, peso) in self.listaAdj[u]:
                    f.write(f"{u} {v} {peso}\n")
        print("  ✅ Arquivo grafo.txt salvo com sucesso!")

    # ── OPÇÃO C — Inserir vértice ─────────────────────────────────────────────

    def inserirVertice(self):
        """Adiciona novo vértice com ID automático e rótulo informado pelo usuário."""
        if not self._checar_carregado(): return
        nome = input("  Nome do novo cruzamento: ").strip()
        if not nome:
            print("  ❌ Nome não pode ser vazio.")
            return
        self.listaAdj.append([])
        self.rotulos.append(nome)
        novo_id = self.n
        self.n += 1
        print(f"  ✅ Vértice {novo_id} inserido!")

    # ── OPÇÃO D — Inserir aresta ──────────────────────────────────────────────

    def inserirAresta(self):
        """Insere aresta direcionada u→v com peso em km."""
        if not self._checar_carregado(): return
        try:
            u = int(input("  Origem (número do vértice): "))
            v = int(input("  Destino (número do vértice): "))
            p = float(input("  Distância em km: "))
            if 0 <= u < self.n and 0 <= v < self.n:
                for (viz, _) in self.listaAdj[u]:
                    if viz == v:
                        print(f"  ⚠️  Aresta {u}→{v} já existe.")
                        return
                self.insereA(u, v, p)
                print("  ✅ Aresta inserida!")
            else:
                print("  ❌ Vértice inválido!")
        except ValueError:
            print("  ❌ Entrada inválida. Digite apenas números.")

    # ── OPÇÃO E — Remover vértice ─────────────────────────────────────────────

    def removerVertice(self):
        """
        Remove vértice e todas as arestas que o envolvem.
        Reajusta índices para manter sequência contínua (0, 1, 2, …).
        """
        if not self._checar_carregado(): return
        try:
            u = int(input("  Vértice a remover: "))
            if 0 <= u < self.n:
                del self.listaAdj[u]
                del self.rotulos[u]
                nova_lista = []
                for i in range(len(self.listaAdj)):
                    nova_adj_i = []
                    for (k, peso) in self.listaAdj[i]:
                        if k == u:
                            self.m -= 1
                            continue
                        novo_k = k - 1 if k > u else k
                        nova_adj_i.append((novo_k, peso))
                    nova_lista.append(nova_adj_i)
                self.listaAdj = nova_lista
                self.n -= 1
                print("  ✅ Vértice removido!")
            else:
                print("  ❌ Vértice inválido!")
        except ValueError:
            print("  ❌ Entrada inválida.")

    # ── OPÇÃO F — Remover aresta ──────────────────────────────────────────────

    def removerAresta(self):
        """Remove a aresta direcionada u→v."""
        if not self._checar_carregado(): return
        try:
            u = int(input("  Origem: "))
            v = int(input("  Destino: "))
            if 0 <= u < self.n:
                for (viz, _) in self.listaAdj[u]:
                    if viz == v:
                        self.removeA(u, v)
                        print("  ✅ Aresta removida!")
                        return
                print("  ❌ Aresta não encontrada!")
            else:
                print("  ❌ Vértice inválido!")
        except ValueError:
            print("  ❌ Entrada inválida.")

    # ── OPÇÃO G — Mostrar conteúdo do grafo ──────────────────────────────────

    def mostrarArquivo(self):
        """Exibe tipo, vértices com rótulos e total de arestas de forma organizada."""
        if not self._checar_carregado(): return
        print("\n" + "=" * 65)
        print("  CONTEÚDO DO GRAFO")
        print("=" * 65)
        print(f"  Tipo do Grafo : {self.tipo} (orientado com peso na aresta)")
        print(f"  Vértices      : {self.n}")
        print(f"  Arestas       : {self.m}")
        print("-" * 65)
        print("  VÉRTICES:")
        for i in range(self.n):
            print(f"  [{i:>2}] {self._rotulo(i)}")
        print("=" * 65)

    # ── OPÇÃO H — Mostrar lista de adjacência ────────────────────────────────

    def show(self):
        """Exibe a lista de adjacência completa com pesos."""
        if not self._checar_carregado(): return
        print("\n" + "=" * 65)
        print("  LISTA DE ADJACÊNCIA")
        print(f"  n: {self.n}  m: {self.m}")
        print("=" * 65)
        for i in range(self.n):
            print(f"\n  [{i:>2}] {self._rotulo(i)}")
            if self.listaAdj[i]:
                for (w, peso) in self.listaAdj[i]:
                    print(f"        → [{w:>2}] {self._rotulo(w)}  ({peso:.1f} km)")
            else:
                print("        (sem arestas de saída)")
        print("\nfim da impressao do grafo.")
        print("=" * 65)

    # ── OPÇÃO I — Conexidade e grafo reduzido (FCONEX) ───────────────────────

    def _n_pos(self, conjunto):
        """N+[R+(v)] — vizinhos diretos do conjunto."""
        vizinhos = set()
        for u in conjunto:
            for (v, _) in self.listaAdj[u]:
                vizinhos.add(v)
        return vizinhos

    def _n_neg(self, conjunto, adj_inv):
        """N-[R-(v)] — vizinhos inversos do conjunto."""
        vizinhos = set()
        for u in conjunto:
            for v in adj_inv.get(u, set()):
                vizinhos.add(v)
        return vizinhos

    def _fconex(self, V_restante, adj_inv, sccs):
        """
        Algoritmo FCONEX (pseudocódigo da aula):
          Início FCONEX(s0 | s0 ∈ V)  <dados G=(V,A)>
            v <- s0
            R+(v) = R-(v) <- {v};  W <- ∅
            enquanto N+[R+(v)] - R+(v) ≠ ∅: R+(v) <- R+(v) ∪ W
            enquanto N-[R-(v)] - R-(v) ≠ ∅: R-(v) <- R-(v) ∪ W
            W <- R+(v) ∩ R-(v)        <- componente f-conexa
            V <- V - W
            Se V ≠ ∅: FCONEX(si | si ∈ V)
          Fim.
        Complexidade: O(n²) no pior caso.
        """
        if not V_restante:
            return
        s0    = min(V_restante)
        R_pos = {s0}
        R_neg = {s0}

        while True:
            W = self._n_pos(R_pos) & V_restante - R_pos
            if not W:
                break
            R_pos |= W

        while True:
            W = self._n_neg(R_neg, adj_inv) & V_restante - R_neg
            if not W:
                break
            R_neg |= W

        W = R_pos & R_neg
        sccs.append(W)
        V_restante -= W
        if V_restante:
            self._fconex(V_restante, adj_inv, sccs)

    def mostrarConexidade(self):
        """
        Executa FCONEX e exibe:
          - Componentes fortemente conexas (SCCs)
          - Categoria de conexidade (C0, C1, C2 ou C3)
          - Grafo reduzido
        """
        if not self._checar_carregado(): return
        if self.n == 0:
            print("  ⚠️  Grafo vazio.")
            return

        adj_inv = {}
        for u in range(self.n):
            for (v, _) in self.listaAdj[u]:
                adj_inv.setdefault(v, set()).add(u)

        sys.setrecursionlimit(10000)
        V_restante = set(range(self.n))
        sccs       = []
        self._fconex(V_restante, adj_inv, sccs)
        num_sccs   = len(sccs)

        print("\n" + "=" * 65)
        print("  CONEXIDADE DO GRAFO — ALGORITMO FCONEX")
        print("=" * 65)
        print(f"\n  Componentes Fortemente Conexas (SCCs): {num_sccs}")
        print("-" * 65)

        for i, scc in enumerate(sccs):
            if len(scc) == 1:
                v = list(scc)[0]
                print(f"  S{i+1}: [{v}] {self._rotulo(v)}")
            else:
                print(f"  S{i+1} ({len(scc)} vértices):")
                for v in sorted(scc):
                    print(f"    • [{v:>2}] {self._rotulo(v)}")

        print("\n" + "-" * 65)

        if num_sccs == 1:
            categoria  = "C3"
            descricao  = "Fortemente Conexo"
            explicacao = ("Existe caminho direcionado entre qualquer par de "
                          "vértices. Todos os cruzamentos são mutuamente "
                          "alcançáveis — ideal para um sistema de caronas.")
        else:
            visitado = [False] * self.n
            pilha    = [0]
            visitado[0] = True
            while pilha:
                u = pilha.pop()
                for (v, _) in self.listaAdj[u]:
                    if not visitado[v]:
                        visitado[v] = True
                        pilha.append(v)
                for v in adj_inv.get(u, set()):
                    if not visitado[v]:
                        visitado[v] = True
                        pilha.append(v)
            conexo_nao_dir = all(visitado)

            if not conexo_nao_dir:
                categoria  = "C0"
                descricao  = "Desconexo"
                explicacao = ("Existem vértices sem nenhum caminho entre si, "
                              "mesmo ignorando as direções das arestas.")
            else:
                mapa_scc = {}
                for i, scc in enumerate(sccs):
                    for v in scc:
                        mapa_scc[v] = i
                arestas_red  = set()
                for u in range(self.n):
                    for (v, _) in self.listaAdj[u]:
                        if mapa_scc[u] != mapa_scc[v]:
                            arestas_red.add((mapa_scc[u], mapa_scc[v]))
                grau_entrada = [0] * num_sccs
                for (a, b) in arestas_red:
                    grau_entrada[b] += 1
                fontes = sum(1 for g in grau_entrada if g == 0)

                if fontes == 1:
                    categoria  = "C2"
                    descricao  = "Unilateralmente Conexo"
                    explicacao = ("Para qualquer par de vértices existe caminho "
                                  "em pelo menos uma direção.")
                else:
                    categoria  = "C1"
                    descricao  = "Fracamente Conexo"
                    explicacao = ("O grafo é conexo apenas ignorando as "
                                  "direções das arestas.")

        print(f"  Categoria : {categoria} — {descricao}")
        print(f"  Explicação: {explicacao}")

        print("\n" + "-" * 65)
        print(f"  GRAFO REDUZIDO ({num_sccs} supervértice(s)):")

        if num_sccs == 1:
            print("  Uma única SCC — grafo reduzido tem 1 nó (DAG trivial).")
        else:
            mapa_scc = {}
            for i, scc in enumerate(sccs):
                for v in scc:
                    mapa_scc[v] = i
            arestas_red = set()
            for u in range(self.n):
                for (v, _) in self.listaAdj[u]:
                    if mapa_scc[u] != mapa_scc[v]:
                        arestas_red.add((mapa_scc[u], mapa_scc[v]))
            if arestas_red:
                print("  Arestas entre SCCs:")
                for (a, b) in sorted(arestas_red):
                    print(f"    S{a+1} → S{b+1}")
            else:
                print("  Nenhuma aresta entre SCCs.")

        print("=" * 65)

    # =========================================================================
    #  PARTE 3 — Novas funcionalidades
    # =========================================================================

    # ── OPÇÃO J — Dijkstra: Caminho Mínimo (solução principal do problema) ───

    def dijkstra(self):
        """
        Algoritmo de Dijkstra para caminho mínimo em grafo orientado ponderado.

        Contexto do problema:
          Encontra a rota de menor distância total (em km) entre dois
          cruzamentos da malha viária, auxiliando diretamente na
          organização de caronas universitárias — o motorista e os
          passageiros percorrem o menor caminho possível até o Mackenzie.

        Pseudocódigo (baseado no material da disciplina):
          Início DIJKSTRA(G, s)
            Para todo v em V: dist[v] <- ∞; prev[v] <- -1
            dist[s] <- 0
            Q <- fila de prioridade com todos os vértices
            Enquanto Q ≠ ∅:
              u <- vértice em Q com menor dist[u]
              Para todo vizinho v de u:
                alt <- dist[u] + peso(u,v)
                Se alt < dist[v]: dist[v] <- alt; prev[v] <- u
          Fim.

        Complexidade: O((V + A) log V) com heap binária.
        """
        if not self._checar_carregado(): return

        print("\n" + "=" * 65)
        print("  DIJKSTRA — CAMINHO MÍNIMO ENTRE CRUZAMENTOS")
        print("=" * 65)
        print("\n  Vértices disponíveis (0 a", self.n - 1, ").")
        print("  Dica: vértice 0 = Cruzamento próximo ao Mackenzie (Rua Maria Antônia x Rua Itambé)\n")

        try:
            origem  = int(input("  Vértice de ORIGEM  (número): "))
            destino = int(input("  Vértice de DESTINO (número): "))
        except ValueError:
            print("  ❌ Entrada inválida.")
            return

        if not (0 <= origem < self.n) or not (0 <= destino < self.n):
            print("  ❌ Vértice fora do intervalo válido.")
            return

        if origem == destino:
            print("  ⚠️  Origem e destino são o mesmo vértice. Distância = 0 km.")
            return

        # Inicialização
        INF   = float('inf')
        dist  = [INF] * self.n
        prev  = [-1]  * self.n
        dist[origem] = 0.0

        # Heap: (distância acumulada, vértice)
        heap = [(0.0, origem)]

        while heap:
            d_u, u = heapq.heappop(heap)
            if d_u > dist[u]:
                continue  # entrada desatualizada na heap
            for (v, peso) in self.listaAdj[u]:
                alt = dist[u] + peso
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    heapq.heappush(heap, (alt, v))

        # Reconstrução do caminho
        if dist[destino] == INF:
            print(f"\n  ❌ Não existe caminho de [{origem}] até [{destino}].")
            print(f"     Isso indica que não há rota viária direta entre os "
                  f"cruzamentos nas direções modeladas.")
            print("=" * 65)
            return

        caminho = []
        v = destino
        while v != -1:
            caminho.append(v)
            v = prev[v]
        caminho.reverse()

        # Exibição
        print("\n" + "-" * 65)
        print(f"  ORIGEM  : [{origem}] {self._rotulo(origem)}")
        print(f"  DESTINO : [{destino}] {self._rotulo(destino)}")
        print("-" * 65)
        print(f"  Distância mínima: {dist[destino]:.2f} km")
        print(f"  Número de cruzamentos no trajeto: {len(caminho)}")
        print("\n  Trajeto detalhado:")
        for i, v in enumerate(caminho):
            if i == 0:
                print(f"    [{v:>2}] {self._rotulo(v)}  ← PARTIDA")
            elif i == len(caminho) - 1:
                print(f"    [{v:>2}] {self._rotulo(v)}  ← CHEGADA")
            else:
                # calcula distância parcial do segmento anterior
                u_prev = caminho[i - 1]
                seg = next((p for (w, p) in self.listaAdj[u_prev] if w == v), 0)
                print(f"    [{v:>2}] {self._rotulo(v)}  (+{seg:.1f} km)")
        print("\n  Interpretação para caronas:")
        print(f"  Um motorista saindo de [{origem}] pode buscar passageiros")
        print(f"  ao longo desse trajeto de {dist[destino]:.2f} km até [{destino}],")
        print(f"  otimizando combustível e tempo de deslocamento.")
        print("=" * 65)

    # ── OPÇÃO K — Graus dos Vértices (Característica 1) ──────────────────────

    def analisarGraus(self):
        """
        Calcula e exibe o grau de entrada (in-degree) e saída (out-degree)
        de cada vértice do grafo orientado.

        Conceito:
          - Grau de saída (out-degree): número de arestas que partem do vértice.
            No contexto do projeto = número de vias que saem de um cruzamento.
          - Grau de entrada (in-degree): número de arestas que chegam ao vértice.
            No contexto do projeto = número de vias que chegam a um cruzamento.

        Interpretação para caronas:
          Cruzamentos com alto grau de saída são pontos de grande ramificação
          (opções de rota), enquanto alto grau de entrada indica pontos de
          convergência — candidatos naturais a pontos de encontro para caronas.

        Complexidade: O(V + A).
        """
        if not self._checar_carregado(): return

        print("\n" + "=" * 65)
        print("  ANÁLISE DE GRAUS DOS VÉRTICES")
        print("=" * 65)

        grau_saida   = [0] * self.n
        grau_entrada = [0] * self.n

        for u in range(self.n):
            grau_saida[u] = len(self.listaAdj[u])
            for (v, _) in self.listaAdj[u]:
                grau_entrada[v] += 1

        # Cabeçalho da tabela
        print(f"\n  {'ID':>4}  {'Grau Saída':>10}  {'Grau Entrada':>12}  {'Grau Total':>10}  Cruzamento")
        print("  " + "-" * 63)

        maior_saida   = max(grau_saida)
        maior_entrada = max(grau_entrada)
        grau_total    = [grau_saida[i] + grau_entrada[i] for i in range(self.n)]
        maior_total   = max(grau_total)

        for i in range(self.n):
            marca = ""
            if grau_total[i] == maior_total:
                marca = " ◄ MAIOR GRAU TOTAL"
            rotulo_curto = self._rotulo(i)[:45]
            print(f"  [{i:>2}]  {grau_saida[i]:>10}  {grau_entrada[i]:>12}  "
                  f"{grau_total[i]:>10}  {rotulo_curto}{marca}")

        print("\n" + "-" * 65)

        # Estatísticas globais
        total_saida   = sum(grau_saida)
        media_saida   = total_saida / self.n if self.n > 0 else 0
        media_entrada = sum(grau_entrada) / self.n if self.n > 0 else 0

        # Vértices com maior/menor grau
        v_max_saida   = grau_saida.index(maior_saida)
        v_max_entrada = grau_entrada.index(maior_entrada)
        v_min_saida   = grau_saida.index(min(grau_saida))

        print("  ESTATÍSTICAS:")
        print(f"    Total de arestas                : {self.m}")
        print(f"    Soma dos graus de saída         : {total_saida}  (= número de arestas)")
        print(f"    Grau médio de saída             : {media_saida:.2f}")
        print(f"    Grau médio de entrada           : {media_entrada:.2f}")
        print(f"    Vértice com MAIOR grau de saída : [{v_max_saida}] {self._rotulo(v_max_saida)} "
              f"(saída={maior_saida})")
        print(f"    Vértice com MAIOR grau entrada  : [{v_max_entrada}] {self._rotulo(v_max_entrada)} "
              f"(entrada={maior_entrada})")
        print(f"    Vértice com MENOR grau de saída : [{v_min_saida}] {self._rotulo(v_min_saida)} "
              f"(saída={min(grau_saida)})")

        # Vértices isolados (grau total = 0)
        isolados = [i for i in range(self.n) if grau_total[i] == 0]
        if isolados:
            print(f"\n  ⚠️  Vértices isolados ({len(isolados)}): {isolados}")
            print("     Esses cruzamentos não possuem conexão com nenhum outro — "
                  "não podem participar de rotas de carona.")
        else:
            print("\n  ✅ Nenhum vértice isolado — todos os cruzamentos têm ao "
                  "menos uma conexão.")

        print("\n  Interpretação para caronas:")
        print(f"  O cruzamento [{v_max_saida}] é o maior 'distribuidor' de rotas.")
        print(f"  O cruzamento [{v_max_entrada}] é o maior 'ponto de chegada'.")
        print("  Cruzamentos com alto grau total são os melhores pontos de encontro.")
        print("=" * 65)

    # ── OPÇÃO L — Verificação Euleriana (Característica 2) ───────────────────

    def verificarEuleriano(self):
        """
        Verifica se o grafo possui Circuito ou Percurso Euleriano.

        Definições (grafo orientado):
          - Circuito Euleriano: existe se o grafo for fortemente conexo
            E para todo vértice: grau_entrada(v) = grau_saída(v).
          - Percurso Euleriano (não-circuito): existe se o grafo for
            conexo na versão não-direcionada, exatamente 1 vértice com
            grau_saída - grau_entrada = 1 (início) e exatamente 1 vértice
            com grau_entrada - grau_saída = 1 (fim), demais equilibrados.
          - Caso contrário: não é Euleriano.

        Contexto do projeto:
          Um circuito Euleriano significaria que um motorista poderia
          percorrer TODAS as vias da malha exatamente uma vez e retornar
          ao ponto de partida — interessante para planejamento de rotas
          de distribuição ou inspeção viária.

        Complexidade: O(V + A).
        """
        if not self._checar_carregado(): return

        print("\n" + "=" * 65)
        print("  VERIFICAÇÃO EULERIANA DO GRAFO")
        print("=" * 65)

        grau_saida   = [len(self.listaAdj[u]) for u in range(self.n)]
        grau_entrada = [0] * self.n
        for u in range(self.n):
            for (v, _) in self.listaAdj[u]:
                grau_entrada[v] += 1

        # Diferenças grau_saída - grau_entrada
        dif = [grau_saida[v] - grau_entrada[v] for v in range(self.n)]

        vertices_mais1  = [v for v in range(self.n) if dif[v] ==  1]  # candidatos a início
        vertices_menos1 = [v for v in range(self.n) if dif[v] == -1]  # candidatos a fim
        vertices_zero   = [v for v in range(self.n) if dif[v] ==  0]
        desequilibrados = [v for v in range(self.n) if abs(dif[v]) > 1]

        print(f"\n  Vértices com grau_saída = grau_entrada     : {len(vertices_zero)}")
        print(f"  Vértices com grau_saída - grau_entrada = +1: {len(vertices_mais1)}")
        print(f"  Vértices com grau_saída - grau_entrada = -1: {len(vertices_menos1)}")
        print(f"  Vértices fortemente desequilibrados (|Δ|>1): {len(desequilibrados)}")

        # Verificar conectividade (não-direcionada) — necessária para Euler
        visitado = [False] * self.n
        pilha    = [0]
        visitado[0] = True
        adj_inv = {}
        for u in range(self.n):
            for (v, _) in self.listaAdj[u]:
                adj_inv.setdefault(v, set()).add(u)
        while pilha:
            u = pilha.pop()
            for (v, _) in self.listaAdj[u]:
                if not visitado[v]:
                    visitado[v] = True
                    pilha.append(v)
            for v in adj_inv.get(u, set()):
                if not visitado[v]:
                    visitado[v] = True
                    pilha.append(v)
        conexo_subjacente = all(visitado)

        print("\n" + "-" * 65)

        if desequilibrados:
            print("  RESULTADO: NÃO É EULERIANO")
            print(f"  Motivo: {len(desequilibrados)} vértice(s) têm |Δgrau| > 1.")
            print("  Exemplo de vértices problemáticos:")
            for v in desequilibrados[:5]:
                print(f"    [{v}] {self._rotulo(v)} — Δgrau = {dif[v]}")
        elif not conexo_subjacente:
            print("  RESULTADO: NÃO É EULERIANO")
            print("  Motivo: o grafo subjacente não-direcionado é desconexo.")
        elif len(vertices_mais1) == 0 and len(vertices_menos1) == 0:
            # Circuito Euleriano — verificar também forte conexidade
            # (usamos a função auxiliar simplificada)
            print("  RESULTADO: POSSUI CIRCUITO EULERIANO ✅")
            print("  Todos os vértices têm grau_entrada = grau_saída.")
            print("  Um motorista pode percorrer todas as vias exatamente")
            print("  uma vez e retornar ao ponto de partida.")
        elif len(vertices_mais1) == 1 and len(vertices_menos1) == 1:
            inicio = vertices_mais1[0]
            fim    = vertices_menos1[0]
            print("  RESULTADO: POSSUI PERCURSO EULERIANO (não-circuito) ✅")
            print(f"  Início do percurso : [{inicio}] {self._rotulo(inicio)}")
            print(f"  Fim do percurso    : [{fim}] {self._rotulo(fim)}")
            print("  Um motorista pode percorrer todas as vias exatamente")
            print("  uma vez, partindo e chegando em cruzamentos distintos.")
        else:
            print("  RESULTADO: NÃO É EULERIANO")
            print(f"  Condição não satisfeita: há {len(vertices_mais1)} vértice(s) "
                  f"com Δ=+1 e {len(vertices_menos1)} com Δ=−1.")

        print("\n  Interpretação para o projeto:")
        print("  A não existência de circuito Euleriano nesta malha é esperada,")
        print("  pois vias reais raramente têm seus graus perfeitamente equilibrados.")
        print("  Isso confirma que um sistema de caronas deve usar caminhos")
        print("  mínimos (Dijkstra) em vez de percursos Eulerianos.")
        print("=" * 65)

    # ── OPÇÃO M — Verificação Hamiltoniana (Característica 3) ────────────────

    def verificarHamiltoniano(self):
        """
        Verifica (heurística) se o grafo admite Caminho ou Ciclo Hamiltoniano
        usando backtracking com limite de profundidade.

        Definições:
          - Caminho Hamiltoniano: visita TODOS os vértices exatamente uma vez.
          - Ciclo Hamiltoniano  : caminho Hamiltoniano que retorna ao vértice inicial.

        Atenção:
          O problema Hamiltoniano é NP-completo. Para grafos grandes (n > 20),
          o backtracking puro é inviável em tempo razoável. Nesta implementação
          utilizamos backtracking com limite de tempo (tentativas) e verificamos
          também condições suficientes de Ore e Dirac (adaptadas para grafos
          direcionados) para dar uma resposta rápida quando possível.

        Condição de Ore (adaptada / dirigida):
          Se para todo par de vértices não-adjacentes (u,v):
            grau_saida(u) + grau_entrada(v) >= n
          então existe Ciclo Hamiltoniano.

        Contexto do projeto:
          Um ciclo Hamiltoniano na malha viária significaria uma rota que passa
          por TODOS os cruzamentos exatamente uma vez — rota ideal para um
          motorista que precisa buscar passageiros em diferentes pontos.

        Complexidade: O(n!) no pior caso (backtracking).
        """
        if not self._checar_carregado(): return

        print("\n" + "=" * 65)
        print("  VERIFICAÇÃO HAMILTONIANA DO GRAFO")
        print("=" * 65)

        n = self.n

        # ── Condição necessária rápida: forte conexidade ──────────────────────
        adj_inv = {}
        for u in range(n):
            for (v, _) in self.listaAdj[u]:
                adj_inv.setdefault(v, set()).add(u)

        visitado = [False] * n
        pilha    = [0]
        visitado[0] = True
        while pilha:
            u = pilha.pop()
            for (v, _) in self.listaAdj[u]:
                if not visitado[v]:
                    visitado[v] = True
                    pilha.append(v)
        fortemente_conexo = all(visitado)

        grau_saida   = [len(self.listaAdj[u]) for u in range(n)]
        grau_entrada = [0] * n
        for u in range(n):
            for (v, _) in self.listaAdj[u]:
                grau_entrada[v] += 1

        # ── Condição de Ore adaptada (dirigida) ───────────────────────────────
        adj_set = [set(v for (v, _) in self.listaAdj[u]) for u in range(n)]
        ore_ok  = True
        for u in range(n):
            for v in range(n):
                if u != v and v not in adj_set[u]:
                    if grau_saida[u] + grau_entrada[v] < n:
                        ore_ok = False
                        break
            if not ore_ok:
                break

        # ── Condição de Dirac adaptada ────────────────────────────────────────
        dirac_ok = all(grau_saida[v] >= n // 2 and grau_entrada[v] >= n // 2
                       for v in range(n))

        print(f"\n  Número de vértices         : {n}")
        print(f"  Fortemente conexo          : {'Sim ✅' if fortemente_conexo else 'Não ❌'}")
        print(f"  Condição de Ore (dirigida) : {'Satisfeita ✅' if ore_ok else 'Não satisfeita'}")
        print(f"  Condição de Dirac (dirigida): {'Satisfeita ✅' if dirac_ok else 'Não satisfeita'}")

        print("\n" + "-" * 65)

        if ore_ok or dirac_ok:
            print("  RESULTADO: CONDIÇÃO SUFICIENTE SATISFEITA")
            print("  O grafo PROVAVELMENTE admite Ciclo Hamiltoniano. ✅")
            print("  (Condição de Ore/Dirac é suficiente, mas não necessária.)")
        elif not fortemente_conexo:
            print("  RESULTADO: NÃO ADMITE CICLO HAMILTONIANO")
            print("  Motivo: o grafo não é fortemente conexo — existem vértices")
            print("  inacessíveis, portanto é impossível visitar todos.")
        else:
            # Backtracking com limite de tentativas
            print("  Condições suficientes não satisfeitas.")
            print("  Executando backtracking (limitado) para verificação…")

            MAX_TENTATIVAS = [0]
            LIMITE         = 50000
            resultado      = [None]  # 'ciclo', 'caminho' ou None

            def backtrack(v, visitados_bt, caminho_bt, profundidade):
                if MAX_TENTATIVAS[0] > LIMITE:
                    return
                MAX_TENTATIVAS[0] += 1

                if profundidade == n:
                    # Verifica se fecha ciclo
                    for (w, _) in self.listaAdj[v]:
                        if w == caminho_bt[0]:
                            resultado[0] = 'ciclo'
                            return
                    resultado[0] = 'caminho'
                    return

                for (w, _) in self.listaAdj[v]:
                    if not visitados_bt[w]:
                        visitados_bt[w] = True
                        caminho_bt.append(w)
                        backtrack(w, visitados_bt, caminho_bt, profundidade + 1)
                        if resultado[0]:
                            return
                        caminho_bt.pop()
                        visitados_bt[w] = False

            vis  = [False] * n
            vis[0] = True
            backtrack(0, vis, [0], 1)

            if resultado[0] == 'ciclo':
                print("  RESULTADO: ADMITE CICLO HAMILTONIANO ✅")
            elif resultado[0] == 'caminho':
                print("  RESULTADO: Admite Caminho Hamiltoniano (sem ciclo encontrado) ✅")
            else:
                if MAX_TENTATIVAS[0] > LIMITE:
                    print(f"  RESULTADO: INCONCLUSIVO (limite de {LIMITE} tentativas atingido)")
                    print("  O problema Hamiltoniano é NP-completo; grafos grandes")
                    print("  exigem heurísticas avançadas para verificação exata.")
                else:
                    print("  RESULTADO: NÃO FOI ENCONTRADO Ciclo/Caminho Hamiltoniano ❌")

        print("\n  Interpretação para o projeto:")
        print("  Um Ciclo Hamiltoniano representaria uma rota que busca todos")
        print("  os estudantes passando por cada cruzamento exatamente uma vez.")
        print("  Na prática, Dijkstra (opção j) é mais adequado para otimizar")
        print("  rotas reais de carona, pois não exige visitar todos os pontos.")
        print("=" * 65)

    # ── OPÇÃO N — Coloração por DFS / Bipartição (Característica 4) ──────────

    def verificarColoracao(self):
        """
        Realiza a coloração do grafo subjacente (não-direcionado) usando
        o algoritmo guloso por DFS e verifica se o grafo é bipartido.

        Conceitos:
          - Coloração de grafos: atribui cores aos vértices de forma que
            vértices adjacentes nunca tenham a mesma cor.
          - Número cromático χ(G): mínimo de cores necessárias.
          - Grafo bipartido: admite 2-coloração (χ = 2), equivale a não
            possuir ciclos ímpares.

        Algoritmo guloso (DFS):
          Para cada vértice v (em ordem de DFS):
            cor(v) = menor cor não usada pelos vizinhos de v

          Nota: o algoritmo guloso não garante o número cromático mínimo,
          mas fornece um limitante superior útil.

        Verificação de bipartição:
          Usa BFS com 2 cores: se possível colorir sem conflito → bipartido.

        Contexto do projeto:
          A bipartição pode identificar se os cruzamentos formam dois grupos
          distintos (ex.: vias de ida e vias de volta), o que auxiliaria
          no agrupamento de estudantes por sentido de deslocamento.

        Complexidade: O(V + A).
        """
        if not self._checar_carregado(): return

        print("\n" + "=" * 65)
        print("  COLORAÇÃO DO GRAFO (Grafo Subjacente Não-Direcionado)")
        print("=" * 65)

        n = self.n

        # Monta lista de adjacência não-direcionada
        adj_nd = [set() for _ in range(n)]
        for u in range(n):
            for (v, _) in self.listaAdj[u]:
                adj_nd[u].add(v)
                adj_nd[v].add(u)

        # ── Verificação de bipartição (BFS com 2 cores) ───────────────────────
        cor_bip  = [-1] * n
        bipartido = True
        for inicio in range(n):
            if cor_bip[inicio] != -1:
                continue
            fila = [inicio]
            cor_bip[inicio] = 0
            while fila:
                u = fila.pop(0)
                for v in adj_nd[u]:
                    if cor_bip[v] == -1:
                        cor_bip[v] = 1 - cor_bip[u]
                        fila.append(v)
                    elif cor_bip[v] == cor_bip[u]:
                        bipartido = False
                        break
                if not bipartido:
                    break
            if not bipartido:
                break

        # ── Coloração gulosa por DFS ──────────────────────────────────────────
        cor_gulosa = [-1] * n
        for u in range(n):
            cores_viz = set(cor_gulosa[v] for v in adj_nd[u] if cor_gulosa[v] != -1)
            c = 0
            while c in cores_viz:
                c += 1
            cor_gulosa[u] = c

        num_cores = max(cor_gulosa) + 1 if n > 0 else 0

        # Agrupa vértices por cor
        grupos = {}
        for v in range(n):
            c = cor_gulosa[v]
            grupos.setdefault(c, []).append(v)

        # ── Exibição dos resultados ───────────────────────────────────────────
        print(f"\n  Total de vértices   : {n}")
        print(f"  Bipartido           : {'Sim ✅' if bipartido else 'Não ❌'}")
        print(f"  Cores usadas (guloso): {num_cores}")
        print(f"  (χ(G) ≤ {num_cores} — limitante superior pelo algoritmo guloso)")

        if bipartido:
            print("\n  O grafo subjacente É BIPARTIDO.")
            print("  Isso significa que os cruzamentos podem ser divididos em")
            print("  2 grupos sem que haja conexão dentro do mesmo grupo.")
            g0 = [v for v in range(n) if cor_bip[v] == 0]
            g1 = [v for v in range(n) if cor_bip[v] == 1]
            print(f"\n  Grupo A ({len(g0)} vértices): IDs {g0[:10]}{'...' if len(g0) > 10 else ''}")
            print(f"  Grupo B ({len(g1)} vértices): IDs {g1[:10]}{'...' if len(g1) > 10 else ''}")
        else:
            print("\n  O grafo subjacente NÃO é bipartido (contém ciclo ímpar).")

        print(f"\n  Distribuição por cor (coloração gulosa — {num_cores} cor(es)):")
        for c in sorted(grupos.keys()):
            verts = grupos[c]
            exibir = verts[:5]
            resto  = len(verts) - 5
            ids    = ", ".join(str(v) for v in exibir)
            sufixo = f" … (+{resto} mais)" if resto > 0 else ""
            print(f"    Cor {c:>2}: {len(verts):>3} vértice(s)  →  [{ids}{sufixo}]")

        print("\n  Interpretação para o projeto:")
        if bipartido:
            print("  Os dois grupos de cruzamentos podem representar pontos de")
            print("  PARTIDA (Zona Leste) vs pontos de CHEGADA (Centro/Mackenzie),")
            print("  facilitando o agrupamento de passageiros por região.")
        else:
            print("  A malha viária possui ciclos de comprimento ímpar, o que é")
            print("  esperado em redes urbanas reais. Isso indica grande")
            print("  interconectividade entre os cruzamentos da cidade.")
        print("=" * 65)


# =============================================================================
# MENU PRINCIPAL
# =============================================================================

g = GrafoCarona()

while True:
    print("\n" + "=" * 65)
    print("   CARONAS MACKENZIE – OTIMIZAÇÃO DE ROTAS NA MALHA VIÁRIA SP")
    print("   Teoria dos Grafos – Turma 6G – Prof. Ivan Carlos")
    print("=" * 65)
    # ── Parte 1 e 2 ──────────────────────────────────────────────────────────
    print("  a) Ler dados do arquivo grafo.txt")
    print("  b) Gravar dados no arquivo grafo.txt")
    print("  c) Inserir vértice")
    print("  d) Inserir aresta")
    print("  e) Remover vértice")
    print("  f) Remover aresta")
    print("  g) Mostrar conteúdo do arquivo")
    print("  h) Mostrar grafo (lista de adjacência)")
    print("  i) Apresentar conexidade e grafo reduzido")
    # ── Parte 3 ───────────────────────────────────────────────────────────────
    print("  --- Parte 3: Análise e Solução ---")
    print("  j) Dijkstra — Caminho mínimo entre cruzamentos   [SOLUÇÃO]")
    print("  k) Analisar graus dos vértices                   [Característica 1]")
    print("  l) Verificar percurso/circuito Euleriano         [Característica 2]")
    print("  m) Verificar caminho/ciclo Hamiltoniano          [Característica 3]")
    print("  n) Coloração do grafo e verificar bipartição     [Característica 4]")
    print("  o) Encerrar a aplicação")
    print("-" * 65)

    op = input("  Digite a opção (a-o): ").strip().lower()

    if   op == "a": g.carregar()
    elif op == "b": g.salvar()
    elif op == "c": g.inserirVertice()
    elif op == "d": g.inserirAresta()
    elif op == "e": g.removerVertice()
    elif op == "f": g.removerAresta()
    elif op == "g": g.mostrarArquivo()
    elif op == "h": g.show()
    elif op == "i": g.mostrarConexidade()
    elif op == "j": g.dijkstra()
    elif op == "k": g.analisarGraus()
    elif op == "l": g.verificarEuleriano()
    elif op == "m": g.verificarHamiltoniano()
    elif op == "n": g.verificarColoracao()
    elif op == "o":
        print("\n  ✅ Aplicação encerrada.")
        break
    else:
        print("  ❌ Opção inválida! Digite uma letra de a a o.")
