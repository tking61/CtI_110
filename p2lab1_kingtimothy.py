#Timothy King
#11/14/23
#use float values to represent the cost to drive a specified distance

#Get input from user
mpg = float(input("Enter the car's mpg as a decimal number: "))
cost_gal = float(input("Enter the cost for one gallon of gas: "))

#calculate cost to drive 20 miles
drive_cost_20 = (20/mpg) *cost_gal

#calculate cost to drive 75 miles
drive_cost_75 = (75/mpg) *cost_gal

#calculate cost to drive 500 miles
drive_cost_500 = (500/mpg) *cost_gal

#output the costs with 2 decimal places using an f-string
print(f"cost to drive 20 miles is{drive_cost_20:.2f}")

#output the costs with 2 decimal places using an f-string
print(f"cost to drive 75 miles is{drive_cost_75:.2f}")

#output the costs with 2 decimal places using an f-string
print(f"cost to drive 500 miles is{drive_cost_500:.2f}")
