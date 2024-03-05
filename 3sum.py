nums = [-1,0,1,2,-1,-4]
def threeSum(nums):

    arr = []
    nums.sort()
    for i in range(len(nums)-2):
        if i < 0 and nums[i] == nums[i-1]:
            continue
        l = i +1
        r = len(nums) - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total > 0:
                l = l +1
            elif total <  0:
                r = r-1
            else:
                arr.append(nums[i], nums[l], nums[r])

                while l < r and nums[l] == [l+1]:
                 l = l+1

                while l < r and nums[r] == [r-1]:
                     r = r-1
    return arr
       
 
