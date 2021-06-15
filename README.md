# BlockOptimizer

This repository holds the code for the Summer of Bitcoin challenge. 

## Task
To construct a block from a mempool such that:                          

- For every transaction in the block, all it's parents are present before it in the block.

- The transactions in the block should yield the maximum fee in total

- The weight of all transactions together is below 4,000,000

## Instructions to run
Migrate to the ```src``` directory

```
python3 main.py <path to mempool.csv>
```
