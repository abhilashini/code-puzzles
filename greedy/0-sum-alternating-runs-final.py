def getMaxSum(arr):
  n = len(arr)
  max_sum = 0
  i = 0

  while i < n-1:
    curr_max = arr[i]

    if arr[i] > arr[i+1]:
      while i < n-1 and arr[i] > arr[i+1]:
        i += 1
        curr_max = max(curr_max, arr[i])
      max_sum += curr_max
    elif arr[i] < arr[i+1]:
      while i < n-1 and arr[i] < arr[i+1]:
        i += 1
        curr_max = max(curr_max, arr[i])
      max_sum += curr_max
    else:
      i += 1

  return max_sum

def test_getMaxSum():
    assert getMaxSum([5, 4, 3, 2]) == 5
    assert getMaxSum([1, 2, 3, 2, 1, 4, 5]) == 11
    assert getMaxSum([1, 2, 1, 2, 1]) == 8
    print("PASSED ALL TESTS.")
    
test_getMaxSum()
