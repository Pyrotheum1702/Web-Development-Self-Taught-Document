import re
from re import search

# simple regex example
p_1 = '[a-z][a-z][a-z]'
# the pattern mean finding the first 3 lowercase character from a to z that close to each other
print(search(p_1 ,'Thanh Dao'))
# Result: 'han' in 'Thanh', 'T' is skipped because it's uppercase character

# if there are no match return None
print(search(p_1, 'ab21v'))
# Result: None

# in range `-` example:
print(search('[a-z][a-z]', 'Thanh Dao'))
# Result: ha
print(search('[A-Z][a-z]', 'Thanh Dao'))
# Result: Th
print(search('[a-z][a-z][0-9]', 'Thanh Dao2'))
# Result: ao2

# simple regex example:

# `.` example:
print(search('1.zF.', 'a1vzFZ&'))
# Result: 1vzFZ
print(search('.vz', 'a1vzFZ'))
# Result: 1vz

# `|` example:
print(search('Thanh|Dao|Trinh', 'kdfThanhcm'))
# Result: Thanh
print(search('Thanh|Dao|Trinh', 'kdfDaoxm'))
# Result: Dao
print(search('Thanh|Dao|Trinh', 'kdfTrinhxm'))
# Result: Trinh

# `\W` example:
print(search('\w', '#(.K$@&'))
# Result: K
print(search('[a-zA-Z0-9_]', '#(.K$@&'))
# Result: K

# `\w` example:
print(search('\W', 'dhhv23c6#ajx'))
# Result: #

# `\d` example:
print(search('\d', 'dhhv23c6#ajx'))
# Result: 2

# `\D` example:
print(search('\D', '829#dhhv23c6#ajx'))
# Result: #
print(search('\D', '349345hv23c6#ajx'))
# Result: h

# `\s` example:
print(search('\s', 'line1\nline2'))\
# Result: \n
print(search('\s', 'line1 line2'))
# Result: * * <- white space

# `\S` example:
print(search('\S', '     \n    K    '))\
# Result: K
print(search('\S', '     \n       \n # '))\
# Result: #

# '^' example:
print(search('^Thanh', 'ThanhDao'))
# Result: Thanh
print(search('^Thanh', 'DaoThanh'))
# Result: None

# '\A' example:
print(search('\AThanh', 'ThanhDao'))
# Result: Thanh
print(search('\AThanh', 'DaoThanh'))
# Result: None

# '$' example:
print(search('Dao$', 'ThanhDao'))
# Result: Dao
print(search('Dao$', 'DaoThanh'))
# Result: None

# '\Z' example:
print(search('Dao\Z', 'ThanhDao'))
# Result: Dao
print(search('Dao\Z', 'DaoThanh'))
# Result: None

# `\b` example:
print(search(r'Thanh\b', "Thanh Dao"))
# Result: Thanh
print(search(r'\bThanh', "ThanhDao"))
# Result: Thanh
print(search(r'Thanh\b', "ThanhDao"))
# Result: None
print(search(r'\bThanh\b', "ThanhDao"))
# Result: None

# `\B` example:
print(search(r'\BDao', "Thanh Dao"))
# Result: None
print(search(r'Dao\B', "ThanhDao"))
# Result: None
print(search(r'\BDao', "ThanhDao"))
# Result: Dao
print(search(r'\BDao\B', "ThanhDaoTrong"))
# Result: Dao
print(search(r'\BDao\B', "ThanhDao"))
# Result: None

# `*` example
print(search('ThanhA*Dao', "ThanhAAAADao"))
# Result: ThanhAAAADao
print(search('ThanhA*Dao', "ThanhDao"))
# Result: ThanhDao

# `+` example
print(search('ThanhA+Dao', "ThanhAAAADao"))
# Result: ThanhAAAADao
print(search('ThanhA+Dao', "ThanhDao"))
# Result: None

# `?` example
print(search('ThanhA?Dao', "ThanhDao"))
# Result: ThanhDao
print(search('ThanhA?Dao', "ThanhADao"))
# Result: ThanhADao
print(search('ThanhA?Dao', "ThanhAAAADao"))
# Result: ThanhAAAADao
