def parse_mempool_csv(path_to_mempool):
    """ Parse the CSV file and return a list of MempoolTransactions. """
    with open(path_to_mempool) as f:
        return([line.strip().split(',') for line in f.readlines()][1:])
    
def write_block_txt(transactions, write_to):
    """ Write transaction ids in the block file. """
    with open(write_to, "w") as output_file:
        for transaction in transactions[:-1]:
            output_file.write(transaction + "\n")
        output_file.write(transactions[-1])