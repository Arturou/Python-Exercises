"""
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, 
if the sum (even after adjustment) exceeds 21, return 'BUST'
"""
def blackjack(a,b,c):
	arr = [a,b,c]
	summation = sum(arr)
	if summation <= 21:
		return summation
	elif 11 in arr:
		summation-=10
	return 'BUST' if summation > 21 else summation
	
print("Test #1: {}".format(blackjack(5,6,7)))
print("Test #2: {}".format(blackjack(9,9,9)))
print("Test #3: {}".format(blackjack(9,9,11)))