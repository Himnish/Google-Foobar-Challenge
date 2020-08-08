def solution(l):
#     # Your code here
#     We start by initialising a counter for every number in the list.
#     This counter resembles the number of times a particular entry in the list has been a multiple of a previous number.
#     Each time we increment that, we can also increase our number of triplets by the factor we're currently evaluating.
        triplets = 0
        size = len(l)
        if size < 3: 
            return 0
        counter = [0] * size
        for product in xrange(size):
            for factor in xrange(product + 1, size):
                if l[factor] % l[product] == 0:
                    counter[factor] += 1
                    triplets += counter[product]
        return triplets
