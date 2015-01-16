"""
refactor to read csv and check all customers 
to see if any have underpaid
"""

# set indices to use when reading data from .csv file
CUST_NUMBER_INDEX = 0 
CUST_NAME_INDEX = 1
CUST_MELONS_INDEX = 2
CUST_PAID_INDEX = 3

def check_payments():

	print "\n" * 5
	print "checking orders and payments...."
	print

	customer_orders_file = open("customer_orders.csv")

	melon_cost = 1.00

	for line in customer_orders_file:

		dataList = line.split(",")
		cust_number, cust_name, cust_melons, cust_paid = dataList
		cust_expected = float(cust_melons) * melon_cost

		if cust_expected != float(cust_paid):
			print cust_name, "paid %.2f, expected %.2f"%(float(cust_paid), cust_expected)

	customer_orders_file.close()
	print "." * 80
	print "Done checking this batch of orders and payments!"
	print "\n" * 3

check_payments()