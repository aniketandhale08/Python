# Method 1
def km_to_miles(km):
  miles = km * 0.621371
  return miles

km = int(input("Enter the distance in kilometers: "))

miles = km_to_miles(km)

print(f"{km} kilometers is equal to {miles} miles.")



# Method 2
rate = 0.621371
km = int(input("Enter the km: "))
mile = km * rate
print(mile)