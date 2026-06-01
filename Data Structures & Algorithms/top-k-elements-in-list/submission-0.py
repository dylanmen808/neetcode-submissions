class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create hashmap/set to store the count of each value
        k_frequent_elements = {}

        #create another hashmap/set for the copy of the input array 
        #set the range to the len of nums + 1
        freq = [[]for i in range(len(nums) + 1)]

        #for loop to go through each int in the input array and count each time it appears
        for n in nums :
            #count the occurences of each int and add 1 for everytime it appears
            #return 0 if it hasn't been counted yet
            k_frequent_elements[n] = 1 + k_frequent_elements.get(n, 0) 
        #go through each value counted 
        #count.items() will return each key value pair
        for n, c in k_frequent_elements.items():
            #in the freq array we want to append each value (n) occurs (n) amount of times
            freq[c].append(n)
        #output array
        res = []
        #return the result in descending order
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res




     

        