# picoCTF Writeup: Bit-O-Asm-2

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Medium  
**Challenge Author:** LT 'syreal' Jones  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Intro to assembly

## Problem Description
Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.

Download the assembly dump [file](disassembler-dump0_b.txt).

## Solution
We are given another small x86-64 assembly dump:

```assembly
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    mov    eax,DWORD PTR [rbp-0x4]
<+25>:    pop    rbp
<+26>:    ret
```

This challenge builds upon the pointer concepts we saw in the previous informational checkpoint. We want to find what ends up in the `eax` register just before the function returns. Let's trace the final two operations:

1. **Instruction at `<+15>`**:
   `mov DWORD PTR [rbp-0x4],0x9fe1a`
   This instruction takes the hexadecimal value `0x9fe1a` and stores it into the memory location pointed to by `[rbp-0x4]` (a local variable on the stack). The `DWORD PTR` tells us it's storing a 32-bit (4-byte) value.

2. **Instruction at `<+22>`**:
   `mov eax,DWORD PTR [rbp-0x4]`
   This instruction takes the value stored at `[rbp-0x4]` and moves it into the `eax` register.

By following the flow, we can see that `eax` ultimately gets the value `0x9fe1a`.

The challenge asks for this value in decimal. Let's convert `0x9fe1a`:
- `9 * 16^4` = 589824
- `15 (f) * 16^3` = 61440
- `14 (e) * 16^2` = 3584
- `1 * 16^1` = 16
- `10 (a) * 16^0` = 10

Adding these together gives us `654874`. We wrap this decimal value in the picoCTF flag format!

## Flag
`picoCTF{654874}`
