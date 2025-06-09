# Importa bibliotecas necessárias
import pandas as pd                 # Para manipulação de dados em formato de tabela (DataFrame)
import networkx as nx               # Para criação e manipulação de grafos
import matplotlib.pyplot as plt     # Para visualização gráfica dos dados
import ast                          # Para converter strings que representam listas em listas reais

# Dados: nomes das pessoas e suas bandas favoritas
data = {
    "nome": [
        "Luis Gustavo Dias Frigeri", "Marcos Vinicius", "Luiz Otávio Vieira Martins Guimarães",
        "Lucas Pereira", "Vitor", "João Celso da Silva Nogueira dos Santos",
        "Vinicius Oliveira", "Jonathan", "Portaluppi", "Rafael", "Luiz Felipe",
        "Karol", "Nicolas Augusto Cardoso", "Luiz Antônio Marcussi Neto",
        "Kaio Enrique", "Kendy H."
    ],
    "bandas": [  # Cada valor é uma string que representa uma lista de bandas
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

# Cria um DataFrame com os dados
df = pd.DataFrame(data)

# Converte as strings que representam listas em listas reais
df['bandas'] = df['bandas'].apply(ast.literal_eval)

# Cria um grafo direcionado
G = nx.DiGraph()

# Adiciona os nós e arestas ao grafo
for _, row in df.iterrows():
    pessoa = row['nome']            # Nome do aluno
    bandas = row['bandas']          # Lista de bandas favoritas
    G.add_node(pessoa, bipartite=0) # Adiciona o nó da pessoa, marcado como conjunto 0 (esquerda)
    for banda in bandas:
        G.add_node(banda, bipartite=1)     # Adiciona o nó da banda, marcado como conjunto 1 (direita)
        G.add_edge(pessoa, banda)          # Cria uma aresta direcionada da pessoa para a banda

# Separa os nós de acordo com o conjunto bipartido
pessoas = [n for n, d in G.nodes(data=True) if d["bipartite"] == 0]
bandas = [n for n, d in G.nodes(data=True) if d["bipartite"] == 1]

# Define o espaçamento vertical entre os nós
espaco = 1.5

# Dicionário de posições para cada nó no layout
pos = {}

# Posiciona as pessoas na coluna da esquerda (x = 0)
for i, n in enumerate(sorted(pessoas)):
    pos[n] = (0, -i * espaco)

# Posiciona as bandas na coluna da direita (x = 4)
for i, n in enumerate(sorted(bandas)):
    pos[n] = (4, -i * espaco)

# Calcula o grau (número de conexões) de cada nó para definir seu tamanho
graus = dict(G.degree())
tamanhos = [graus[n] * 300 for n in G.nodes()]  # Multiplicado por 300 para visualização adequada

# Configurações do gráfico
plt.figure(figsize=(20, 14))  # Define o tamanho da figura
nx.draw(
    G,
    pos,
    with_labels=True,  # Exibe rótulos dos nós
    node_color=['skyblue' if n in pessoas else 'lightgreen' for n in G.nodes()],  # Cor dos nós: azul para pessoas, verde para bandas
    node_size=tamanhos,  # Tamanho proporcional ao grau
    font_size=8,         # Tamanho da fonte
    edge_color='gray',   # Cor das arestas
    arrows=True,         # Usa setas nas arestas (grafo direcionado)
    arrowsize=20,        # Tamanho das setas
    connectionstyle='arc3,rad=0.05'  # Estilo de curva das arestas
)

# Título e exibição final do gráfico
plt.title("Grafo Direcionado: Alunos de BCC → Todas as Bandas Favoritas (com Separação)")
plt.axis('off')  # Remove os eixos
plt.tight_layout()
plt.show()