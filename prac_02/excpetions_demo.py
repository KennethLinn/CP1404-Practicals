try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
1.
When will a ValueError occur?
Answer: A ValueError will occur when the input is a string or a float.

2.
When will a ZeroDivisionError occur?
Answer: A ZeroDivisionError will occur when the input for the denominator is 0.

"""