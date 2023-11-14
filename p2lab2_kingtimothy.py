#Timothy king
#11/14/23
#mathemathichal expressions and f-string
from statistics import mean
#Get input from the user
num1 = float(input("enter a float value: "))
num2 = float(input("enter a float value: "))        
num3 = float(input("enter a float value: "))
num4 = float(input("enter a float value: "))

#Create a empty list
num_list = []

#Add values to the list
num_list.append(num1)
num_list.append(num2)
num_list.append(num3)
num_list.append(num4)

#print the list to ensure values are added
print(num_list)

#Call methods on the list to get the sum and product
list_sum = sum(num_list)
list_avg = mean(num_list)
#Output to user formatted with f-string
print(f"{list_sum:.0f} {list_avg:.0f}")      
print(f"{list_sum:.3f} {list_avg:.3f}") 
