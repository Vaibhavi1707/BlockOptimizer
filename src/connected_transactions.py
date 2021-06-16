class ConnectedTransactions:
    def __init__(self, txns):
        self.hierarchy = txns
        self.net_weight = sum(txn.weight for txn in txns)
        self.net_fee = sum(txn.fee for txn in txns) 