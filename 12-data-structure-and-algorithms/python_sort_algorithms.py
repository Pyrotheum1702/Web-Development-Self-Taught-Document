# Bubble Sort function
def bubble_sort(array):
    array_length = len(array)

    for i in range(array_length):
        for index in range(array_length - i - 1):
            if index < array_length and array[index] > array[index+1]:
                temp = array[index]
                array[index] = array[index+1]
                array[index + 1] = temp


array = [9, 3, 6, 1, 2, 7, 4, 2, 7, 5, 8, 9, 11, 2, 33, 45, 14]
array_1 = [10, 15, 20, 25, 16, 3, 23, 14, 29, 2, 1, 30, 21, 27,
           11, 24, 17, 28, 5, 18, 9, 19, 13, 22, 12, 26, 7, 6, 8, 4]
array_2 = [117, 39, 134, 272, 144, 394, 4, 325, 303, 282, 67, 159, 152, 338, 31, 429, 410, 26, 100, 435, 365, 11, 443, 106, 332, 421, 254, 13, 334, 486, 259, 457, 208, 378, 72, 145, 34, 22, 473, 7, 57, 460, 136, 312, 137, 124, 240, 94, 262, 477, 498, 483, 475, 197, 221, 170, 252, 191, 132, 267, 468, 497, 214, 189, 350, 397, 289, 293, 339, 273, 206, 432, 36, 290, 82, 162, 382, 32, 154, 176, 16, 284, 399, 333, 404, 104, 322, 400, 96, 257, 449, 438, 65, 246, 68, 361, 179, 46, 391,
           21, 53, 444, 14, 291, 171, 488, 495, 64, 433, 300, 376, 343, 121, 73, 402, 323, 211, 243, 18, 492, 93, 105, 187, 420, 56, 493, 313, 213, 299, 118, 80, 236, 295, 496, 405, 321, 15, 229, 98, 237, 309, 294, 3, 439, 233, 464, 49, 44, 352, 199, 60, 83, 183, 2, 89, 374, 166, 471, 427, 283, 91, 251, 69, 238, 465, 146, 423, 459, 329, 451, 48, 108, 207, 223, 130, 122, 302, 450, 372, 330, 215, 70, 383, 234, 261, 219, 125, 437, 317, 90, 409, 114, 142, 115, 288, 71, 163, 173, 355, 277]

# Testing section:

# Bubble sort:
# Before bubble sort:
print('before sort:', array)

bubble_sort(array)

# After bubble sort:
print('after sort:', array)
# ------------------------------|
# Before bubble sort:
print('before sort:', array_1)

bubble_sort(array_1)

# After bubble sort:
print('after sort:', array_1)
# ------------------------------|
# Before bubble sort:
# print('before sort:', array_2)

# bubble_sort(array_2)

# After bubble sort:
# print('after sort:', array_2)
