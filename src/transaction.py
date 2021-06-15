class MempoolTransaction():
    def __init__(self, txid, fee, weight, parents):
        self.txid = txid
        self.fee = int(fee)
        self.weight = float(weight)
        self.parents = parents.split(";") if not parents == "" else []  