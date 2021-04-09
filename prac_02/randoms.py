import random
print(random.randint(5, 200))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
What did you see on line 1?
What was the smallest number you could have seen, what was the largest?

Answer: 5 is the smallest number and the possible largest number is 200
"""

"""
What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?

Answer: Line 2 returns random integer from 3 to 9 with step 2
"""

"""
What did you see on line 3?
What was the smallest number you could have seen, what was the largest?

Line 3 returns a random float anywhere from 2.5 to 5.5.
The smallest would be 2.50 and the largest would be 5.50
"""