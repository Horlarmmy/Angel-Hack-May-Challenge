def min_cost(efficiency):
    mincost = float('inf')
    efficiency_sortedn = sorted(efficiency)
    for i in efficiency_sortedn:
        efficiency_sorted = efficiency_sortedn[:]
        efficiency_sorted.remove(i)
        pairs = [(efficiency_sorted[i],efficiency_sorted[i+1]) for i in range(0, len(efficiency_sorted), 2)]
        cost = sum(abs(pair[0] - pair[1]) for pair in pairs)
        if cost < mincost:
            mincost = cost
            rem = i
            paired = pairs
        else:
            mincost = mincost
    
    return(mincost, rem, paired)


efficiency = [1, 3, 54, 712, 52, 904, 113, 12, 135, 32, 31, 56, 23, 79, 611, 123, 677, 232, 997, 101, 111, 123, 2, 7, 24, 57, 99, 45, 666, 42, 104, 129, 554, 335, 876, 35, 15, 93, 13]
results = min_cost(efficiency)
print("Worker with efficiency {} was excluded \n" .format(results[1]))
print("The paired used to get the minimum cost {}\n".format(results[2]))
print("The minimum cost of the given array is {}" .format(results[0]))
