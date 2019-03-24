#Uber
#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#Follow-up: what if you can't use division?

def product(lst):
  total_product = 1
  product_list = []
  for i in range(len(lst)):
    total_product *= lst[i]
  for j in range(len(lst)):
    product_list.append(total_product / lst[j])
  return product_list

def productExceptSelf(lst):
  len = len(lst)
  left_arr = [1] * len
  right_arr = [1] * len
  product_arr = [1] * len
  for i in range(1, len):
    left_arr[i] = lst[i-1] * left_arr[i-1]
  for j in range(len - 2, -1, -1):
    right_arr[j] = lst[j+1] * right_arr[j+1]
  for k in range(len):
    product_arr[k] = left_arr[k] * right_arr[k]
  return product_arr

def productExceptSelf(nums):
  leng = len(nums)
  product_arr = [1] * leng
  tmp = 1
  for i in range(leng):
    product_arr[i] = tmp
    tmp *= nums[i]
  tmp = 1
  for j in range(leng - 1, -1, -1):
    product_arr[j] *= tmp
    tmp *= nums[j]
  return product_arr
  
