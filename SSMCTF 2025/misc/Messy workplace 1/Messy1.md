# Challenge Details
Challenge name: Messy Workplace 1  
Competition: SSMCTF 2025  
Category: Misc  
Difficulty: Medium  
Points: 250  
Solves: 63  
Author: Gr0undUp  

# Challenge Description
My workplace is a mess! What did I do???

# Solve
We are given a file flag.py  
Trying to run the file, we get no output

```python
scrambled = "_dwe35rse0_psu"
....
scrambled, swaps = "3_hoeeP7e_em_e1}", [(0, 5), (1, 5), (2, 8), (3, 8), (4, 10), (5, 11), (6, 7), (7, 11), (8, 13), (9, 13), (10, 14), (11, 13), (12, 2), (13, 2), (14, 2)]
...
scrambled, order = "SSStMnCeT3Fm{0c", [0, 14, 1, 13, 2, 12, 3, 11, 4, 10, 5, 9, 6, 8, 7]
...
```

Looking at the code, I noticed that the flag was made up of 3 scrambled parts.

However, it appears that the code that was used to **unscramble** them has issues.

Thus, I copied each part into its own cell in a jupyter notebook for easier debugging: 
[notebook](solve.ipynb)

## Part 1
```python
scrambled = "_dwe35rse0_psu"
result = [''] * len(scrambled)
front = 0
back = len(scrambled) - 1
back += front
for i, c in enumerate(scrambled):
    if i % 2 == 0:
        result[front] = c
        front += 1
        back += 1
    elif i + 5 == i:
        back, front = front, back
    else:
        result[back] = c
        back -= 1
```
Looking at the code, it appears that it is trying to append characters to the **front** if the index is positive, or the **back** if it is not.

However, there are some unnecessary/weird lines.

1. back += front, but front is 0?
2. why is there a check for i + 5 == i 🤨🤨
3. After appending to the front for even indexes, why is it incrementing back += 1?

Commenting out these lines will correct the code 

```python 
flag = ""
scrambled = "_dwe35rse0_psu"
result = [''] * len(scrambled)
front = 0
back = len(scrambled) - 1
# back += front
for i, c in enumerate(scrambled):
    if i % 2 == 0:
        result[front] = c
        front += 1
        # back += 1
    # elif i + 5 == i:
    #     back, front = front, back
    else:
        result[back] = c
        back -= 1
flag += ''.join(result)
print(flag)
#_w3re_sup0s5ed
```

## Part 2
```python
scrambled, swaps = "3_hoeeP7e_em_e1}", [(0, 5), (1, 5), (2, 8), (3, 8), (4, 10), (5, 11), (6, 7), (7, 11), (8, 13), (9, 13), (10, 14), (11, 13), (12, 2), (13, 2), (14, 2)]
s = list(scrambled)
for i, j in reversed(swaps):
    i, j = 1, 1
    s[i], s[j] = s[j], s[i]
    s[i+1], s[j+1] = s[j], s[i]
```
The second part has a list of swaps that is being iterated through, then swapping the characters at each specified index.

However,
1. why does it set i,j = 1,1 in each iteration? This would just swap the current character with itself, which does nothing
2. why is it doing s[i+1], s[j+1] = s[j], s[i]? This part is weird and could lead to index out of bounds errors

Commenting them out:
```python
scrambled, swaps = "3_hoeeP7e_em_e1}", [(0, 5), (1, 5), (2, 8), (3, 8),
    (4,10), (5, 11), (6, 7), (7, 11), (8, 13), (9, 13), (10, 14), (11, 13), (12, 2), (13, 2), (14, 2)]
s = list(scrambled)
for i, j in reversed(swaps):
    #i, j = 1, len(s)
    s[i], s[j] = s[j], s[i]
    # s[i+1], s[j+1] = s[j], s[i]

print("".join(s))
#_7o_h31P_meeeee}
```

## Part 3
```python
scrambled, order = "SSStMnCeT3Fm{0c", [0, 14, 1, 13, 2, 12, 3, 11, 4, 10, 5, 9, 6, 8, 7]
original = [''] * len(scrambled)
original += ['SSMCTF']
for i, idx in enumerate(order):
    idx += 1
    original[idx] = scrambled[i]
flag += ''.join(original)
```
The third part appears to be trying to reorder the scrambled string based on a list of indexes.

However,
1. Why did it add ['SSMCTF'] to original?
2. The code does for i,idx in enumerate(order), it then increments idx += 1.
 The enumerate function is already **auto incrementing** idx, like how i is auto incremented in a for...range loop

Thinking back now I could have just commented out those 2 lines and it would have worked

```python
scrambled, order = "SSStMnCeT3Fm{0c", [0, 14, 1, 13, 2, 12, 3, 11, 4, 10, 5, 9, 6, 8, 7]
original = [''] * len(scrambled)
# original += ['SSMCTF']
for i, idx in enumerate(order):
    # idx += 1
    original[idx] = scrambled[i]
print("".join(original))
#SSMCTF{c0m3entS
```
Instead I was looking at what the unscrambler wanted to do at a higher level and used replaced enumerate with zip to iterate through both the string and the order list :)

```python
scrambled, order = "SSStMnCeT3Fm{0c", [0, 14, 1, 13, 2, 12, 3, 11, 4, 10, 5, 9, 6, 8, 7]
original = [''] * len(scrambled)
for char,dex in zip(scrambled,order):
    original[dex] = char
print("".join(original))
#SSMCTF{c0m3entS
```

## Flag
Combining the 3 parts together you get: SSMCTF{c0m3entS_w3re_sup0s5ed_7o_h31P_meeeee}




