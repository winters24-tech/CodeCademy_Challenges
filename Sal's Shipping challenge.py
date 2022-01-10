print("Sal's Shipping\n")

weight = 7
# cost ground shipping 
if weight <= 2:
  print("Cost of shipping is $1.50")
elif weight <=6:
  print("Cost shipping is $3.00")
elif weight <=10:
  print("Cost of shipping is $4.00")
else:
  print("Cost of shipping is $4.75")

package = 8.4
flat_charge = 20.00

package_total = package * 4.00 + 20.00
print("Your total = ", '${:,.2f}\n'.format(package_total))

#cost for premium ground shipping
prem_shipping = '${:,.2f}'.format(125.00)
print("Package total for premium shipping has a flat rate of", prem_shipping,"\n")


#Drone shipping
if weight <= 2:
  print("Cost of drone shipping = $4.50")
elif weight <= 6:
  print("Cost of drone shipping = $9.00")
elif weight <= 10:
  print("Cost of drone shipping = $12.00")
else:
  print("Cost of drone shipping = 14.25")

drone_package = 1.5
drone_shipping = drone_package * 4.50 + 0.00

print("The total to ship your drone package = ",'${:,.2f}\n'.format(package_total))

#find the cheapest way to ship a 4.8lb package and the price
C1_package = 4.8
ground_C1 = C1_package * 3.00 + 20.00
drone_C1 = C1_package * 9.00 + 0.00

print("Hi, Customer 1! The best way to ship your 4.8lbs box here at Sal's would be ground shipping with a price of", '${:,.2f}\n'.format(ground_C1))

#find the cheapest price to ship a 41.5lb package
C2_package = 41.5
ground_C2 = C2_package * 3.00 + 20.00
drone_C2 = C2_package * 9.00 + 0.00

print("Hi, Customer 2! The best way to ship your 41.5lbs box here at Sal's would be ground shipping premium which has a flat rate price of", '${:,.2f}\n'.format(125.00))
