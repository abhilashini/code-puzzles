def getMaxSum(arr):
    n = len(arr)
    i = 0
    max_sum = 0

    print(f"before loop starts. arr = {arr}, arr[0] = {arr[0]}")

    while 0 <= i+1 < n:
        print(f"index: {i}")
        curr_run_max = arr[i] # Needs to be arr[i]; not float("-inf")

        if arr[i] > arr[i+1]:
            while 0 <= i+1 < n and arr[i] > arr[i+1]:
                i += 1
                curr_run_max = max(curr_run_max, arr[i]) # NEED THIS TO COME FIRST AND THEN INC i
                print(f"i: {i}, curr_run_max={curr_run_max}, arr[{i}]={arr[i]}")
        elif arr[i] < arr[i+1]: # don't check == because that's not a run.
            while 0 <= i+1 < n and arr[i] < arr[i+1]:
                i += 1
                curr_run_max = max(curr_run_max, arr[i]) # NEED THIS TO COME FIRST AND THEN DEC i

        print(f"curr_run_max = {curr_run_max}")

        max_sum += curr_run_max

        # i += 1 # no need to increment this

        '''if i < n:


            i -= 1'''


    print(f"max_sum = {max_sum}")


    return max_sum
    
def test_getMaxSum():
    assert getMaxSum([5, 4, 3, 2]) == 5
    assert getMaxSum([1, 2, 3, 2, 1, 4, 5]) == 11
    assert getMaxSum([1, 2, 1, 2, 1]) == 8
    
test_getMaxSum()
        
    
def test_getMaxSum():
    assert getMaxSum([5, 4, 3, 2]) == 5
    assert getMaxSum([1, 2, 3, 2, 1, 4, 5]) == 11
    assert getMaxSum([1, 2, 1, 2, 1]) == 8
    
test_getMaxSum()
