def lengthOfLongestSubstring(s: str) -> int:
        sub = 0
        temp_sub = ''
        idx_count = 0
        len_s = len(s)
        B = dict()
        # for i, c in enumerate(s):
        #     # if s[i] in temp_sub:
        #     if c in temp_sub:
        #         idx = temp_sub.find(c)
        #         # print(f"idx is {idx}")
        #         sub = max(len(temp_sub), sub)
        #         # print(f"s[idx+1] is: {s[idx+1]}")
        #         temp_sub = s[idx_count+1:i+1]
        #         idx_count += idx
        #         # print(f"temp_sub is {temp_sub}")
        #         # temp_sub = s[i]
        #     else:
        #         temp_sub += s[i].
        for i, c in enumerate(s):
            if c in temp_sub:
                
                sub = max(len(temp_sub), sub)
                temp_sub = s[B[c]+1:i+1]
                B[c] = i
            else:
                temp_sub += c
                B[c] = i
                
        return max(sub, len(temp_sub))
# 
# another solution

def maxsubstring(s):
    seen = {}
    l = 0
    length = 0
    
    for a in range(len(s)):
        char = s[a]
        if char in seen and seen[char] >= l:
            l = seen[char] + 1
        else:
            length = max(length, a-l+1)
        seen[char] = a
    return length 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        l = 0
        length = 0
        for r in range(len(s)):
            char = s[r]
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                length = max(length, r - l + 1)
            seen[char] = r

        return length

# abcabcbb
# A = lengthOfLongestSubstring("cdd")
# print(A)

def isValid(s: str) -> bool:
    status = False
    str_list = list()
    for ch in range(len(s)):
        if s[ch] in ['(', '[', '{']:
            str_list.append(s[ch])
        else:
            if len(str_list) == 0:
                return False
            a = str_list.pop()
            if a == '(' and s[ch] == ')':
                print("under if")
                status = True
            elif a == '[' and s[ch] == ']':
                status = True
                print("under elif 1")
            elif a == '{' and s[ch] == '}':
                status = True
                print("under elif 2")
            else:
                print("under else")
                status = False
    return status