def printSeries(ch,n):
    assert(n>=0), 'INVALID'
    for i in range(n):
        print(ch*i)
        

ch=input()
n=int(input())
try:
    printSeries(ch,n)
except AssertionError as b:
    print(b)
