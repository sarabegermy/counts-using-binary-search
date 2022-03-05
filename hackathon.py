import random
import time
import numpy as np

def counts_optimized(a, b):
    a.sort()
    res = []
    include = None
    for i in range(len(b)):
        start = 0
        end = len(a)-1
        mid_index = (end-start) // 2
        while(end >= start):
            if b[i]>=a[mid_index]:
                start = mid_index+1
                #n += n//2
                mid_index = (end + start) // 2
                include = True
            else:
                end = mid_index
                mid_index = (end + start) // 2
                include = False
                if start == end:
                    #mid_index = mid_index-1
                    break

        if include:
            res.append(mid_index+1)
        else:
            res.append(mid_index)

    return res


def counts_reshaping(teamA, teamB):
    a = np.array(teamA)[np.newaxis, :]
    b = np.array(teamB)[:, np.newaxis]

    return list((a <= b).sum(axis=1))


def counts_caching(teamA, teamB, cach={}):
    teamA = np.array(teamA)
    results = []
    for m in teamB:
        if m not in cach:
            cach[m] = (teamA <= m).sum()
        results.append(cach[m])
    return results


'''
def counts(a,b):
    a.sort()
    #b_copy = b.sort(reverse=True)
    res=[]
    for i in range(len(b)):
        count=0
        j=0
        while(b[i]>=a[j]):
            count=count+1
            j +=1

        res.append(count)
    return res
'''


'''
    n = (int)(input())
    teamA = []
    for i in range(n):
        teamA.append((int)(input()))
    m = int(input())
    teamB = []
    for i in range(m):
        teamB.append((int)(input()))
'''
if __name__ == '__main__':
    teamA = np.random.randint(1e9, size=int(1e5))
    teamB = np.random.randint(1e9, size=int(1e5))

    start = time.time()
    #print(counts_optimized(teamA, teamB))
    counts_optimized(teamA, teamB)
    end = time.time()
    print("Binary Search Algorithm took: ", end-start)

    start = time.time()
    #print(counts_reshaping(teamA, teamB))
    counts_reshaping(teamA, teamB)
    end = time.time()
    print("Reshaping Approach took: ", end - start)

    start = time.time()
    #print(counts_caching(teamA, teamB))
    counts_caching(teamA, teamB)
    end = time.time()
    print("Caching Approach took: ", end - start)


