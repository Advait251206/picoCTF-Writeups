# picoCTF Writeup: Calling functions

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Trivial  
**Challenge Author:** picoCTF  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Intro to Debuggers

## Problem Description
A feature that assembly languages do have is the idea of a function. A function is a grouping of code that can be called from other places in the program. A function can have input and output, but we won’t go into that right now. The `call` instruction is like an unconditional jump in that it transfers execution to the address provided. When the function is finished, execution resumes at the instruction right after the `call`, or at least, that’s the intention! Later we will see how we can subvert that convention and call whatever code we want.

## Solution
This is an informational checkpoint challenge introducing the concept of **functions** and the `call` instruction in assembly language.

In high-level languages like C or Python, you call a function by its name (e.g., `my_function()`). In assembly language, this is implemented using the `call` instruction followed by a memory address (or a label representing that address). 

Key takeaways:
1. **The `call` instruction:** This instruction does two things:
   - It pushes the return address (the address of the instruction immediately following the `call`) onto the stack.
   - It jumps to the target address of the function, transferring execution flow.
2. **The `ret` instruction:** When a function completes its execution, it uses the `ret` (return) instruction. This pops the return address off the stack and jumps back to it, resuming execution right where the program left off.
3. **Exploitation Hint:** The challenge hints at memory corruption vulnerabilities (like buffer overflows). If an attacker can overwrite the return address stored on the stack before the `ret` instruction executes, they can trick the program into jumping to malicious code instead of the intended location!

Since this is purely an introductory checkpoint, there are no files to download or flags to find. Simply click the **Mark Complete** button on the picoCTF learning path to proceed!

## Flag
*No flag required - just mark as complete.*
