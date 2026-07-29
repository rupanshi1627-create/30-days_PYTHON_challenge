Example- apple
a : 1
p : 2
l : 1
e : 1
------------
code--

word=apple
frequency = {}

for ch in word:
  if ch in frequency:
    # Us character ka count 1 se badha do
        frequency[ch] = frequency[ch] + 1

    # Agar character pehli baar mila
    else:

        # Dictionary mein character ko add karo
        # Aur uska count 1 set kar do
        frequency[ch] = 1

# Poori dictionary print karo
print(frequency)
