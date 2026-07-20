# picoCTF Writeup: Assembly Arithmetic

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Trivial  
**Challenge Author:** picoCTF  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Intro to assembly

## Problem Description
Arithmetic in assembly is a little different. Both operands are used in the operation, as expected, but the result of the operation is stored in the first operand, wiping away its original contents.

The next problem introduces the `imul` and `add` instructions. `imul` is multiplication, the operands are multiplied together and the result is stored in the first operand. `add` is addition, the operands are added together and the result is stored in the first operand.

## Solution
This is an informational checkpoint preparing us for some math operations in upcoming assembly challenges. 

It explains two critical things to remember about x86 assembly arithmetic:
1. **Destructive operations:** In an instruction like `add eax, 5`, the operation is equivalent to `eax = eax + 5`. The original value of `eax` is overwritten by the result of the addition. 
2. **Left-to-Right Destination:** The destination register or memory location is always the *first* operand on the left side of the comma.
   - `add a, b` -> `a = a + b`
   - `imul a, b` -> `a = a * b`

Since this is purely an introductory checkpoint, there are no files to download or code to execute. Simply click the **Mark Complete** button on the picoCTF learning path to proceed!

## Flag
*No flag required - just mark as complete.*
