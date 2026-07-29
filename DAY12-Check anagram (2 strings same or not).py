ANAGRAM-
Two strings are called anagrams if they contain the same characters with the same frequency, but the order can be different.
Examples--listen and silent
  CODE--

word1=listen
word2=silent

if sorted(word1)==sorted(word2):
      print("Anagram")
else:
      print("Not Anagram")
  
