def tax(bill):
	'''tax with add %8.0 to the bill'''
	bill *= 1.08
	print ("With tax: {0:.2f}".format(bill))
	return bill
def tip(bill):
	'''tip is will add 15% to bill with tax'''
	bill*=1.15
	print ("With tip: {0:.2f}".format(bill))
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)