# picoCTF Writeup: Disassembly Capstone

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Trivial  
**Challenge Author:** picoCTF  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Intro to Debuggers

## Problem Description
The next challenge combines a few of the concepts we’ve learned in this playlist so far into a single challenge. This problem can be solved manually, but I implore you to use a technique we have taught to get the answer more readily.

## Solution
This is an informational checkpoint preparing us for the final challenge in the **Intro to Debuggers** playlist!

Up to this point, we've learned how to:
1. Use GDB to load a binary (`gdb ./program`).
2. **Disassemble** functions (`disassemble main`).
3. Set **breakpoints** to pause execution right where we want (`break *main+offset`).
4. Read **registers** dynamically (`info registers eax`).
5. Read **memory** dynamically (`x/4xb $rbp-0x4`).
6. Recognize **Little Endian** byte ordering.
7. Understand function calls (`call` and `ret`) and the stack layout.
8. Perform **Static Analysis** using tools like `objdump` when dynamic execution isn't possible or necessary.

For the upcoming capstone challenge, the text hints that while we *could* trace all the instructions manually on paper, it's far easier and less error-prone to use a dynamic debugger (like GDB) to let the computer do the hard work for us.

Since this is an introductory checkpoint, there are no files to download or flags to find. Simply click the **Mark Complete** button on the picoCTF learning path to proceed to the capstone!

## Flag
*No flag required - just mark as complete.*
