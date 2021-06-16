from order_transactions import find_parent_order


def get_partial_txns(max_wt, connected_txns):
    """ Get a part of connected txns such that the total weight is less than max_weight  """
    txns = connected_txns.parent_order
    partial_txns, i = [], 0
    
    while max_wt >= txns[i].wt:
        partial_txns.append(txns[i])
        i += 1
    
    return partial_txns



def find_optimum_block(max_wt, txns):
    """ Finds the optimal block with total weight less that 4 million and maximum fee. """
    txns.sort()
    block = []

    for txn in txns:
        curr_wt = txn.net_wt
        curr_fee = txn.net_fee
        
        if max_wt >= curr_wt:
            max_wt -= curr_wt
            block += [txn.txid for txn in txn.parent_order]
        else:
            block += [txn.txid for txn in get_partial_txns(max_wt, txn)]
    
    return block


    
def construct_ordered_optimum_block(txns, max_wt):
    """ Finds an ordered block which maximises the total fees obtained. """
    connected_txns = find_parent_order(txns)
    
    ordered_optimum_block = find_optimum_block(max_wt, connected_txns)
    
    return ordered_optimum_block