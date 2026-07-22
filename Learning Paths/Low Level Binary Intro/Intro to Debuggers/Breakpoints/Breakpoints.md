# picoCTF Writeup: Breakpoints

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Trivial  
**Challenge Author:** picoCTF  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Intro to Debuggers

## Problem Description
Breakpoints are the core of debugging, a dynamic technique. You can set a breakpoint somewhere in code and when the computer goes to execute that statement, it will instead pause and wait for direction. We will use a breakpoint to jump over complicated code and examine the register directly.
Mark Complete

## Solution
This is an informational checkpoint challenge introducing the concept of breakpoints in debugging. 

Breakpoints allow us to pause the execution of a program right before a specific line of code or instruction executes. This is especially useful because:
1. **Skipping Complexity:** Instead of painstakingly analyzing thousands of lines of obfuscated code, you can set a breakpoint *after* the complex logic and simply look at what the result was.
2. **State Inspection:** Once the program pauses, you can freely examine the CPU registers (like `eax`, `rbp`, etc.), memory contents, and stack state at that exact moment.
3. **Execution Control:** In GDB, you can set a breakpoint at the `main` function (`break main` or `b main`) or at a specific memory address (`b *0x401000`). Once paused, you can use commands like `step` (step into) or `next` (step over) to execute instructions one by one.

Since this is purely an introductory checkpoint, there are no files to download or flags to find. Simply click the **Mark Complete** button on the picoCTF learning path to proceed!

## Flag
*No flag required - just mark as complete.*
