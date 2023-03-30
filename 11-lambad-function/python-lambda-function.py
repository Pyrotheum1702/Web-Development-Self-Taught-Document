# A lambda function get the sum of two numbers and return it
add = lambda a, b: a + b
add2 = lambda a, b, c, d: a + b + c +  d

s = add(104, 28)
s_2 = add2(104, 28, -43, -33)
print(s)
# Result: 104 + 28 = 132
print(s_2)
# Result: 104 + 28 -43 -33 = 56
