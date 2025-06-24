# Challenge Details
Challenge name: Messy Workplace 2  
Competition: SSMCTF 2025  
Category: Misc  
Difficulty: Hard  
Points: 496  
Solves: 42  
Author: Gr0undUp  

# Challenge Description
Here's the code to my flag, just that it's a little messy...

# Solve
Looking at the code, we can see a lot of weird indentation, as well as lines that are in the wrong order. We will have to fix them one by one.

I used a jupyter notebook for easier debugging [notebook](solve.ipynb)

We will solve this by
1. Finding the scrambled parts of the flag
2. Piecing together the lines of code that unscramble this flag

## Finding the scrambled parts of the flag
This is easy, we just have to search for strings. 
```python
scrambled = "rmmsycdssf0_35_03s}"
offsets, scrambled2 = [0, 4, 4, 0, -3, -4, -1, 3, 4, 2, -2], "4g7s\\_/p77]"
s = list("0135_kmprswy{")
flag += "SCFMST"
```
We will find 3 of those such strings, as well as what seems to be the flag prefix

## Piecing together the lines of code that unscramble this flag

### Part 1
Lets look at scrambled first.
```python
scrambled = "rmmsycdssf0_35_03s}"
evens = scrambled[9:]
odds = scrambled[:9]
```
I found these 2 lines by doing ctr + f and searching for "scrambled".

From this, we can deduce that the the "scrambled" string was split into 2 parts, called evens and odds. Lets look for these 2 parts in the code.

```python
if len(evens) > len(odds):
for o, e in zip(odds, evens):
result.append(evens[-1])
```
These are what I found, however, they are still jumbled. From these, we can see that there is another variable, called result.  
Searching for it:

```python
result = []
flag += "".join(result)
result.extend([e, o])
```

Now, we have everything we need.  
We can assume the logic is something like:
1. Split the string into 2 halves (evens,odds)
2. Iterate through them with zip
3. Extend the result list
4. If the length of evens is greater than odds, evens has an extra character that was not added to result during zip
5. Add that extra character
6. Join it together  

```python
scrambled = "rmmsycdssf0_35_03s}"
odds      = scrambled[:9]
evens     = scrambled[9:]
result = []
for o, e in zip(odds, evens):
    result.extend([e, o])           # add even, then odd
if len(evens) > len(odds):          # one extra even character
    result.append(evens[-1])
print("".join(result))
#fr0m_m3s5y_c0d3sss}
```
### Part 2
Now lets find everything related to scrambled2
```python
offsets, scrambled2 = [0, 4, 4, 0, -3, -4, -1, 3, 4, 2, -2], "4g7s\\_/p77]"
for i, c in enumerate(scrambled2):
offset = offsets[i]
decoded_char = chr(ord(c) - offset)
decoded_chars = []
decoded_chars.append(decoded_char)
flag += ''.join(decoded_chars)
```
I also found anything related to "offsets", which led me to find anything related to "decoded_char" and "decoded_chars"

We can assume the logic goes like this:
1. You have a list of offsets and scrambled string
2. Iterate through scrambled string and offsets simultaneously
3. Do decoded_char = chr(ord(c) - offset) and append this to the decoded_chars list
4. Join it together

```python
offsets, scrambled2 = [0, 4, 4, 0, -3, -4, -1, 3, 4, 2, -2], "4g7s\\_/p77]"
decoded_chars = []
for i,c in enumerate(scrambled2):
    offset = offsets[i]
    decoded_char = chr(ord(c) - offset)
    decoded_chars.append(decoded_char)
print("".join(decoded_chars))
#4c3s_c0m35_
```
### Part 3
Now lets find everything related to "s"

```python
s = list("0135_kmprswy{")
s[j], s[i] = s[i], s[j] 
```
This is all you can find merely searching for "s".

From this, we can deduce that s is unscrambled by swapping the positions of 2 characters each time, s[j] and s[i].  
Thus, lets look for a for loop that iterates through something and updates i and j each iteration.

```python
for j, i in reversed([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (0, 1), (2, 3), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (1, 2), (3, 4), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (2, 3), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (3, 4), (5, 6), (6, 7), (7, 8), (2, 3), (4, 5), (6, 7), (1, 2), (5, 6), (0, 1), (4, 5), (3, 4), (2, 3), (1, 2)])
```

Putting it together, we get
```python
s = list("0135_kmprswy{")
for j,i in reverse(swap_indices): #for readability I wrote it like this
    s[j],s[i] = s[i],s[j]
print("".join(s))
#{m3s5y_w0rkp1
```

There seem to be other parts in the code such as
```python
flag = flag[:6] + flag[-13:] + flag[25:-13] + flag[6:25] 
flag = flag[:i] + flag[-1] + flag[i:-1]
```
But they dont seem to serve any purpose now as we already have all 3 parts of the flag, and can put it together ourseleves.

## Flag
Putting everything we found together, we get
SSMCTF{m3s5y_w0rkp14c3s_c0m35_fr0m_m3s5y_c0d3sss}




