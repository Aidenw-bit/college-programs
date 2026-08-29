"""
Name: R.Anderson
Date: 9/3/25
Purpose: To calculate the average of two test scores

Pseudocode:

1. Read in two test scores, score1, score2
2. Calculate average, average = (score1 + score2)/2
3. Display the average
"""

# read test scores
score1 = float(input("Enter the score for test 1: "))
score2 = float(input("Enter the score for test 2: "))

# calculate average
average = (score1 + score2)/2

# display the average
print("The average is", average,".")

#using the concatenation operator
print('the average is ' +str(average) +'.')