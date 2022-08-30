# 1) NUMBER - Integer
students_count = 1000

# 2) NUMBER - Float
students_count = 4.99

# 3) BOOLEAN
is_published = False
is_published = True
1 == 1	# True
1 > 2	# False

# 4) STRING
full_name = "Joao Pedro da Silva"

print(f'Hello {full_name}')


# 5) METHODS
x = 3.5
y = 3
int(x)      # 3
float(y)    # 3.0
bool(y)     # True
str()


# 6) SWAPPING VARIABLES

# First Way
x = 10
y = 11
print(f"x = {x} , y = {y}")


z = x
x = y
y = z
print(f"x = {x} , y = {y}")


# Second way  - by using tuples
a, b = 10, 11
print(f"a = {a} , b = {b}")

a, b = b, a
print(f"a = {a} , b = {b}")
