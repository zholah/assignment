# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(s, p):
    
    # [assignment] Add your code here
    
   if len(s) == len(p):
      return True
 
   s = sorted(s)
   p = sorted(p)
 
   return s == p

s = "stop"
p = "pots"
print(find_anagram(s, p))