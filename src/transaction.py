class MempoolTransaction():
    def __init__(self, txid, fee, weight, parents):
        self.txid = txid
        self.fee = int(fee)
        self.weight = float(float(weight) / 10000)
        self.parents = parents.split(";") if not parents == "" else []  