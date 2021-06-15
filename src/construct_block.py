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
    parent_order.insert(0, transaction)

def find_parent_hierarchy(transactions):
    """ Sort the transactions such that every transaction comes after its parent. """
    visited = dict(list(zip([transaction.txid for transaction in transactions], ["white" for transaction in transactions])))
    parent_order = []
    
    for transaction in transactions:
        if visited[transaction.txid] == "white":
            visit(transaction, transactions, visited, parent_order)
    return parent_order

def find_optimised_block(max_weight, transactions):
    K = [[0 for w in range(max_weight + 1)]
            for i in range(len(transactions) + 1)]
    for i in range(len(transactions) + 1):
        for w in range(max_weight + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif transactions[i - 1].weight <= w:
                K[i][w] = max(transactions[i - 1].fee
                  + K[i - 1][int(w - transactions[i - 1].weight)],
                               K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    res = K[len(transactions)][max_weight]
    block = []
    w = int(max_weight)
    for i in range(len(transactions), 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][w]:
            continue
        else:
            block.append(transactions[i - 1].txid)
            res = res - transactions[i - 1].fee
            w = int(w - transactions[i - 1].weight)
    return block
    
def construct_ordered_optimised_block(transactions, max_weight):
    """ Finds an ordered block such that for every transaction, it's parent comes 
    before it and the block maximises the total fees obtained. """
    ordered_transactions = find_parent_hierarchy(transactions)
    ordered_optimised_block = find_optimised_block(max_weight, ordered_transactions)
    return ordered_optimised_block
    
    