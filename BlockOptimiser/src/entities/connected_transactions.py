class ConnectedTransactions:
    def __init__(self, txns):
        self.parent_order = txns
        self.net_wt = sum(txn.wt for txn in txns)
        self.net_fee = sum(txn.fee for txn in txns)
        self.fee_wt_ratio = self.net_fee / self.net_wt 
        
    def __lt__(self, other):
        return self.fee_wt_ratio > other.fee_wt_ratio