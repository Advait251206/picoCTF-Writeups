# picoCTF Writeup: Picker II solution

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Trivial  
**Challenge Author:** picoCTF  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Interlude

## Problem Description
At first, we can try some dynamic analysis. Does our old solution still work? (Probably not, but it's always worth checking, maybe we solved the previous problem in an unexpected way?) Entering ‘win’ now gets us ‘Illegal Input’ instead of the flag in hexadecimal. So how elaborate is this filter? Static analysis can answer that for us. If we look at `picker-II.py`, all the way at the bottom, we see that `filter` is only checking for `win` which actually leaves our options fairly open.

So we can’t directly invoke the `win` function, but we can still do the things that the `win` function does, as long as the substring `win` is not present in those things. The first line in `win`, `open('flag.txt', 'r').read()` is what we want, but we want to print the result, not store it in a variable. So now we have `print(open('flag.txt', 'r').read())` This works, but it can be made a little cleaner by commenting out the rest of the line and thus getting rid of the calling error. Our final exploit is: `print(open('flag.txt', 'r').read())#` The hashtag makes the parentheses tagged on to the user input a comment, instead of code.

## Solution
This is an informational checkpoint reviewing the official solution for the **Picker II** challenge.

It validates the exact logic we used in our exploit! The intended exploit simply replicates the functionality of the blocked `win()` function:
```python
print(open('flag.txt', 'r').read())#
```

The script appends `()` to everything, but by adding the `#` (comment) character at the end of our payload, Python ignores the trailing parenthesis. Our `or exit` trick in the previous writeup also worked similarly to handle the `()` syntax correctly!

Since this is purely a debrief/review checkpoint, there are no files to download or flags to find. Simply click the **Mark Complete** button on the picoCTF learning path to wrap up this challenge!

## Flag
*No flag required - just mark as complete.*
