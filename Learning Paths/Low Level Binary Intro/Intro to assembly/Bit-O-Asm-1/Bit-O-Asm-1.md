# picoCTF Writeup: Bit-O-Asm-1

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Medium  
**Challenge Author:** LT 'syreal' Jones  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Intro to assembly

## Problem Description
The `mov` instruction moves the second operand into the first operand.

Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.

Download the assembly dump [here](disassembler-dump0_a.txt).

## Solution
We are given a text file containing a small x86-64 assembly dump:

```assembly
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x4],edi
<+11>:    mov    QWORD PTR [rbp-0x10],rsi
<+15>:    mov    eax,0x30
<+20>:    pop    rbp
<+21>:    ret
```

The challenge asks us to find the contents of the `eax` register when the program returns. Looking through the instructions, we can ignore the function prologue (`endbr64`, `push rbp`, `mov rbp, rsp`) and the stack setup operations (`[rbp-0x4]` and `[rbp-0x10]`).

The crucial instruction is at `<+15>`:
`mov eax,0x30`

This instruction moves the hexadecimal value `0x30` into the `eax` register.

The challenge asks for the value in decimal base. We can convert `0x30` (hexadecimal) to decimal:
`0x30` = (3 * 16) + (0 * 1) = 48

We wrap the decimal value 48 in the flag format to solve the challenge.

## Flag
`picoCTF{48}`
