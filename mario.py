"""
rastgele kodlama keyfi wtih deni deni
mario with python
"""
height = 0
while True:
    height = int(input("Height:"))
    if (height < 9 and height > 0):
        break
    else:
        print("Enter a valid value!")
i = 1
while(height >= i):
    block = "#" * i
    space = " " * (height - i)

    print(f"{space}{block}")

    i += 1