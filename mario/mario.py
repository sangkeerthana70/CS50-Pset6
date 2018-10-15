from cs50 import get_int

#prompts user for a positive integer
while True:
    height = get_int("Height: ")
    if (height >= 1 and height < 23):
        width = height + 1
        break
# prints rows = height of pyramid
for i in range(height):
    for j in range(height-i-1):
        print(" ", end = "")
    for k in range (i + 2):
        print("#", end = "")
    print("")