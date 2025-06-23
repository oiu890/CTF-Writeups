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

Thus, I copied each part into its own cell in a jupyter notebook for easier debugging.
[notebook](solve.ipynb)




