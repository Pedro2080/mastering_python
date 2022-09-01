numbers = [1,2,3,4,5,6]

def check_even(num):
	return num % 2 == 0

print(f"Printing the even numbers that are in the list numbers")


# EXMAPLE 1
for n in filter(check_even, numbers):	# 2,4,6
	print(n, end=",") # This prints a list with a comma at the end .

print("\n========================\n")
# This does not print the comma at the end
print(",".join([str(x) for x in filter(check_even, numbers)]))

# EXAMPLE 2
print(f"\n{list(filter(check_even, numbers))}")		# [2,4,6]


# EXAMPLE 3
# Filtering the below list and getting only the prices greater than or equal to $10

items = [
    ("Product1", 10),
    ("Product1", 9),
    ("Product1", 12),
]
#lambda function takes an item and returns a boolean value tha determine if this item matches the criteria or not
filteredList = list(filter(lambda item: item[1] >=10, items))
print(f"\n{filteredList}")