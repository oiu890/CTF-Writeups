# Challenge Details
Challenge name: Snake Game  
Competition: LNC 5.0  
Category: Misc  
Difficulty: Medium  
Points: ???  
Solves: ???   
Author: benwoo1110  

# Challenge description
Just a simple snake game from the nokia days with a special fruit.

# Files
![snake_game](./snake_game)

# Solve
We are given a binary that lets you play a snake game when run. (the kind where you eat apples to increase your length/score)  
The goal of the game is to eat the Golden apple.

## Examining the code
As with most binaries, we can use a decompiler like Ghidra to generate C-like pseudocode for analysis.

Note I have renamed function/variable names for easier analysis.

### Main function
![main](/LNC%205.0/images/snake_main.png)
First we will be taking a look at this "main" function which starts the game.

"main" calls quite a few other functions to do stuff. By simply clicking around you should be able to figure out that the last function, "logic", is the one we have to use to find the flag.

### Logic function
![logic](/LNC%205.0/images/logic.png)
The logic function is quite long but if you read properly it calls 2 important functions, "make_gapple_and_key" and "decrypt".
The golden apple has a 1/100 chance of being created. The code then checks if you have eaten it and calls "decrypt", which uses the key to decrypt the flag.

### make_gapple_and_key
![gapple](/LNC%205.0/images/gapple.png)
The X and Y positions of the golden apple are determined by the rand() function. The X coord has range of 1-38, while the Y coord has a range of 1-18. "fill_key" is then called to create the key.

### fill_key
![key](/LNC%205.0/images/key.png)
The "fill_key" function tells us how the key is generated.
rand() is first seeded using the x_coord of the golden apple, then used to generate the first 5 characters of the key.
After that rand() is seeded again but this time using the y_coord of the golden apple. The last 5 characters of the key are then filled.

### decrypt
Now lets look at the "decrypt" function.
![decrypt](/LNC%205.0/images/decrypt.png)
We can see that a hardcoded array is being xored with the key that was created earlier. The code then prints the new array. However, as the key is different everytime, even if you win you might not be given the correct flag 😔

## Brute force
So how should we solve it?
Remember that the key is seeded using the X and Y coord of the golden apple. However, these coords have a small range of 38 and 18! This means there are only 684 possible keys.
We can simply brute force this :)

![code](./snake.py)

## Flag
LNC25{g0ld3n_a99le_appe4r3_r4nD0m1y}