from entities.connected_transactions import ConnectedTransactions

def visit(transaction, transactions, visited, parent_order):
    """ Visits a transaction and all it's ancestors """
    visited[transaction.txid] = "grey"
    for parent in transaction.parents:
        if parent not in visited:
            transactions.remove(transaction)
        if visited[parent] == "grey":
            raise Exception("Cyclic parents")
        if visited[parent] == "white":
            for transaction_pa in transactions:
                if parent == transaction_pa.txid:
                    parent = transaction_pa 
            visit(parent, transactions, visited, parent_order)
    visited[transaction.txid] = "black"
    parent_order.append(transaction)

def find_parent_hierarchy(transactions):
    """ Sort the transactions such that every transaction comes after its parent. """
    visited = dict(list(zip([transaction.txid for transaction in transactions], ["white" for transaction in transactions])))
    connected_txns = []
    count = 0    
    for transaction in transactions:
        if visited[transaction.txid] == "white":
            parent_order = []
            visit(transaction, transactions, visited, parent_order)
            connected_txns.append(ConnectedTransactions(parent_order))
    return connected_txns

def get_partial_transactions(max_weight, connected_transactions):
    """ Get a part of connected transactions such that the total weight is less than max_weight  """
    transactions = connected_transactions.hierarchy
    partial_transactions = []
    i = 0
    while max_weight >= transactions[i].weight:
        partial_transactions.append(transactions[i])
        i += 1
    return partial_transactions

def find_optimised_block(max_weight, transactions):
    """ Finds the optimal block with total weight less that 4 million and max fee. """
    transactions.sort()
    total_fee = 0
    block = []
    for transaction in transactions:
        curr_wt = int(transaction.net_wt)
        curr_fee = int(transaction.net_fee)
        if max_weight >= curr_wt:
            max_weight -= curr_wt
            total_fee += curr_fee
            block += [txn.txid for txn in transaction.hierarchy]
        else:
            remain_txns = get_partial_transactions(max_weight, transaction)
            total_fee += sum(txn.fee for txn in remain_txns)
            block += [txn.txid for txn in remain_txns]
    return block
    
def construct_ordered_optimised_block(transactions, max_weight):
    """ Finds an ordered block such that for every transaction, it's parent comes 
    before it and the block maximises the total fees obtained. """
    connected_transactions = find_parent_hierarchy(transactions)
    ordered_optimised_block = find_optimised_block(max_weight, connected_transactions)
    return ordered_optimised_block
    
    