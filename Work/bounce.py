# bounce.py
#
# Exercise 1.5
height = 100
bounce_number = 1

while bounce_number <= 10:
    height = height * 3/5
    # print(bounce_number, height)
    print(bounce_number, round(height, 4))
    bounce_number = bounce_number + 1
