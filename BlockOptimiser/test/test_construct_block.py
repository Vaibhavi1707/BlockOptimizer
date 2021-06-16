import unittest, sys
sys.path.insert(1, ".")
from BlockOptimiser.src.make_block.construct_block import get_partial_txns, find_optimum_block, construct_ordered_optimum_block  
from BlockOptimiser.src.entities.transaction import MempoolTransaction
from BlockOptimiser.src.entities.connected_transactions import ConnectedTransactions

class TestConstructBlock(unittest.TestCase):
    def setUp(self):
        self.txns1 = [MempoolTransaction("1", 300, 100, ["2", "3"]), MempoolTransaction("2", 400, 30, []), MempoolTransaction("3", 500, 20, ["2"])]
        self.txns2 = [MempoolTransaction("1", 300, 200, []), MempoolTransaction("2", 300, 50, [])]
        self.connected_txns1 = [ConnectedTransactions(self.txns1)]
        self.connected_txns2 = []
    
    def test_get_partial_txns(self):
        self.assertEqual(get_partial_txns(100, self.connected_txns1), [MempoolTransaction("1", 300, 100, ["2", "3"])])
        self.assertEqual(get_partial_txns(100, self.connected_txns2), [])
    
    def test_find_optimum_block(self):
        self.assertEqual(find_optimum_block(200, self.txns1), [])
        self.assertNotEqual(find_optimum_block(200, self.txns2), [])
    
    def test_construct_ordered_optimum_block(self):
        self.assertEqual(construct_ordered_optimum_block(300, self.txns1), [])
        self.assertNotEquals(construct_ordered_optimum_block(300, self.txns2), [])
    
if __name__ == '__main__':
    unittest.main()