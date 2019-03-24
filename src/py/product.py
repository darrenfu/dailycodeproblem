#Uber
#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#Follow-up: what if you can't use division?

def product(lst):
  product_list = []
  for i in range(len(lst)):
    product = 1
    for j in range(len(lst)):
      if (j != i):
        product *= j
    product_list.append(product)
  return product_list