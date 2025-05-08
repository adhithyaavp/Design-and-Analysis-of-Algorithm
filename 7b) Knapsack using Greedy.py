def fractional_knapsack(weights, values, capacity):
    ratio = [(v/w, w, v) for v, w in zip(values, weights)]
    ratio.sort(reverse=True)

    total_value = 0
    for r, w, v in ratio:
        if capacity >= w:
            total_value += v
            capacity -= w
        else:
            total_value += r * capacity
            break
    return total_value

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print("Maximum value in knapsack:", fractional_knapsack(weights, values, capacity))
