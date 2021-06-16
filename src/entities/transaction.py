class MempoolTransaction():
    def __init__(self, txid, fee, wt, parents):
        self.txid = txid
        self.fee = int(fee)
        self.wt = int(wt)
        self.parents = parents.split(";") if not parents == "" else []  