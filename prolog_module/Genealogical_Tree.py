import pytholog as prolog


class Genealogical_Tree(object):

    def __init__(self, name: str):
        self.name = name
        self.kb = prolog.KnowledgeBase(name=name)

    def query(self, query: str):
        try:
            return self.kb.query(prolog.Expr(query))
        except Exception as e:
            return "Impossible query"
