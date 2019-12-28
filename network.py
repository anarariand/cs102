from api import *
import numpy as np
from igraph import Graph, plot
import numpy as np
import igraph

def get_network(users_ids, as_edgelist=True):
    #в виде списка ребер (as_edgelist=True)
      """ Building a friend graph for an arbitrary list of users """
    vertices = ['me'] # Создание вершин и ребер
    edges = []
    ids = []
    cipher = {}
    for user_id in users_ids['response']['items']:
        name = user_id['first_name'] + user_id['last_name']
        user_id = user_id['id']
        ids.append(user_id)
        cipher.update({user_id : len(cipher.keys()) + 1})
        vertices.append(name)
    for user_id in users_ids['response']['items']:
        user_id = user_id['id']
        edges.append((0, cipher[user_id]))
        friends = get_friends(user_id, 'sex')
        try:
            for friend in friends['response']['items']:
                lable = friend['id']


                if lable in ids:

                    edges.append((cipher[user_id], cipher[lable]))

        except:
            pass
    if as_edgelist:
        print(edges)
    else:
        n = max(max(i, j) for i, j in edges)
        matrix = np.zeros((n, n))
        for i, j in edges:
            matrix[i-1][j-1] = 1
        for row in matrix:
            print(row)
    g = Graph(vertex_attrs={"label":vertices}, # Создание графа
            edges=edges, directed=False)
    N = len(vertices) #Задаем стиль отображения графа
    visual_style = {}
    visual_style["layout"] = g.layout_fruchterman_reingold(
    maxiter=1000,
    area=N**3,
    repulserad=N**3)
    g.simplify(multiple=True, loops=True) #удаляем из графа петли и повторяющиеся ребра
    plot_graph(g, visual_style) # Отрисовываем граф

def plot_graph(g, visual_style):
    communities = g.community_edge_betweenness(directed=False)
    clusters = communities.as_clustering()
    print(clusters)
    pal = igraph.drawing.colors.ClusterColoringPalette(len(clusters))
    g.vs['color'] = pal.get_many(clusters.membership)
    plot(g, **visual_style)


if __name__ == '__main__':
    get_network(get_friends(user_id, 'sex'), True)