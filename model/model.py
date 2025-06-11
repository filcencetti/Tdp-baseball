import copy
import itertools

import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._idMap = {}

    def getYears(self):
        return DAO.getYears()

    def getTeams(self, year):
        self._teams = DAO.getTeams(int(year))
        for team in self._teams:
            self._idMap[team.ID] = team

    def buildGraph(self,year):
        self._graph = nx.Graph()

        self._graph.add_nodes_from(self._teams)
        print(self._graph.number_of_nodes())

        # Aggiungo un arco per ogni combinazione di nodi
        myedges = list(itertools.combinations(self.list_with_nodes, 2)) # restituisce una lista di tuple con tutte le combinazioni dei nodi
        self._grafo.add_edges_from(myedges)

        allEdges = DAO.getEdges(int(year))
        for edge in allEdges:
            self._graph.add_edge(self._idMap[edge[0]], self._idMap[edge[1]], weight=edge[2])
        print(self._graph.number_of_edges())

    def getNeighbors(self, source):
        result = {}
        for node in self._graph.neighbors(source):
            result[node] = self._graph[source][node]["weight"]
        res = sorted(result.items(), key=lambda item: item[1],reverse=True)
        return res

    def getPath(self,team):
        self._bestPath = []
        self._bestScore = 0

        parziale = [team]

        for v in self._graph.neighbors(team):
            parziale.append(v)
            self.recursion(parziale)
            parziale.pop()

    def recursion(self, parziale):
        if self.getScore(parziale) > self._bestScore:
            self._bestScore = self.getScore(parziale)
            self._bestPath = copy.deepcopy(parziale)

        for v in self._graph.neighbors(parziale[-1]):  # == self._graph.successors()
            if (v not in parziale and  # check if not in parziale
                    self._graph[parziale[-2]][parziale[-1]]["weight"] > self._graph[parziale[-1]][v][
                        "weight"]):  # check if peso nuovo arco è minore del precedente
                parziale.append(v)
                self.recursion(parziale)
                parziale.pop()

    def getScore(self, path):
        tot = 0
        for i in range(len(path) - 1):
            tot += self._graph[path[i]][path[i + 1]]["weight"]

        return tot