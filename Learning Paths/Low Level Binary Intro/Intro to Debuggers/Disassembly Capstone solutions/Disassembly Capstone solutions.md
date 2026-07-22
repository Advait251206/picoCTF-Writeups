# picoCTF Writeup: Disassembly Capstone solutions

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Trivial  
**Challenge Author:** picoCTF  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Intro to Debuggers

## Problem Description
Probably the best known solution for this problem is setting a breakpoint after all the byte loads to memory, and then running this command in GDB `(gdb) x/s $rbp-0x30` after pausing at the breakpoint.

Our examine command is similar to what we used for GDB baby step 3, but it’s a little different. The address of course is different. But more importantly, instead of `4xb` we have `s`. `4xb` means examine 4 bytes at the address and display them as hexadecimal. `s` means interpret data as strings and display them as ASCII.

This solution cleanly displays the flag as an ASCII string as intended.

Another solution would be to grab the disassembly text and delete everything besides the hex numbers and then put those numbers in CyberChef.

Some disassemblers interpret hex in the ASCII range as text and include it as a comment next to the code. In that case, you might just transcribe the flag.

## Solution
This is an informational checkpoint reviewing the solutions for the **ASCII FTW** challenge.

It validates the exact approaches we documented in our writeup!
- **Dynamic Analysis:** We used GDB, set a breakpoint after the instructions, and used the `x/s` (examine string) command to print the memory as text.
- **Static Analysis:** We extracted the hex values manually and decoded them (just like using CyberChef).

Since this is purely a debrief/review checkpoint, there are no files to download or flags to find. Simply click the **Mark Complete** button on the picoCTF learning path to wrap up this section!

## Flag
*No flag required - just mark as complete.*
