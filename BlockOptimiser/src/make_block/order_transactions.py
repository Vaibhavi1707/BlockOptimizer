from entities.connected_transactions import ConnectedTransactions


def find_txn_by_id(id_to_find, txns):
    """ Finds a transaction by id """
    for txn in txns:
        if id_to_find == txn.txid:
            return txn

    raise Exception("Transaction not found.") 



def visit_self_and_ancestors(txn, txns, visited, parent_order):
    """ Visits a transaction and all it's ancestors and finds parent to child ordering of a connected component """
    visited[txn.txid] = "grey"
    
    for parent in txn.parents:
        if visited[parent] == "grey":
            raise Exception("A transaction cannot be a descendent and a parent of another transaction.")
        
        if visited[parent] == "white":
            visit_self_and_ancestors(find_txn_by_id(parent, txns), txns, visited, parent_order)
    
    visited[txn.txid] = "black"
    
    parent_order.append(txn)
    
    return parent_order



def find_parent_order(txns):
    """ Sort the txns such that every txn comes after its parent. """
    visited = dict(list(zip([txn.txid for txn in txns], ["white" for txn in txns])))
    connected_txns = []
    
    for txn in txns:
        if visited[txn.txid] == "white":
            parent_order = visit_self_and_ancestors(txn, txns, visited, [])
            connected_txns.append(ConnectedTransactions(parent_order))
            
    return connected_txns