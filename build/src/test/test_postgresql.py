import unittest
import os
from nose.exc import SkipTest
from . import graph_case
from . import context_case
from .n3_2_case import testN3Store
from rdflib.graph import Graph

# CONNSTR default is Travis-CI config
configString = os.environ.get(
    'CONNSTR',
    "user=postgresql host=127.0.0.1 dbname=rdflibpostgresql_test")


class PostgreSQLGraphTestCase(graph_case.GraphTestCase):
    store_name = "PostgreSQL"
    storetest = True
    path = configString
    create = True


class PostgreSQLContextTestCase(context_case.ContextTestCase):
    store_name = "PostgreSQL"
    storetest = True
    path = configString
    create = True

    def testLenInMultipleContexts(self):
        raise SkipTest("Known issue with __len__")


class PostgreSQLStoreTests(unittest.TestCase):
    storetest = True
    store_name = "PostgreSQL"
    path = configString
    create = True

    def setUp(self):
        self.graph = Graph(store=self.store_name)
        self.graph.open(self.path, create=self.create)

    def tearDown(self):
        self.graph.destroy(self.path)
        self.graph.close()

    def test_PostgreSQL_testN3_store(self):
        testN3Store('PostgreSQL', configString)

if __name__ == '__main__':
    unittest.main()

# To enable profiling data, use nose's built-in hookup with hotshot:
# nosetests --with-profile --profile-stats-file stats.pf test/test_postgresql
# Also see Tarek Ziade's gprof2dot explorations:
# http://tarekziade.wordpress.com/2008/08/25/visual-profiling-with-nose-and-gprof2dot/
