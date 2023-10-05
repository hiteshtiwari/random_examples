# def threesum(nums):
#     answer = []
#     nums.sort()
#     for i in range(len(nums) - 2):
#         # num = nums[i]
#         l = i+1
#         r = len(nums) - 1
#         if i > 0 and nums[i] == nums[i-1]:
#             continue
        
#         while l < r:
#             total = nums[i] + nums[l] + nums[r]
            
#             if total > 0:
#                 r -= 1
#             elif total < 0:
#                 l += 1
#             else:
#                 triplet = [nums[i], nums[l], nums[r]]
#                 answer.append(triplet)
#                 while l < r and nums[l] == triplet[1]:
#                     l += 1
                
#                 while l < r and nums[r] == triplet[2]:
#                     r -= 1
#     return answer
    



def threesum(nums):
    
    nums.sort()
    answer = []
    # count = 0
    for i in range(len(nums) -2 ):
        l = i+1
        r = len(nums) - 1
        if nums[i] == 0:
            break
        while l < r:
            total =  nums[i] + nums[l] + nums[r]
            # count += 1
            # print(f"while loop {count}")
            if total > 0:
                r -= 1
            elif total < 0:
                l += 1
            else:
                triplet = [nums[i], nums[l], nums[r]]
                answer.append(triplet)
                
                while l < r and nums[l] == triplet[1]:
                    l += 1
                while l < r and nums[r] == triplet[2]:
                    r -= 1
    return answer
print(threesum([-2, 0, -1, -4, -1, 3, 5]))