class Solution:
    def queryString(self, s: str, n: int) -> bool:
        binary_n = []
        substrings_matched = 0
        valid_len_so_far = 0

        for num in range(1, n+1):
            binary_n.append(bin(num)[2:])
        
        print(f"These binary substrings: {binary_n} have to match to the substring in {s} in order to return True")

        for pattern in binary_n:
            pat_idx = 0

            for idx in range(len(s)):
                #print(f"Idx: {idx}, Looking for pattern: {pattern} with Idx: {pat_idx}")
                if s[idx] == pattern[pat_idx]:

                    for pat_char in range(len(pattern)):
                        if idx+pat_char == len(s): break

                        #print(f"Does {s[idx+pat_char]} equal {pattern[pat_char]}")
                        if s[idx+pat_char] != pattern[pat_char]:
                            break
                        else:
                            valid_len_so_far += 1
            
                    if valid_len_so_far == len(pattern): 
                        valid_len_so_far = 0 
                        substrings_matched += 1
                        break
                
                valid_len_so_far = 0

            #print(pattern, valid_len_so_far)
        
        return substrings_matched == n

instance = Solution()
print(instance.queryString("0110", 3))

#Time Complexity: 
    # O(n) to create binary_n array
    # n (loop through each pattern) * len(s) (loop through each character of string in worst case) * n (for each char in s, loop through pattern)
    # O(n^2 * len(s)) -> cubic

#Space Complexity:
    # O(n) for binary n array

#Memeory limit exceeded ~ Time complexity too high, too many recursive calls. We failed on n = 1000000000 (10^9). 