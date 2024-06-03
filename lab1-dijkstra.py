
'''
1. Требуется написать скрипт на языке Python с реализацией алгоритма Дейкстры для заданного графа.
Граф задаётся матрицей смежности или списком смежных вершин.
Алгоритм должен находить кратчайшие пути от произвольной начальной вершины до всех остальных.

Для представления графов разрешается использовать сторонние библиотеки,
но не разрешается использовать реализацию алгоритма Дейкстры в составе сторонних библиотек.

Описание алгоритма Дейкстры:
- https://ru.ruwiki.ru/wiki/Алгоритм_Дейкстры
- https://habr.com/ru/companies/otus/articles/748470/
'''

import networkx as nx
import numpy as np
import sys

# Для визуализации графа
# in Linux: apt-get install elementary-icon-theme
import matplotlib.pyplot as plt

# 1. Класс Graph1 и его методы
class Graph1(object):
    def __init__(self, graph0_asDict):
        self.graph = self.CreateGraph1( graph0_asDict )

    # 1.1. Метод создания
    #      экземпляра класса Graph1
    #      .CreateGraph1( init_graph-as-Adjacency-Matrix )

    def CreateGraph1(self, graph0_asDict):
        graph1 = nx.Graph()
        for vertex34, edge34_asDict in graph0_asDict.items():
            ##print("1.1. N_35: ", "vertex34=", vertex34, "; edge34_asDict=", edge34_asDict )
            for vertex36, edgeWeight36 in edge34_asDict.items():
                ##print("1.1. N_37: ", "vertex34=", vertex34, "vertex36=", vertex36, "; edgeWeight36=", edgeWeight36 )
                graph1.add_edge( vertex34, vertex36, weight=edgeWeight36 )
        ##print("1.1. N_39: .graph1=", graph1 )
        return graph1

    # 1.2. Метод удаления вершины из списка-вершин, хранящих кратчайших путей в графе
    #      экземпляре класса Graph1
    #      Применяется для удаления startVertex в самом конце, перед выводом итогового расчёта
    #      .MinPaths_delVertex(vertex47)

    def MinPaths_delVertex(self, vertex47):
        self.MinPaths_asDict.pop(vertex47, None )
        ##print("1.3. N_49: .MinPaths_asDict=", self.MinPaths_asDict )

    # 1.3. Метод запроса списка-вершин, хранящих кратчайших путей в графе
    #      экземпляре класса Graph1
    #      .MinPaths_get(vertex55)

    def MinPaths_get(self, vertex55):
        minpath56_asList = self.MinPaths_asDict[vertex55]
        minpath56_asList = minpath56_asList[:]  # a copy of List
        ##print("1.3. N_58: .MinPaths_get[", vertex55, "]=", minpath56_asList )
        return minpath56_asList

    # 1.4. Метод создания структуры для хранения кратчайших путей в графе
    #      экземпляре класса Graph1
    #      .MinPaths_init(G1)

    def MinPaths_init(self, startVertex):
        # Создаём структуру для хранения кратчайших путей в графе как словарь:
        #     индекс_в_словаре - это номер вершины
        #     значение_в_словаре - это список-вершин - последовательность вершин, хранящая кратчайший путь

        self.MinPaths_asDict = {}  # create an empty dictionary
        for vertex71 in self.graph.nodes:
            self.MinPaths_asDict[vertex71] = [startVertex]  # создаём пару индекс_в_словаре -- список-вершин-пока_что-из-одной_нулевой-вершины
        ##print("1.4. N_73: .MinPaths_asDict=", self.MinPaths_asDict )

    # 1.5. Метод замены массива-вершин, хранящих кратчайших путей в графе
    #      экземпляре класса Graph1
    #      .MinPaths_replace(G1, vertex, minpath_asList)

    def MinPaths_replace(self, vertex79, minpath79_asList):
        # Заменяем в структуре для хранения кратчайших путей в графе
        #     индекс_в_словаре - это номер вершины
        #     значение_в_словаре - это список-вершин - последовательность вершин, хранящая кратчайший путь

        self.MinPaths_asDict[vertex79] = minpath79_asList
        ##print("1.5. N_85: .MinPaths_asDict=", self.MinPaths_asDict )

    # 1.6. Метод создания списка непосещённых вершин
    #      экземпляра класса Graph1
    #      .Vertexes_unvisited_createList(G1)

    def Vertexes_unvisited_createList(self):
        self.unvisitedVertexes_asList = []  # create an empty list
        for vertex93 in self.graph.nodes:
            self.unvisitedVertexes_asList.append(vertex93)
        ##print("1.6. N_95: .unvisitedVertexes_asList=", self.unvisitedVertexes_asList )

    # 1.7. Метод удаления вершины из списка непосещённых вершин
    #      экземпляра класса Graph1
    #      .Vertexes_unvisited_delVertexFromList()

    def Vertexes_unvisited_delVertexFromList(self, vertex92):
        self.unvisitedVertexes_asList.remove(vertex92)
        ##print("1.7. N_103: self.unvisitedVertexes_asList=", self.unvisitedVertexes_asList)

    # 1.8. Метод получения списка непосещённых вершин
    #      экземпляра класса Graph1
    #      .Vertexes_unvisited_getList()

    def Vertexes_unvisited_getList(self):
        return self.unvisitedVertexes_asList

    # 1.9. Метод присвоения указанного значения метки вершине
    #      экземпляра класса Graph1
    #      .Vertex_LabValue_Assing()

    def Vertex_LabValue_Assing(self, vertex116, value116):
        self.LabValues_asDict[vertex116] = value116
        ##print("1.9. N_118: ", "vertex=", vertex116, "; value=", self.LabValues_asDict[vertex116] )

    # 1.10. Метод присвоения всем вершинам
    #       экземпляра класса Graph1
    #       значения меток "бесконечность"
    #       .Vertex_LabValue_Assing_4all_asInfin()

    def Vertex_LabValue_Assing_4all_asInfin(self):
        self.LabValues_asDict = {}  # create an empty dictionary
        for vertex127 in self.graph.nodes:
            self.LabValues_asDict[vertex127] = sys.maxsize
        ##print("1.10. N_129: ", self.LabValues_asDict)

    # 1.11. Метод вывода значений всех вершин и кратчайших-путей, после сортировок
    #       экземпляра класса Graph1
    #       .Vertex_LabValue_output_all( toOutputAsFinal )

    def Vertex_LabValue_output_all( self, toOutputAsFinal ):
        sorted1_asDict = dict(sorted(self.LabValues_asDict.items()))
        self.LabValues_asDict = sorted1_asDict
        sorted2_asDict = dict(sorted(self.MinPaths_asDict.items()))
        self.MinPaths_asDict = sorted2_asDict
        if toOutputAsFinal:
            print("Значения меток вершин графа: ", self.LabValues_asDict )  # 1.10. N_140:
            print("Кратчайшие пути в графе: ", self.MinPaths_asDict )  # 1.10. N_141:


# 2. Решение по алгоритму Дейкстры (рекурсивная реализация)
#    dijkstra_algorithm( G1-as-Graph1, startVertex-as-int )

def dijkstra_algorithm( graph2, startVertex ):
    ##print("2. N_148: startVertex=", startVertex )
    ##print("2. N_149: startVertex=", startVertex, ", ", graph2.Vertexes_unvisited_getList() )
    if startVertex in graph2.Vertexes_unvisited_getList():
        # 2.1. Записываем значения меток вершин vertexU (ближайших к startVertex)

        for vertexU in graph2.graph.neighbors(startVertex):
            ##print("2.1. N_154: startVertex=", startVertex, ", vertexU=", vertexU )
            if vertexU in graph2.Vertexes_unvisited_getList():
                # 2.1.1. vertexU - непосещённая, иожно аналировать глубже

                ##print("2.1.1. N_158: startVertex=", startVertex, ", vertexU=", vertexU )

                # 2.1.2. Вычисляем значение метки вершины vertexU

                weightEdge162_asDict = graph2.graph.get_edge_data(startVertex, vertexU)
                ##print("2.1.2. N_163: startVertex=", startVertex=, ", weightEdge162_asDict=", weightEdge162_asDict )
                weightEdge164_asInt = weightEdge162_asDict['weight']
                ##print("2.1.2. N_165: startVertex=", startVertex, ", weightEdge164_asInt=", weightEdge164_asInt )
                newValueVertexU = graph2.LabValues_asDict[startVertex] + weightEdge164_asInt
                ##print("2.1.2. N_167: startVertex=", startVertex=
                ##      , ", graph2.LabValues_asDict[startVertex]=", graph2.LabValues_asDict[startVertex]
                ##      , ", weightEdge164_asInt=", weightEdge164_asInt
                ##      , ", newValueVertexU=", newValueVertexU
                ##      )

                # 2.1.3. Если newValueVertexU меньше текущего значение метки вершины vertexU
                #        то записываем newValueVertexU в значение метки вершины vertexU

                minpath176_asList = G1.MinPaths_get(vertexU)
                minpath176_Last_asInt = minpath176_asList[-1]
                if newValueVertexU < graph2.LabValues_asDict[vertexU]:
                    ##print("2.1.3. N_179: startVertex=", startVertex, ", vertexU=", vertexU, ", minpath176_asList=", minpath176_asList )
                    graph2.Vertex_LabValue_Assing(vertexU, newValueVertexU )
                    if vertexU != minpath176_Last_asInt:  # в глубине рекурсии бывает, что vertexU == minpath176_Last_asInt, и в списке возникает дублирующийся элемент...
                        minpath176_asList.append(vertexU)
                    G1.MinPaths_replace(vertexU, minpath176_asList)
                ##print("2.1.3. N_184: startVertex=", startVertex
                ##      , ", vertexU=", vertexU
                ##      , ", newValueVertexU=", newValueVertexU
                ##      , ", minpath176_asList=", minpath176_asList
                ##      )
                G1.Vertex_LabValue_output_all( False )  # False означает вывод для протокола/лога
        ## end if for vertexU in graph2.graph.neighbors(startVertex):

        # 2.2. Отмечаем вершину startVertex как посещённую
        #      чтобы при обработке соседей-соседей   обработка пропустила её

        graph2.Vertexes_unvisited_delVertexFromList(startVertex)

        # 2.3. Записываем значения меток вершин verUNbhrs (соседних с vertexU)

        for vertexU in graph2.graph.neighbors(startVertex):
            ##print("2.3. N_200: startVertex=", startVertex, ", vertexU=", vertexU )
            if vertexU in graph2.Vertexes_unvisited_getList():
                # 2.3.1. vertexU - непосещённая, иожно аналировать глубже

                ##print("2.3.1. N_204: startVertex=", startVertex, ", vertexU=", vertexU )

                # 2.3.2. Составляем список вершин verUNbhrs (соседних с vertexU)

                verUNbhrs = []  # create an empty list
                for vertex209 in graph2.graph.neighbors(vertexU):
                    if vertex209 != startVertex:
                        verUNbhrs.append(vertex209)  # вершину startVertex не нужно анализировать, она "не соседняя"
                ##print("2.3.2. N_212: startVertex=", startVertex, ", verUNbhrs=", verUNbhrs )

                # 2.3.3. Вычисляем и записываем значения меток вершины verUNbhrs (in verUNbhrs)

                valueVertexU = graph2.LabValues_asDict[vertexU]
                ##print("2.3.3. N_217: startVertex=", startVertex, ", valueVertexU=", valueVertexU )
                for vertexUNbh in verUNbhrs:
                    ##print("2.3.3. N_219: startVertex=", startVertex, ", vertexUNbh=", vertexUNbh )

                    # 2.3.3.1. Вычисляем значение метки вершины vertexUNbh

                    weightEdge223_asDict = graph2.graph.get_edge_data(vertexU, vertexUNbh)
                    ##print("2.3.3.1. N_224: startVertex=", startVertex, ", weightEdge223_asDict=", weightEdge223_asDict )
                    weightEdg225_asInt = weightEdge223_asDict['weight']
                    ##print("2.3.3.1. N_226: startVertex=", startVertex, ", eightEdg156_asInt=", weightEdg225_asInt )
                    newValueVertexUNbh = valueVertexU + weightEdg225_asInt + graph2.LabValues_asDict[startVertex]
                    ##print("2.3.3.1. N_228: startVertex=", startVertex
                    ##      , ", valueVertexU=", valueVertexU
                    ##      , ", weightEdg225_asInt=", weightEdg225_asInt
                    ##      , ", graph2.LabValues_asDict[startVertex]=", graph2.LabValues_asDict[startVertex]
                    ##      , ", newValueVertexUNbh=", newValueVertexUNbh
                    ##      )

                    # 2.3.3.2. Если newValueVertexUNbh меньше текущего значение метки вершины vertexUNbh
                    #          то записываем newValueVertexUNbh в значение метки вершины vertexUNbh

                    minpath238_asList = G1.MinPaths_get(vertexU)
                    if newValueVertexUNbh < graph2.LabValues_asDict[vertexUNbh]:
                        ##print("2.3.3.2. N_240: startVertex=", startVertex
                        ##      , ", vertexUNbh=", vertexUNbh
                        ##      , ", graph2.LabValues_asDict[vertexUNbh]=", graph2.LabValues_asDict[vertexUNbh]
                        ##      , ", newValueVertexUNbh=", newValueVertexUNbh
                        ##      )
                        ##print("2.3.3.2. N_245: startVertex=", startVertex
                        ##      , ", vertexU=", vertexU
                        ##      , ", minpath238_asList=", minpath238_asList
                        ##      , ", vertexUNbh=", vertexUNbh
                        ##      )
                        graph2.Vertex_LabValue_Assing(vertexUNbh, newValueVertexUNbh )
                        minpath238_asList.append(vertexUNbh)
                        G1.MinPaths_replace( vertexUNbh, minpath238_asList )
                    ##print("2.3.3.2. N_253: startVertex=", startVertex
                    ##      , ", vertexUNbh=", vertexUNbh
                    ##      , ", graph2.LabValues_asDict[vertexUNbh]=", graph2.LabValues_asDict[vertexUNbh]
                    ##      , ", minpath238_asList=", minpath238_asList
                    ##      )
                    G1.Vertex_LabValue_output_all( False )  # False означает вывод для протокола/лога
        ## end of for vertexU in graph2.graph.neighbors(startVertex):

        # 2.4. Рекурсивно обрабатываем атрибуты соседей вершины startVertex, далее по большому графу...

        for vertexU in graph2.graph.neighbors(startVertex):
            ##print("2.4. N_264: Рекурсивно запускаем dijkstra_algorithm( G1, ", vertexU, " )", )
            dijkstra_algorithm( G1, vertexU )

    ## end of if startVertex in graph2.Vertexes_unvisited_getList():


# 3. Создаём граф из Adjacency-Matrix / Матрица-смежности

# 3.1. Тестовый граф из https://ru.ruwiki.ru/wiki/Алгоритм_Дейкстры
#      graph1\graph1-2.ods
'''
graph0_asDict = {
    0: {1:  7, 2:  9, 5: 14},
    1: {3: 15, 2: 10, 0:  7},
    2: {3: 11, 5:  2, 0:  9, 1: 10},
    3: {4:  6, 2: 11, 1: 15},
    4: {5:  9, 3:  6},
    5: {0: 14, 2:  2, 4:  9}
}
'''

# 3.2. Тестовый граф
#      graph2\graph2-2.ods

graph0_asDict = {
    0: {1:  2, 2:  4, 8: 14},
    1: {0:  2, 2: 1},
    2: {0:  4, 1:  1, 3:  8},
    3: {2:  8, 4: 11},
    4: {3: 11, 5:  3, 6:  6, 7:  9},
    5: {4:  3, 6:  5},
    6: {4:  6, 5:  5, 7:  7},
    7: {4:  9, 6:  7, 8: 10},
    8: {0: 14, 7:  10}
}

##print("3.1. N_300: ", "graph0_asDict=", graph0_asDict )

# 3.2. Создаём граф как структуру библиотеки networkx

G1 = Graph1( graph0_asDict )
G1.Vertex_LabValue_Assing_4all_asInfin()  # присвоение всем вершинам графа G1 значения меток почти-бесконечность
G1.Vertexes_unvisited_createList()  # создание списка непосещённых вершин

# 3.2.1. Создаём структуру для хранения кратчайших путей в графе
#        как словарь: индекс_в_словаре - это номер вершины
#                     значение_в_словаре - это список вершин - последовательность вершин, хранящая кратчайший путь

# 3.2.1. Отладочная визуализация с весами рёбер
'''
# Getting positions of nodes
pos315 = nx.circular_layout( G1.graph )  # ,scale=3 ,center="array-like"
##print("3.2.1. N_316: ", "pos315=", pos315 )

# Plotting the graph
nx.draw( G1.graph, pos315, node_size=500, with_labels=True, node_color='y' )

# Getting edge labels
labels322 = nx.get_edge_attributes( G1.graph, 'weight')

# Drawing edge labels
nx.draw_networkx_edge_labels( G1.graph, pos315, edge_labels=labels322, verticalalignment="bottom" )
plt.show()  # show graph visualization constructed, from RAM to screen
'''

# 3.2.2. Отладочная визуализация без весов рёбер
'''
# Визуализация графа
nx.draw( G1.graph, node_size=500, with_labels=True, node_color='y')  # construct graph visualization, in RAM
plt.show()  # show graph visualization constructed, from RAM to screen
'''

# 4. Запускаем решение по алгоритму Дейкстры (рекурсивная реализация)

startVertex0 = 0
G1.MinPaths_init(startVertex0)  # создание структуры для хранения кратчайших путей в графе
G1.Vertex_LabValue_Assing( startVertex0, 0 )
dijkstra_algorithm( G1, startVertex0 )

# 5. Выводим результат решения по алгоритму Дейкстры

G1.MinPaths_delVertex( startVertex0 )
G1.Vertex_LabValue_output_all( True )  # True означает вывод итогового расчёта

