# picoCTF Writeup: Picker III solution

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Trivial  
**Challenge Author:** picoCTF  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Interlude

## Problem Description
Picker III also tries to fix the issues of its predecessor. It locks down the user, for sure, but still leaves a gap that can be exploited. This vulnerability is mostly leveraged through “write_variable”.

The programmer has limited the functions we can call to a table of names. However, this table is just a variable and in the table is included a function called “write_variable”. We’ll actually use “read_variable” first, to get a string of the table. In the source code, the table is formatted specially by escaping the newline present at the end of each line. Calling read_variable will give us a string we can modify and give back to the program through write_variable. We must be careful to maintain the length of the string as given while still inserting our win function into the table. The check_table function makes sure that the length of the string is correct per the size of each entry and how many entries are expected. Be careful copying and pasting the result of read_variable as there are trailing spaces you want, but you don’t want to copy the newline of the line. Lastly, don’t forget to enclose your new table in quotes, so the text is interpreted as a string.

## Solution
This is an informational checkpoint reviewing the official solution for the **Picker III** challenge.

It validates the exact logic we used in our exploit! The intended vulnerability was indeed the poorly sanitized `write_variable` function, which allows us to overwrite the `func_table` global variable. 

The official solution suggests doing this manually:
1. Using `read_variable` to print out the exact string value of `func_table`.
2. Copying that string, manually replacing the first entry with `win`, and ensuring all the trailing spaces are perfectly preserved so the length remains exactly 128 characters.
3. Using `write_variable` and pasting that massive string back in.

Our approach was a bit more "programmatic" and elegant: we just told Python to calculate the spacing for us by sending `'win' + ' ' * 125`, which evaluated to the exact 128-character padded string required to bypass `check_table()`. Both approaches achieve the exact same memory corruption effect!

Since this is purely a debrief/review checkpoint, there are no files to download or flags to find. Simply click the **Mark Complete** button on the picoCTF learning path to wrap up this challenge!

## Flag
*No flag required - just mark as complete.*
