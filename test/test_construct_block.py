import unittest, sys
sys.path.insert(1, ".")
from src.construct_block import find_parent_hierarchy, find_optimised_block
from test_utility import follows_topo_order   
from src.transaction import MempoolTransaction

class TestConstructBlock(unittest.TestCase):
    def setUp(self):
        self.adj_list1 = [MempoolTransaction("0", 200, 1000, "1;2"), MempoolTransaction("1", 300, 400, ""), MempoolTransaction("2", 400, 500, "")]
        self.adj_list2 = [MempoolTransaction("0", 200, 100, "1"), MempoolTransaction("1", 300, 700, "0")]
        self.transaction_list = []
    
    def test_find_parent_hierarchy(self):
        self.assertTrue(follows_topo_order(find_parent_hierarchy(self.adj_list1), self.adj_list1)) 
        with self.assertRaises(Exception):
            find_parent_hierarchy(self.adj_list2)
        
    def test_find_optimized_block(self):
        self.assertTrue(len(find_optimised_block(400, self.transaction_list)) == 0)

if __name__ == '__main__':
    unittest.main()