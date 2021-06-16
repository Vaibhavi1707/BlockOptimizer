import sys
from file_operations import parse_mempool_csv, write_block_txt
from construct_block import construct_ordered_optimised_block
from entities.transaction import MempoolTransaction

MAX_WEIGHT = 4000000

if __name__ == '__main__':
    transactions = [MempoolTransaction(*transaction_details) 
                    for transaction_details in parse_mempool_csv(sys.argv[1])]
    print("Data inputted from mempool..")
    write_block_txt(construct_ordered_optimised_block(transactions, MAX_WEIGHT))
    print("Output written ..")