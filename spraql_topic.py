import rdflib
import json
import os


class SpraqlTopic:
    def __init__(self, startID, endID, path):
        self.g = rdflib.Graph()
        self.g.parse(path)
        self.startID = startID
        self.endID = endID
        print(path)
    # def covertInt(self, path):
    #     for i in range(0, len(path)):
    #         if path[i] != 'None':
    #             path[i] = int(path[i])

    #     return path

    def DFS(self, stack, path, paths):
        if not stack:
            self.DFS([self.startID] + stack, path + [self.startID], paths)
        else:
            if path != [] and path[-1] == self.endID:
                # paths += [self.covertInt(path)]
                paths += [path]
                return

            sparql_query = f"""
                PREFIX : <http://www.semanticweb.org/thuha/topic-onto/>
                PREFIX owl: <http://www.w3.org/2002/07/owl#>
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX xml: <http://www.w3.org/XML/1998/namespace>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX topics: <http://www.semanticweb.org/thuha/topic-onto#>
                BASE <http://www.semanticweb.org/thuha/topic-onto/>
                SELECT *
                WHERE
                {{
                    ?start topics:topicID "{stack[0]}".
                    ?start topics:link ?topicID.
                }}
            """

            qres = self.g.query(sparql_query)
            for row in qres:
                if row["topicID"].value != 'None':
                    self.DFS([row["topicID"].value] + stack,
                             path + [row["topicID"].value], paths)

    def spraqlTopic(self):
        paths = []
        self.DFS([], [], paths)
        with open(os.getcwd() + '/ontology/json/paths.json', 'w') as json_file:
            json.dump(paths, json_file, indent=2)
        return paths
