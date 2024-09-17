import networkx as nx

class FamilyTree:
    def __init__(self):
        self.graph = nx.Graph()

    def add_member(self, fullname):
        self.graph.add_node(fullname)

    def add_relationship(self, member1, member2, relation):
            self.graph.add_edge(member1, member2, relationship=relation)
  
    def get_closest_relationship_degree(self, member1, member2):
        try:
            path_length = nx.shortest_path_length(self.graph, source=member1, target=member2)
            return path_length
        except nx.NetworkXNoPath:
            return None

    def __repr__(self):
        return f"FamilyTree with {len(self.graph.nodes)} members and {len(self.graph.edges)} relationships"


class Member:
    CHILD = 'CHILD'
    SPOUSE = 'SPOUSE'
    SIBLING = 'SIBLING'
    
    def __init__(self, fullname, family_tree):
        self.fullname = fullname
        self.family_tree = family_tree
        self.family_tree.add_member(fullname)

    def relationship_with(self, member, relation):
        self.family_tree.add_relationship(self.fullname, member.fullname, relation)
    
    def get_closest_relationship_degree(self, member):
        if(self.fullname == member.fullname):
            return 1
        else:
            return self.family_tree.get_closest_relationship_degree(self.fullname, member.fullname)

    def __repr__(self):
        return f"Member(fullname='{self.fullname}')"

#Testing the above class
if __name__ == "__main__":
    family_tree = FamilyTree()

    jenny = Member(fullname="Jenny Doe",family_tree=family_tree)
    jimmy = Member(fullname="Jimmy Doe",family_tree=family_tree)
    john = Member(fullname="John Doe",family_tree=family_tree)
    jane = Member(fullname="Jane Doe",family_tree=family_tree)
    james = Member(fullname="James Doe",family_tree=family_tree)
    jezza = Member(fullname="Jezza Doe",family_tree=family_tree)
    jason = Member(fullname="Jaosn Doe",family_tree=family_tree)

    jimmy.relationship_with(member=jenny, relation=Member.CHILD)
    jezza.relationship_with(member=jimmy, relation=Member.CHILD)
    john.relationship_with(member=jenny, relation=Member.CHILD)
    jane.relationship_with(member=john, relation=Member.SPOUSE)
    james.relationship_with(member=jane, relation=Member.SIBLING)
    jason.relationship_with(member=james, relation=Member.CHILD)
    jezza.relationship_with(member=jason, relation=Member.SPOUSE)

    degree = james.get_closest_relationship_degree(jenny)
    print(f"The degree of relationship between James Doe and Jenny Doe is: {degree}")
    degree = john.get_closest_relationship_degree(james)
    print(f"The degree of relationship between John Doe and James Doe is: {degree}")
    degree = jenny.get_closest_relationship_degree(jane)
    print(f"The degree of relationship between Jenny Doe and Jane Doe is: {degree}")
    degree = jason.get_closest_relationship_degree(jason)
    print(f"The degree of relationship between Jason Doe and Jason Doe is: {degree}")

