# picoCTF Writeup: Static analysis of debugger0_b

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Trivial  
**Challenge Author:** picoCTF  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Intro to Debuggers

## Problem Description
Download the artifact from the next challenge.
Disassemble it like you did for the previous challenge.
Statically analyze it; read it, try to understand what is happening.
Notice how the code jumps backwards! The same block of code is executed multiple times. This is how a loop looks in assembly language. To statically figure out what is in `eax` at `main+56` we’d have to precisely calculate how many times this loop runs. This is possible, but in this case, we can easily set a breakpoint to pause program execution after the loop. To set a breakpoint and examine `eax`, follow these steps:

- `(gdb) break *main+59` This sets a breakpoint at the instruction immediately after the one in question. This guarantees that the instruction in question has actually been executed.
- `(gdb) run` This lets the program run until it tries to execute the instruction at our breakpoint.
- `(gdb) info registers eax` This prints out our answer in hexadecimal and decimal.

Mark Complete

## Solution
This is an informational checkpoint preparing you for the next challenge by introducing **loops** in assembly and demonstrating how dynamic analysis simplifies things. 

While static analysis involves manually calculating the loop iterations (which is error-prone and time-consuming), dynamic analysis lets the computer do the hard work. 

By setting a breakpoint *right after* the loop finishes (`break *main+59`), running the program (`run`), and dumping the register state (`info registers eax`), you effortlessly capture the final calculated value!

Since this is purely an introductory checkpoint, there are no files to download or flags to find. Simply click the **Mark Complete** button on the picoCTF learning path to proceed!

## Flag
*No flag required - just mark as complete.*
