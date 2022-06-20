# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None
# loop through all values
while True:
    sinteval = input('Enter an integer:')
    # end the loop if the input is donw
    if sinteval == 'done':
        break
    try:
        ninteval = int(sinteval)
    except:
        print('Invalid input')
        # go back to top of the loop if the input is not a num
        continue
    # get the smallest and maximum num
    if smallest is None or smallest > ninteval:
        smallest = ninteval
    if largest is None or largest < ninteval:
        largest = ninteval        
print('Maximum is', largest)
print('Minimum is', smallest)
