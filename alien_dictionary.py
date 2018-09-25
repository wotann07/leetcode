from collections import defaultdict


class Graph:
    def __init__(self, v_num: int):
        """
        Graph to do topological sorting on
        :param v_num: Number of vertices of this graph
        """
        self.adjacency_dict = defaultdict(set)
        self.v_num = v_num

    def add_edge(self, v_source, v_destination):
        self.adjacency_dict[v_source].add(v_destination)
        _ = self.adjacency_dict[v_destination]

    def print_graph(self):
        for u in self.adjacency_dict.keys():
            print(u, ':', ', '.join([v for v in self.adjacency_dict[u]]))

    def _top_sort_util(self, v, visited, alphabet):
        visited[v] = True

        for child_v in self.adjacency_dict[v]:
            if not visited[child_v]:
                self._top_sort_util(child_v, visited, alphabet)

        alphabet.append(v)

    def topology_sort(self):
        visited = defaultdict(bool)
        alphabet = []

        for v in self.adjacency_dict.keys():
            if not visited[v]:
                self._top_sort_util(v, visited, alphabet)

        return alphabet


class AlienDictionary:
    def __init__(self, word_sample: [], k: int):
        """
        :param word_sample: Sorted list of words in Alien language
        :param k: Number of characters in dictionary
        """
        self.word_sample = word_sample
        self.k = k

    def get_alphabet(self):
        """
        Will apply topological sorting to solve this problem
        :return: Returns the ordered, size k alphabet for this language
        """
        dag = Graph(self.k)
        # Building the DAG
        for i in range(len(self.word_sample) - 1):
            for a, b in zip(self.word_sample[i], self.word_sample[i + 1]):
                if a != b:
                    dag.add_edge(a, b)
                    break

        dag.print_graph()
        return dag.topology_sort().reverse()
