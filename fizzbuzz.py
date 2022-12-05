import sys

for index in sys.argv[1:]:
    i = int(index)
    if i % 3 == 0 and i % 5 == 0: print("fizzbuzz")
    elif i % 3 == 0: print("fizz")
    elif i % 5 == 0: print("buzz")
    else: print(i)
