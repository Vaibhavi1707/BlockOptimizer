# Python3 program to solve fractional
# Knapsack Problem


class ItemValue:

	"""Item Value DataClass"""

	def __init__(self, wt, val, ind):
		self.wt = wt
		self.val = val
		self.ind = ind
		self.cost = val // wt

	def __lt__(self, other):
		return self.cost < other.cost

# Greedy Approach


def getMaxValue(wt, val, capacity):
    """function to get maximum value """
    iVal = []
    for i in range(len(wt)):
        iVal.append(ItemValue(wt[i], val[i], i))

    # sorting items by value
    iVal.sort(reverse=True)
    print([(i.cost, i.val, i.wt) for i in iVal])
    sack = []
    totalValue = 0
    for i in iVal:
        curWt = int(i.wt)
        curVal = int(i.val)
        if capacity - curWt >= 0:
            capacity -= curWt
            totalValue += curVal
            sack.append((i.ind, i.val, i.wt))
        else:
            fraction = capacity / curWt
            totalValue += curVal * fraction
            capacity = int(capacity - (curWt * fraction))
            sack.append((i.ind, fraction * i.val, fraction * i.wt))
            break
    print(sack)
    return totalValue


# Driver Code
if __name__ == "__main__":
	wt = [10, 40, 20, 30]
	val = [60, 40, 100, 120]
	capacity = 50

	# Function call
	maxValue = getMaxValue(wt, val, capacity)
	print("Maximum value in Knapsack =", maxValue)

# This code is contributed by vibhu4agarwal
