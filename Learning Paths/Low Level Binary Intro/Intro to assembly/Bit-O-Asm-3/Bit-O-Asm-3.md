# picoCTF Writeup: Bit-O-Asm-3

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Medium  
**Challenge Author:** LT 'syreal' Jones  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Intro to assembly

## Problem Description
Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.

Download the assembly dump [here](disassembler-dump0_c.txt).

## Solution
We are given another x86-64 assembly dump, which builds upon the arithmetic concepts we learned in the previous checkpoint:

```assembly
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0xc],0x9fe1a
<+22>:    mov    DWORD PTR [rbp-0x8],0x4
<+29>:    mov    eax,DWORD PTR [rbp-0xc]
<+32>:    imul   eax,DWORD PTR [rbp-0x8]
<+36>:    add    eax,0x1f5
<+41>:    mov    DWORD PTR [rbp-0x4],eax
<+44>:    mov    eax,DWORD PTR [rbp-0x4]
<+47>:    pop    rbp
<+48>:    ret
```

Let's trace the execution step-by-step, focusing on the instructions that affect the `eax` register:

1. **`<+15> mov DWORD PTR [rbp-0xc],0x9fe1a`**
   - The value `0x9fe1a` (654874 in decimal) is stored in the local variable at `[rbp-0xc]`.
2. **`<+22> mov DWORD PTR [rbp-0x8],0x4`**
   - The value `0x4` (4 in decimal) is stored in the local variable at `[rbp-0x8]`.
3. **`<+29> mov eax,DWORD PTR [rbp-0xc]`**
   - The value `0x9fe1a` is loaded into the `eax` register.
4. **`<+32> imul eax,DWORD PTR [rbp-0x8]`**
   - The `eax` register is multiplied by the value at `[rbp-0x8]` (which is `0x4`).
   - `eax` = `0x9fe1a` * `0x4` = `0x27F868` (2619496 in decimal).
5. **`<+36> add eax,0x1f5`**
   - The value `0x1f5` (501 in decimal) is added to `eax`.
   - `eax` = `0x27F868` + `0x1f5` = `0x27FA5D`.
6. **`<+41> mov DWORD PTR [rbp-0x4],eax`**
   - The result (`0x27FA5D`) is temporarily stored in the local variable at `[rbp-0x4]`.
7. **`<+44> mov eax,DWORD PTR [rbp-0x4]`**
   - The result is moved right back into `eax` (this is typical compiler behavior for preparing a return value).

The final value in `eax` is `0x27FA5D`. Let's convert this to decimal:
- `2 * 16^5` = 2097152
- `7 * 16^4` = 458752
- `15 (F) * 16^3` = 61440
- `10 (A) * 16^2` = 2560
- `5 * 16^1` = 80
- `13 (D) * 16^0` = 13

Summing these up: 2097152 + 458752 + 61440 + 2560 + 80 + 13 = **2619997**.

We wrap the decimal value in the picoCTF flag format to solve the challenge.

## Flag
`picoCTF{2619997}`
