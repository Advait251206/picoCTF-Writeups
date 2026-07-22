# picoCTF Writeup: GDB baby step 4

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Medium  
**Challenge Author:** LT 'syreal' Jones  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Intro to Debuggers

## Problem Description
`main` calls a function that multiplies `eax` by a constant. The flag for this challenge is that constant in decimal base. If the constant you find is `0x1000`, the flag will be `picoCTF{4096}`.

Debug [this](debugger0_d).

## Solution
The goal is to determine the constant by which a function multiplies the `eax` register. We can find this out using both dynamic and static analysis.

### Linux / macOS (Dynamic Analysis)
If you have access to GDB, you can run the binary and inspect the execution:

1. Make the binary executable:
   ```bash
   chmod +x debugger0_d
   ```
2. Open it in GDB:
   ```bash
   gdb ./debugger0_d
   ```
3. Disassemble `main` to find the function call:
   ```bash
   (gdb) disassemble main
   ```
   You will see an instruction calling another function, likely named something like `<func1>`:
   `0x0000000000401142 <+38>:    call   0x401106 <func1>`
4. Disassemble that function to look for the multiplication instruction:
   ```bash
   (gdb) disassemble func1
   ```
   Inside this function, you will see an `imul` (integer multiplication) instruction:
   `0x0000000000401114 <+14>:    imul   $0x3269,%eax,%eax`
   
This instruction multiplies the value in `eax` by the constant `$0x3269` and stores the result back in `eax`.

### Windows (Native, No WSL - Static Analysis)
We can statically analyze the binary using a disassembler like `objdump` without needing to execute it:

1. Disassemble the `main` function first:
   ```powershell
   objdump -d debugger0_d | Select-String -Pattern "<main>:" -Context 0, 15
   ```
   Looking at the output, we see a function call at instruction `401142`:
   ```assembly
    40113d:     8b 45 fc                mov    -0x4(%rbp),%eax
    401140:     89 c7                   mov    %eax,%edi
    401142:     e8 bf ff ff ff          call   401106 <func1>
   ```

2. Next, disassemble `<func1>` to see what it does:
   ```powershell
   objdump -d debugger0_d | Select-String -Pattern "<func1>:" -Context 0, 10
   ```
   The output shows:
   ```assembly
    401106:     f3 0f 1e fa             endbr64
    40110a:     55                      push   %rbp
    40110b:     48 89 e5                mov    %rsp,%rbp
    40110e:     89 7d fc                mov    %edi,-0x4(%rbp)
    401111:     8b 45 fc                mov    -0x4(%rbp),%eax
    401114:     69 c0 69 32 00 00       imul   $0x3269,%eax,%eax
   ```

The `imul` instruction tells us the multiplication constant is `0x3269`.

Converting the hex value `0x3269` to decimal:
`3 * 4096 + 2 * 256 + 6 * 16 + 9 = 12905`

## Flag
`picoCTF{12905}`
