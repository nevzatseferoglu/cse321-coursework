
def maxAdIncome(x, ad, M, size, dist):

    adIncomePerKm = [0 for _ in range(M + 1)]
    realDist = 0

    for i in range(1, M + 1):
        if (realDist < size):
            if (x[realDist] != i):
                adIncomePerKm[i] = adIncomePerKm[i - 1]  
            else:
                if (dist > i):
                    adIncomePerKm[i] = max(adIncomePerKm[i - 1], ad[realDist])
                else:
                    adIncomePerKm[i] = max(adIncomePerKm[i - dist - 1] + 
                                    ad[realDist],  
                                    adIncomePerKm[i - 1])
                    realDist += 1
        else:
            adIncomePerKm[i] = adIncomePerKm[i - 1]  
    
    
    return adIncomePerKm[M]


if __name__ == "__main__" : 
      
    M = 15
    x = [5, 6, 10] 
    ad = [4, 5, 7]  
    dist = 4
    size = len(x) 
    print(maxAdIncome(x, ad, M, size, dist))  