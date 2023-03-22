name = ["Duoc", "Dung", "Hiep"]

# A simple iteration reading all element in a List:
for n in name:
  print(n)

# get the iterator form of the list(sequence)
name_iter = iter(name)

# A demonstration of iterator mechanism that work almost identical to the `for` loop shown above
while True:
  try:
    n = next(name_iter) # get next item
    print(n)
  except StopIteration: # stop when out of item
    break # exit while loop


# An iterator class example
class ContactList:

  def __init__(self):
    self.index = -1
    self.contact_dict = {} # Key = name, Value = phone number

  def set_contact(self, name: str, number: int):
    self.contact_dict[name] = number
# Iterator protocol: __iter__
  def __iter__(self):
    return iter(self.contact_dict.items())
# Iterator protocol: __next__
  def __next__(self):
    self.index += 1
    return list(self.contact_dict)[self.index]

# ContactList instantiate
duoc_contact_list = ContactList()
duoc_contact_list.set_contact("Hung", 3498928243)
duoc_contact_list.set_contact("Dat", 3494289568)
duoc_contact_list.set_contact("Thanh", 3492888434)

# Iteration to read duoc_contact_list
for (name, number) in duoc_contact_list:
  print(name, number)

# Iteration to read names in duoc_contact_list
for (name, number) in duoc_contact_list:
  print(name)

# Iteration to read numbers in duoc_contact_list
for (name, number) in duoc_contact_list:
  print(number)