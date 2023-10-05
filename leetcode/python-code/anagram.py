def check_anagram(s, t):
    t_freq = dict()
    s_freq = dict()
    
    for ch in s:
        s_freq[ch] = s_freq.get(ch, 0) + 1
    for ch1 in t:
        t_freq[ch1] = t_freq.get(ch1, 0) + 1
        
    return t_freq == s_freq

print(check_anagram('night', 'thing'))