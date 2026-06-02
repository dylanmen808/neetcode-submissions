class Solution:

    def encode(self, strs: List[str]) -> str:
        #we want the output (result) to be a single string
        result = ""
        #go string by string through the input and append the encoded string (s)
        for s in strs:
            #we want the length of each string but need it to be a string not an integer
            #with the delimiter of choosing followed by the actual string
            result += str(len(s)) + "$" + s
        return result


    def decode(self, s: str) -> List[str]:
        #here our output needs to be a list with a pointer (i) to tell the position were at in the input string
        result, i = [], 0
        
        #go through character by character (decoding each string)
        while i < len(s):
            #create another pointer to find the delimter we have (the end of the integer)
            j = i
            #increment j by 1 for each character that isnt our delimiter
            while s[j] != "$":
                j += 1
            #we get our length which tells us how many character we need to read after j to get every character of the string 
            length = int(s[i:j])
            #this gives us the entire string and we need to append it and send it to our list of strings output
            result.append(s[j + 1 : j + 1 + length])
            #the end of the beggining of the string to the beginning of the next string, to update our j pointer for each iteration of the loop 
            i = j + 1 + length 
        return result
          