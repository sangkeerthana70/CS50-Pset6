from cs50 import get_int

#prompts user for a positive integer
while True:
    height = get_int("Height: ")
    if (height >= 1 and height < 23):
        break
# prints rows = height of pyramid
for i in range(height):
    # prints spaces for height minus i - 1
    for j in range(height-i-1):
        print(" ", end = "")
    # prints # for height + 2
    for k in range (i + 2):
        print("#", end = "")
    print("")