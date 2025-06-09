import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt
import ast

# Dados
data = {
    "nome": [
        "Luis Gustavo Dias Frigeri",
        "Marcos Vinicius",
        "Luiz Otávio Vieira Martins Guimarães",
        "Lucas Pereira",
        "Vitor",
        "João Celso da Silva Nogueira dos Santos",
        "Vinicius Oliveira",
        "Jonathan",
        "Portaluppi",
        "Rafael",
        "Luiz Felipe",
        "Karol",
        "Nicolas Augusto Cardoso",
        "Luiz Antônio Marcussi Neto",
        "Kaio Enrique",
        "Kendy H."
    ],
    "bandas": [
        "['phonk', 'rock', 'heavy metal']",
        "['sabaton', 'iron maiden', 'insomnium']",
        "['charlie brown jr', 'jota quest', 'rosa de saron']",
        "['link do zap', 'gp da zl', 'joji']",
        "['menos e mais', 'israel e rodolfo', 'kendrick lamar']",
        "['linking park', 'pink floyd', 'megadeath']",
        "['bringmethehorizon', 'novulent', 'signcrushesmotorist']",
        "['bee gees', 'backstreet boys', 'west life']",
        "['marino', 'the neighbourhood', 'twenty one pilots']",
        "['linkin park', 'system of a down', 'bruno e marrone']",
        "['nirvana', 'gorillaz', 'ac/dc']",
        "['slipknot', 'raimundos', 'charlie brown jr.']",
        "['projeto sola', '5 a seco', 'attos 2']",
        '["guns nroses", "legiao urbana", "beatles"]',
        "['system of down', 'slipknot', 'linkin park']",
        "['iron maiden', 'linkin park', 'imagine dragons']"
    ]
}

# DataFrame e processamento
df = pd.DataFrame(data)
df['bandas'] = df['bandas'].apply(ast.literal_eval)

# Grafo direcionado
G = nx.DiGraph()

for _, row in df.iterrows():
    pessoa = row['nome']
    bandas = row['bandas']  # usa todas as bandas
    G.add_node(pessoa, bipartite=0)
    for banda in bandas:
        G.add_node(banda, bipartite=1)
        G.add_edge(pessoa, banda)  # Direção: pessoa → banda

# Layout manual bipartido com espaçamento
pessoas = [n for n, d in G.nodes(data=True) if d["bipartite"] == 0]
bandas = [n for n, d in G.nodes(data=True) if d["bipartite"] == 1]

espaco = 1.5  # Espaço vertical entre os nós

pos = {}

# Posiciona pessoas na coluna da esquerda
for i, n in enumerate(sorted(pessoas)):
    pos[n] = (0, -i * espaco)

# Posiciona bandas na coluna da direita
for i, n in enumerate(sorted(bandas)):
    pos[n] = (4, -i * espaco)

# Tamanhos dos nós conforme grau
graus = dict(G.degree())
tamanhos = [graus[n] * 300 for n in G.nodes()]

# Plot
plt.figure(figsize=(20, 14))
nx.draw(
    G, pos,
    with_labels=True,
    node_color=['skyblue' if n in pessoas else 'lightgreen' for n in G.nodes()],
    node_size=tamanhos,
    font_size=8,
    edge_color='gray',
    arrows=True,
    arrowsize=20,
    connectionstyle='arc3,rad=0.05'
)
plt.title("Grafo Direcionado: Alunos de BCC → Todas as Bandas Favoritas (com Separação)")
plt.axis('off')
plt.tight_layout()
plt.show()