def tonghaisolonnhat(nums):
    if len(nums) < 2 :
        raise ValueError("Danh sách phải có ít nhất hai số.")
    
    lonnhat1 = float("-inf")
    lonnhat2 = float("-inf")

    for num in nums:
        if num > lonnhat1:
            lonnhat2 = lonnhat1
            lonnhat1 = num
        elif num > lonnhat2:
            lonnhat2 = num


    return lonnhat1 + lonnhat2



# Test 
print(tonghaisolonnhat([1, 4, 2, 3, 5]))