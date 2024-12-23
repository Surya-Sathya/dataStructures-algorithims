class Solution:
    def evaluateALONE(self, s: str, knowledge: list[list[str]]) -> str:
        #Input is a string s, bracket pair = (key), never non-empty
        #knowledge = [[name, Null], [age, Null]]
        #You don't know all the actual keys, each key only appears once
        #R: (rat)iseatingrats, k = [["rat", "master"]] -> output string is: masteriseatingrats
        #E: 
        #V: Always have to be bracket pairs present? 
        #S: How many bracket pairs there are? Size of string? Size of knowledge array?

        #Brute Force ~ Bulid up the string as we're going
        #Linear sweep through the string, adding each char to an output string -> ""
            #a(rat), amaster
        #When we see an open bracket:
            #continue
            #key = ""
            #we will keep adding characters to this empty string UNTIl we reach closing bracket
            #Do a linear search for the KEY have just created -> Knowledge array
            #When we find associated index of key in k, add the associated value to our output string
            #Go back to adding each iteration
        

        #Stack
        #rat(rat)iseating
        #Linear sweep through the string, adding to output string:
            # stack = [r, a, t]
            # If we see CLOSING BRACKET
            
            #Do not add to the stack, pop off all the elements until we get to the associatd open bracket
                #add all the popped values to a string
                #simply search this string
                #find the value, add all these back to the stack
        
        #For each element in the stacl: add to res, we're done
        stack = []
        res = "" 
        #stack = [r, a, t, (, r, a, t]
        #s = rat(rat)iseating
        for char_idx in range(len(s)):
            if s[char_idx] != ")": stack.append(s[char_idx])

            #[r, a, t, (, r, a, t]
            #fk = tar(
            else:
                rev_found_key = ""
                while True:
                    #print(stack)
                    if len(rev_found_key) > 0:
                        if rev_found_key[-1] == "(": break
                    rev_found_key = rev_found_key + stack.pop()
                #print(rev_found_key)

                found_key = "" 
                for rev_char in range(len(rev_found_key)-2, -1, -1):
                    #print(rev_char)
                    found_key = found_key + rev_found_key[rev_char]

                found = False
                for key, value in knowledge:
                    #print(found_key, key, value)
                    if found_key == key:
                        for val_char in value:
                            stack.append(val_char)
                        found = True
                        break
                
                if found == False: stack.append("?")
        
        for output_char in stack:
            res = res + output_char
        
        return res
                

    def evaluateALONE_EDITING(self, s: str, knowledge: List[List[str]]) -> str:
        #Create Hashmap -> Key, Value pairs. O(K), where K is the length of the knowledge array
        #Time: O(k)
        #Space: O(k)
        hashmap = dict(knowledge)
        
        res = "" 
        for string_char in s:
            if string_char != ")": res += string_char

            else:
                rev_found_key = ""
                while True:
                    if len(rev_found_key) > 0:
                        if rev_found_key[-1] == "(": break
                    rev_found_key += res[-1]
                    res = res[:-1]

                found_key = rev_found_key[::-1][1:len(rev_found_key)] 

                if found_key in hashmap: res += hashmap[found_key]
                else: res += "?"
        
        return res
                
    def evaluateWITHSOLS(self, s: str, knowledge: List[List[str]]) -> str:
        #Create Hashmap -> Key, Value pairs. O(K), where K is the length of the knowledge array
        #Time: O(k)
        #Space: O(k)
        hashmap = dict(knowledge)
        res = "" 
        splitted_lst = s.split("(") #O(len(s)) complexity
        res += splitted_lst[0]

        #For the key string_split, we are only splitting PARTS of the main string. 
        #splitted list length is how many "(" are present, which is < len(s) -> O(#{ + len(s) + k) -> O(len(s) + K)
        for key_string in splitted_lst[1:]:
            found_key, rest = key_string.split(")")
            #print(key_string)
            res += hashmap.get(found_key, "?") + rest
    
        return res

        