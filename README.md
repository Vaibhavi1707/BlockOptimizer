# BlockOptimizer

This repository holds the code for the Summer of Bitcoin challenge. 

## Task
To construct a block from a mempool such that:                          

- For every transaction in the block, all it's parents are present before it in the block.

- The transactions in the block should yield the maximum fee in total

- The weight of all transactions together is below 4,000,000

## Approach

All the transactions when connected to their parents, form a directed acyclic graph. This is because any transaction cannot be a parent as well as a descendent of another transaction. 

Thus, to order any transaction after all its parents in a block, we can reverse the topological sort of this graph or any connected component of it to get the parent to descendent ordering within the graph or the component repectively.

I have several approaches of optimising the block to maximise the total fee.

### Approach 1

Since we have the parent to descendent ordering obtained from the topological sort of the entire graph, we now only have to pick a subset of the transactions inorder to maximise the fee, but at the same time upper bounding the total weight to 4 million. 

Hence, this is simplified to the 0 1 Knapsack problem. We use dynamic programming to maximise the fee while capping the total weight of all selected transactions.

**Time Complexity**: O(n * W)

**Drawbacks**:

- There's no way to ensure whether *all* parents of a transaction are selected or not.

- Exhaustion of computing power: Due to the high value of maximum capacity of 4 million (4 * 10 ^ 6), the program takes a long time for execution. The system may also crash considering we don't use the space optimised version of 0 1 Knapsack, where only O(W) space is consumed, else we use the one with O(n * W) space. 

There are algorithms to improve the time complexity of 0 1 Knapsack on an average, one of which is the [branch and bound method](https://www.geeksforgeeks.org/0-1-knapsack-using-branch-and-bound/). This is based on the fact that it rejects infeasible solutions. The main observation here is that the solution given by fractional knapsack algorithm upperbounds the answer given by 0 1 knapsack. It is a backtracking algorithm, which works slightly better than brute force.

**Note**: The first drawback can be mitigated however by adding a ```flag``` to the transactions data structure which is true if it's selected. Thus, for all transacations, before entering it into the knapsack, we can check whether all it's parents are taken or not.  

### Approach 2

This is an approximate approach and may not be completely accurate in the general case. This has been adopted due to the lack of computing power.

We obtain topologically sorted connected components of the transaction graph, let's call them collections. 

We see that if we take one transaction ```a``` from a collection say ```A```, we will have to include all the transactions preceding ```a``` in ```A```. This is to obey the *all* parents selection and ordering criteria of the problem.

Further, we see that we need not have to take all the transactions from a collection. Thus, the problem now looks similar to Fractional Knapsack over these collections. 

Thus, we sort the collections by the ratio of their net fee and net weight in the decreasing order and greedily add transactions from these collections to the knapsack. 

**Complexity**: O(nlogn)

## Instructions to run
Migrate to the ```src``` directory

```
python3 main.py <path to mempool.csv>
```

## References

https://www.geeksforgeeks.org/fractional-knapsack-problem/
