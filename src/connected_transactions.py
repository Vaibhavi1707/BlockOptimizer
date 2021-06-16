class ConnectedTransactions:
    def __init__(self, txns):
        self.hierarchy = txns
        self.net_wt = sum(txn.weight for txn in txns)
        self.net_fee = sum(txn.fee for txn in txns)
        self.fee_weight_ratio = self.net_fee / self.net_wt 
        
    def __lt__(self, other):
        return self.fee_weight_ratio > other.fee_weight_ratio