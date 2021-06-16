import sys
sys.insert(0, ".")
from file_operations import parse_mempool_csv, write_block_txt
from construct_block import construct_ordered_optimum_block
from entities.transaction import MempoolTransaction

PATH_TO_MEMPOOL = "mempool.csv" if len(sys.argv) == 1 else sys.argv[1]
MAX_WEIGHT = 4000000 if len(sys.argv) <= 2 else int(sys.argv[2])

if __name__ == '__main__':
    transactions = [MempoolTransaction(*transaction_details) 
                    for transaction_details in parse_mempool_csv(PATH_TO_MEMPOOL)]
    print("Data inputted from mempool ..")
    
    write_block_txt(construct_ordered_optimum_block(transactions, MAX_WEIGHT))
    print("Output written ..")