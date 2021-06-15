def parse_mempool_csv(path_to_mempool):
    """ Parse the CSV file and return a list of MempoolTransactions. """
    with open(path_to_mempool) as f:
        return([line.strip().split(',') for line in f.readlines()][1:])
    
def write_block_txt(transactions):
    """ Write transaction ids in the block file. """
    output_file = open("block.txt", "w")
    for transaction in transactions:
        output_file.write(str(transaction) + "\n")