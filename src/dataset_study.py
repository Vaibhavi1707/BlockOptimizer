from construct_block import find_parent_hierarchy 
# from utility import follows_topo_order
from file_operations import parse_mempool_csv
from transaction import MempoolTransaction

def is_cyclic(transactions):
    parent_order = find_parent_hierarchy(transactions)
    return False

def atleast_one_without_parent(transactions):
    return any(len(transaction.parents) == 0 for transaction in transactions)

def dataset_description(transactions):
    cyclic = is_cyclic(transactions)
    print(cyclic)
    one_orphan = atleast_one_without_parent(transactions)
    print(one_orphan)
    return {(False, False): "No cycles in parents and all transations have parents",
     (True, False): "Cyclic parents exist and all transactions have parents", 
     (False, True): "No cycles in parents and atleast one transaction has no parents",
     (True, True): "Cyclic parents exist and atleast one transaction has no parents"}[(cyclic, one_orphan)]
    
def parents_in_transactions(transactions):
    for transaction in transactions:
        for parent in transaction.parents:
            if parent not in [transaction.txid for transaction in transactions]:
                return False
    return True

def sum_of_fees(transactions):
    return sum(transaction.fee for transaction in transactions)

def no_of_connected_components(transactions):
    return find_parent_hierarchy(transactions)[1]

if __name__ == '__main__':
    transactions = [MempoolTransaction(*details) for details in parse_mempool_csv(input())]
    print(dataset_description(transactions))
    print("Sum of fees", sum_of_fees(transactions))
    print(no_of_connected_components(transactions))