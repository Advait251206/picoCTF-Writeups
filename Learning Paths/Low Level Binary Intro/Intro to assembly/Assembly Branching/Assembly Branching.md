# picoCTF Writeup: Assembly Branching

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Trivial  
**Challenge Author:** picoCTF  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Intro to assembly

## Problem Description
Just like Python, assembly programs are executed from top to bottom. Unlike Python, in assembly, you can jump to specific instructions, skipping everything in between them.

A `jmp` instruction is unconditional, it always jumps. In the disassembly listings given, you can tell where a jump goes by the function + offset given in angle brackets to the right of the address. The function the disassembly listings show is main and the offset to each line in the function is the first number on each line, also given in angle brackets.

We represent conditional jumps by `jcc`. There is no `jcc` instruction, “cc” stands for conditional and there are many different options available to the assembly programmer, see [this](http://unixwiz.net/techtips/x86-jumps.html). The `jcc` we see in the next problem is `jle`. This is “jump if less or equal to”, and semantically, we’re checking the first operand against the second. This check happens at the `cmp` instruction, which is “compare”.

## Solution
This is an informational checkpoint preparing us for control flow (branching) in assembly language. 

When you see a conditional jump like `jle` (Jump if Less than or Equal), it is almost always preceded by a `cmp` (Compare) instruction. 
1. **`cmp a, b`**: This instruction subtracts `b` from `a` internally and sets the processor's flags based on the result (e.g., if the result is negative, it sets the Sign Flag).
2. **`jle <address>`**: This instruction looks at the flags set by `cmp`. If the flags indicate that `a <= b`, the processor will jump to the specified `<address>`. If not, it just continues to the very next instruction.

These two instructions together form the assembly equivalent of an `if / else` statement or a `while` loop!

Since this is purely an introductory checkpoint, there are no files to download or code to execute. Simply click the **Mark Complete** button on the picoCTF learning path to proceed!

## Flag
*No flag required - just mark as complete.*
