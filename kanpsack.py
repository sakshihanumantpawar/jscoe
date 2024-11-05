class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def profit_to_weight_ratio(item):
    return item.profit / item.weight

def fractionalKnapsack(w, arr):
    arr.sort(key=profit_to_weight_ratio, reverse=True)
    finalValue = 0.0
    for item in arr:
        if w >= item.weight:
            finalValue += item.profit
            w -= item.weight
        else:
            finalValue += item.profit * (w / item.weight)
            break
    return finalValue

if __name__ == "__main__":
    n = int(input("Enter number of items-\n"))
    arr = []
    w = int(input("Enter capacity of knapsack-\n"))
    for i in range(n):
        profit = int(input("Enter profit of item " + str(i + 1) + "-\n"))
        weight = int(input("Enter weight of item " + str(i + 1) + "-\n"))
        arr.append(Item(profit, weight))
   
    print("Maximum value in knapsack: ", fractionalKnapsack(w, arr))
