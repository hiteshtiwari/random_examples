def strStr(haystack, needle):
    lps = [0] * len(needle)
    pre = 0 
    for i in range(1, len(needle)):
        while (pre > 0 and needle[i] != needle[pre]):
            pre = lps[pre-1]
        if needle[pre] == needle[i]:
            pre += 1
            lps[i] = pre
            