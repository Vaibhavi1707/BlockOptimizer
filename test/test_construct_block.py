import unittest, sys
sys.path.insert(1, ".")
from src.construct_block import find_parent_hierarchy, find_optimised_block
from src.utility import follows_topo_order   

class TestConstructBlock(unittest.TestCase):
    def setUp(self):
        self.adj_list1 = {"0": ["1", "2"], "1": ["3"], "2": ["3"], "3": []}
        self.adj_list2 = {"0": ["1"], "1": ["0"]}
        self.transaction_list = []
    
    def test_find_parent_hierarchy(self):
        self.assertTrue(follows_topo_order(find_parent_hierarchy(self.adj_list1), self.adj_list1)) 
        self.assertFalse(follows_topo_order(find_parent_hierarchy(self.adj_list2), self.adj_list2))
        
    def test_find_optimized_block(self):
        pass

if __name__ == '__main__':
    unittest.main()