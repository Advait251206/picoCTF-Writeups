# picoCTF Writeup: Assembly Pointers

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Trivial  
**Challenge Author:** picoCTF  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Intro to assembly

## Problem Description
A pointer, abbreviated “PTR” in the disassembly listing, is a number that is interpreted as an address to a location for storing a value. It points to another location in the program where a value is stored.

It’s like if you had a book where every letter was sequentially numbered from first to last. You could jump right to a letter by giving its number. This number is like a pointer in assembly programs, only instead of letters there is data and instructions at these addresses.

## Solution
This is an informational checkpoint introducing the concept of **Pointers** in assembly language. 

In x86 assembly (which we saw in the previous `Bit-O-Asm-1` challenge), you will frequently see instructions like `DWORD PTR [rbp-0x4]`. 
- `PTR` stands for Pointer.
- The brackets `[...]` mean "dereference", meaning we are looking at the *value stored at the address* inside the brackets, not the address itself.
- `DWORD` (Double Word, 32 bits) or `QWORD` (Quad Word, 64 bits) tells the processor how large the piece of data is that we are pointing to.

Understanding how pointers reference memory is crucial for reverse engineering, as local variables, function arguments, and arrays are all accessed via memory addresses (pointers).

Since this is purely an introductory checkpoint, there are no files to download or code to execute. Simply click the **Mark Complete** button on the picoCTF learning path to proceed!

## Flag
*No flag required - just mark as complete.*
