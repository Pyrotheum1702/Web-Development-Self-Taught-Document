# 1. What is a quote?
#   - a quote is a sequence of characters enclosed in quotation marks
#   - quotation marks are these symbols:
#     - '
#     - "
#   - in programming they call a quote as a string literal
#   - Example:
name = 'nguyen quang duoc'
#      |-----------------|
#               ^
#               |
# This is a string literal, a sequence of characters enclosed in single quotes
#   - Example:
name = "nguyen quang duoc"
#      |-----------------|
#               ^
#               |
# This is a string literal, a sequence of characters enclosed in double quotes
# ----------------------------------------------------------------------------
# 2. What are different types of quotes
#   - There are three different type of quotes:
single_quotes = 'hello'
double_quotes = "hello"
triple_quotes = '''hello'''
#   - What is the different between them:
#     - Single and double quote work the same, just different in symbol
#     - Triple quotes are used to span the string across multiple lines
#       - Example:
triple_quotes = '''This is a paragraph. It is
 made up of multiple lines and sentences.'''
# 3. Notice
#   - Single and double quote work the same, just different in symbol
#   - You could also use """ """ to form a triple quotes instead of ''' '''
#     - Example:
triple_quotes = """This is a paragraph. It is
 made up of multiple lines and sentences."""
#   - If you want to have quotation mark in a string literal,
# use the quotation mark that is different to the enclosure quotation mark.
#     - Example no.1:
print('"The only source of knowledge is experience."')
# Expected result: "The only source of knowledge is experience."
#     - Example no.2:
print("'Anyone who has never made a mistake has never tried anything new.'")
# Expected result: 'Anyone who has never made a mistake has never tried anything new.'
