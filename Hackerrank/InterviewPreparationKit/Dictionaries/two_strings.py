
'''
https://www.hackerrank.com/challenges/two-strings/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
Two Strings
'''

# Solution 1
def twoStrings(s1, s2):
    # Write your code here
    set_s1 = set(s1)
    set_s2 = set(s2)
    if len(set_s1.intersection(set_s2)) > 0:
        return 'YES'
    return 'NO'


# Solution 2
def twoStrings2(s1, s2):
    return "YES" if set(s1) & set(s2) else "NO"


print(twoStrings2("he", "world"))
