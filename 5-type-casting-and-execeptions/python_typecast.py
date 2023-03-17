# 1. Implicit type cast example
# - Integer addition with float
number = 10
decimal_number = 2.5
print(number + decimal_number)
# Result: number(int) + decimal_number(float) = 12.5(float)

# 2. Explicit type cast example
# - Integer typecast

# float to int
f = 1.182
print(int(f))
# Result: 1.182(float) -> 1(int)

# string to int
s = "148"
print(int(s))
# Result: "148"(str) -> 148(int)

# - Float typecast

# int to float
i = 10
print(float(i))
# Result: "10(int) -> 10.0(float)

# string to float
s = "15.7"
print(float(s))
# Result: "15.7"(str) -> 15.7(float)

# - String typecast

# int to string
i = 5
print(str(i))
# Result: 5(int) -> "5"(str)

# # float to string
f = 4.7
print(str(f))
# Result: 4.7(float) -> "4.7"(str)

print(int("abc"))