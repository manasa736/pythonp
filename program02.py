months={1:'january', 2:'february', 3:'march',4:'April', 5:'may',
        6:'june',7:'july',8:'August', 9:'september',
        10:'october', 11:'November', 12:'December',}
n=int(input())

for count in range(n):
    mn=int(input())
    if mn>=1 and mn<=12:
        print(months[mn])
    else:
        print("INVALID")


