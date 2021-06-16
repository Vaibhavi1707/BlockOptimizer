from connected_transactions import ConnectedTransactions

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

def find_optimised_block(max_weight, transactions):
    """ Finds the optimal block with total weight less that 4 million and max fee. """
    opt = [0 for w in range(max_weight + 1)] # Space optimisation for 0 - 1 Knapsack
    for n in range(len(transactions)):
        for w in range(max_weight, transactions[n].weight - 1, -1):
            opt[w] = max(transactions[n].fee + opt[w - transactions[n].weight], 
                         opt[w])
        print(n)
    print(opt[max_weight])
    return backtrack_block(opt, opt[max_weight], max_weight, transactions)

def backtrack_block(opt_array, opt_fee, max_weight, transactions):
    pass
    
def construct_ordered_optimised_block(transactions, max_weight):
    """ Finds an ordered block such that for every transaction, it's parent comes 
    before it and the block maximises the total fees obtained. """
    ordered_transactions = find_parent_hierarchy(transactions)
    ordered_optimised_block = find_optimised_block(max_weight, ordered_transactions)
    return ordered_optimised_block
    
    