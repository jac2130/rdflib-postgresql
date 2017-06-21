from rdflib import Graph, URIRef
configString = "user=postgres host=postgres_triple password=postgres dbname=predictit"

g = Graph('PostgreSQL', identifier=URIRef("http://example.com/g43"))
g.open(configString, create=True)
result = g.parse("http://www.w3.org/People/Berners-Lee/card")

print("graph has %s statements." % len(g))
# prints graph has 79 statements.

for subj, pred, obj in g:
    if (subj, pred, obj) in g:
        print subj
