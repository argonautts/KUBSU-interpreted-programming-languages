import random

def printDict(cart):
    for key, value in cart.items():
        print("Cart:", key, " = ", value)
    print()

def cartCheck(cart):
    count = 0
    cMiddle = 0
    for key, value in cart.items():
        for indexValue in range(len(value)):
            if value[indexValue] == 0:
                count += 1
        if value[2] == 0:
            cMiddle += 1
        if count == 5 or cMiddle == 5:
            return True
        count = 0
    return False

cart = dict(B = random.sample(range(1, 16), 5),
            I = random.sample(range(16, 31), 5),
            N = random.sample(range(31, 46), 5),
            G = random.sample(range(46, 61), 5),
            O = random.sample(range(61, 76), 5))
printDict(cart)

randomQuantity = int(input("Enter the numbers of lots won: "))
winNumbers = random.sample(range(1, 76), randomQuantity)
winNumbers.sort()

print("winNumbers = ", winNumbers)
print()

for key, value in cart.items():
    for indexValue in range(len(value)):
        for indexWinNumbers in range(len(winNumbers)):
            if value[indexValue] == winNumbers[indexWinNumbers]:
                cart[key][indexValue] = 0

printDict(cart)

if cartCheck(cart):
    print("Cart win")
else:
    print("Cart lose")