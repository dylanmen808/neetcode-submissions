class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #create the result output array 
        #give each initial position a value of 1 * length of the array
        res = [1] * (len(nums))

        #intialize prefix
        prefix = 1
        #go through every position of the input array
        for i in range(len(nums)):
            #take each prefix and place it in our output array at position [i]
            res[i] = prefix
            #take the input array value * what the prefix is
            prefix *= nums[i]

        #start the postfix process
        postfix = 1
        #start at the end of the input array,( - 1, - 1, - 1), 
        for i in range(len(nums) - 1, - 1, - 1):
            #multiply the prefix to the postfix to not override the values in the prefix
            res[i] *= postfix 
            #multiply postfix to each value in the array nums
            postfix *= nums[i]
        return res
