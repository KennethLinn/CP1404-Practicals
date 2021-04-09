#  count odd numbers from 1-20
def example():
    for i in range(1, 20 + 1, 2):
        print(i, end=" ")

#  count in 10 from 0-100
def a():
    for i in range(0, 100, 10):
        print(i, end=" ")

#  count down from 20-1
def b():
    for i in range(20, 0, -1):
        print(i, end=" ")

#  print n stars
def c():
    stars = int(input("Number of stars: "))
    for i in range(stars):
        print("*", end="")

#  print n lines of increasing stars
def d():
    stars = int(input("Number of stars: "))
    for i in range(1, stars + 1):
        print("*" * i)