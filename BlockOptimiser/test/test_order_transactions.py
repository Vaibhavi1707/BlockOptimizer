import unittest, sys
sys.path.insert(1, ".")
from BlockOptimiser.src.make_block.order_transactions import find_txn_by_id, visit_self_and_ancestors, find_parent_order  
from BlockOptimiser.src.entities.transaction import MempoolTransaction
from BlockOptimiser.src.entities.connected_transactions import ConnectedTransactions

class TestConstructBlock(unittest.TestCase):
    def setUp(self):
        self.txns1 = [MempoolTransaction("1", 300, 100, ["2", "3"]), MempoolTransaction("2", 400, 30, []), MempoolTransaction("3", 500, 20, ["2"])]
        self.txns2 = [MempoolTransaction("1", 300, 200, ["2"]), MempoolTransaction("2", 300, 50, ["1"])]
    
    
    def test_find_txn_by_id(self):
        self.assertEqual(find_txn_by_id("1", self.txns1), MempoolTransaction("1", 300, 100, ["2", "3"]))
        
        with self.assertRaises(Exception("Transaction not found.")):
            find_txn_by_id("5", self.connected_txns2)
    
    
    def test_visit_self_and_ancestors(self):
        self.assertEqual(visit_self_and_ancestors(MempoolTransaction("1", 300, 100, ["2", "3"]), self.txns1, {"1": "white", "2": "white", "3": "white"}), [])
        
        with self.assertRaises(Exception("A transaction cannot be a descendent and a parent of another transaction.")):
            visit_self_and_ancestors(MempoolTransaction("1", 300, 100, ["2"]), self.txns2, {"1": "white", "2": "white"})
    
            
    def test_find_parent_order(self):
        self.assertEqual(find_parent_order(self.txns1), ["2", "3", "1"])
 
 
   
if __name__ == '__main__':
    unittest.main()