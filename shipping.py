weight = 41.5

flat_charge = 20.00


#Ground Shipping
if weight <= 2:
  price_per_pound = 1.50
  cost = weight * price_per_pound
  cost += flat_charge
if weight >= 2 and weight <= 6:
  price_per_pound = 3.00
  cost = weight * price_per_pound
  cost += flat_charge
if weight >= 6 and weight <= 10:
  price_per_pound = 4.00
  cost = weight * price_per_pound
  cost += flat_charge
if weight >= 10:
  price_per_pound = 4.75
  cost = weight * price_per_pound
  cost += flat_charge

print("Ground Shipping cost: " )
print(cost)

premium_ground_shipping_flat_charge = 125.00
print("Ground shipping premium: ")
print(premium_ground_shipping_flat_charge)



#Drone Shipping
if weight <= 2:
  drone_price_per_pound = 4.50
  cost = weight * drone_price_per_pound
if weight >= 2 and weight <= 6:
  drone_price_per_pound = 9.00
  cost = weight * drone_price_per_pound
if weight >= 6 and weight <= 10:
  drone_price_per_pound = 12.00
  cost = weight * drone_price_per_pound
if weight >= 10:
  drone_price_per_pound = 14.25
  cost = weight * drone_price_per_pound

print("Drone shipping cost: ")
print(cost)