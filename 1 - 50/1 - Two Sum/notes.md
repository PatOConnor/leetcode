# Two Sum Notes

### Pseudocode

1. sort list
2. iterate through list ( O(n) )
   a. search other list for other component to add to target value
   b. when value is found, return result

### Binary Search

looking for a value
check what the value at the halfway point is,
if its too low, go high, and vice versa

#### Binary Search While Loop Implementation

###### Python

```python
def binary_search_while(nums:list[int], target:int):
  """Searches the list for the number passed as an argument

  Parameters:
    nums (list[int]): a sorted list of integers
    target (int): an integer value being searched for

  Returns:
    index of the target value, or -1 if the value is not present

  """
  # loop chops list in half until it either finds the value or deletes it all
  while len(nums) >= 1:
    # starting point for the search is halfway through the array
    i = len(nums) // 2:
    # correct answer gets returned
    if nums[i] == target: return i
    # if value is too high, check bottom half
    elif nums[i] > target: nums = nums[i+1:]
    # if value is too low, check top half
    else: nums = nums[:i]
  #if there are no more numbers to check, the target is not able to be found
  return -1
```

###### Javascript (ES6)

```javascript
/**
 * Performs a binary search for a value by slicing the list in half until the value is found
 * @param {List[Number]} nums   A list of numbers
 * @param {Number}       target The specified number being searched for
 * @return {Number}             Returns index of entry where target is located, or -1 if not found
*/
const binarySearchWhileLoop = (nums, target) => {
  let i;
  while (nums.length >= 1) {
    // check if the halfway point is equal. If not, then
    // with the equal disqualified, greater/less is now a boolean,
    // which can be implemented as a nested ternary operator
    i = Math.floor(nums.length / 2)
    nums[i] == target
      ? return i;
      : nums[i] > target
          ? nums = nums.slice(i+1)
          : nums = nums.slice(0,i)
  }
  //if there are no more numbers to check, the target is not able to be found
  return -1;
}

```

#### Binary Search Recursive Implementation to check whethera value is in a list

```python
def binary_search_recur(nums, target):
  """Checks if target

  Parameters:
    nums (list[int]): a list of integers
    target (int): the integer being searched for

  Returns:
    True if the Target is in the List, False if it does not
  """
  size = len(nums)
  if size == 0: return -1
  if size == 1: return nums[0] == target
  i = size // 2
  nums = nums[:i] if nums[i] > target else nums[i:]
  return binary_search_recur(nums, target)
```

```javascript
/**
 * Performs a binary search for a value by slicing the list in half until the value is found
 * @param {List[Number]} nums   A list of numbers
 * @param {Number}       target The specified number being searched for
 * @return {Number}             Returns True if entry is there, false if not
 */
const binarySearchRescursive = (nums, target) => {
  if (nums.length == 0) {
    return -1;
  }
  if (nums.length == 1) {
    return nums[0] === target;
  }
  i = Math.floor(nums.length / 2);
  nums[i] > target ? nums.slice(i + 1) : nums.slice(0, i);
};
```

### Two Sum

- Two sum is an O(nlogn) solution where you iterate through a sorted list and then do a binary search on the shrinking remainder

###### Python

```python
def binary_search(nums, target):
  # loop chops list in half until it either finds the value or deletes it all
  while len(nums) >= 1:
    # starting point for the search is halfway through the array
    i = len(nums) // 2:
    # correct answer gets returned
    if nums[i] == target: return i
    # if value is too high, check bottom half
    elif nums[i] > target: nums = nums[i+1:]
    # if value is too low, check top half
    else: nums = nums[:i]
  #if there are no more numbers to check, the target is not able to be found
  return -1

def two_sum (nums, target):
  nums.sort()
  for i in range(len(nums)):
    j = binary_search(nums[i:], nums[i]*-1)
    if j != -1:
      return [i, j]

```

###### Javascript (ES6)

```javascript
/**
 * Performs a binary search for a value by slicing the list in half until the value is found
 * @param {List[Number]} nums   A list of numbers
 * @param {Number}       target The specified number being searched for
 * @return {Number}             Returns index of entry where target is located, or -1 if not found
*/
const binarySearch = (nums, target) => {
  let i;
  while (nums.length >= 1) {
    // check if the halfway point is equal. If not, then
    // with the equal disqualified, greater/less is now a boolean,
    // which can be implemented as a nested ternary operator
    i = Math.floor(nums.length / 2)
    nums[i] === target
      ? return i;
      : nums[i] > target
          ? nums = nums.slice(i+1)
          : nums = nums.slice(0,i)
  }
  //if there are no more numbers to check, the target is not able to be found
  return -1;
}
var two_sum = function(nums, target) {
  nums.sort()
  for (let i = 0; i < nums.length; i++){
    j = binarySearch(nums.slice(i), nums[i] * -1)
    if (j !== -1) { 
      return [i, j] 
    }
  }
}
```


