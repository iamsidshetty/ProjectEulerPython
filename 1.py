__author__ = 'sid'

def div_by_3_and_5(N):
    sum = 0
    for i in range(N):
        if i % 3 == 0 or i%5 == 0:
           sum += i

    return sum

print div_by_3_and_5(1000)