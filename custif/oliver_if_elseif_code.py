#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


# message = 'The movie is about to begin, we recommend '

# wrap connection in a float() to accept decimals as numbers
grade = float(input("What was your test score, numerically?"))

# if input value was higher or equal to 25
if grade >= 90:
    message = 'Your grade is an A.'
elif grade >= 80:
      message = 'Your grade is a B.'
elif grade >= 70:
      message = 'Your grade is a C.'
elif grade >= 60:
      message = 'Your grade is a D.'
elif grade >= 50:
      message = 'Your grade is an F.'
else:
    message = 'Youve failed the class'
print(message)

