import sys

for index, item in enumerate(sys.argv[1:], start=1):
    print(f"{index}. {item}")
