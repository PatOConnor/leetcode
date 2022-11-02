# takes in a list of numbers and a target number, 
# and returns the two elements of the array that 
# add up to the target
def two_sum(nums: list[int], target: int)->list[int]:
  nums.sort()
  size = len(nums)
  #each iter, binary search the rest for the other component to add to the target value
  for i in range(size):
    while(True):
      j = (size - i) // 2
      s = nums[i] + nums[j]
    ...
  

