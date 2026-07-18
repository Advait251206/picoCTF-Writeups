# picoCTF Writeup: strings it

**Author:** Advait Kawale  
**Event:** picoCTF 2019  
**Difficulty:** Easy  
**Challenge Author:** Sanjay C/Danny Tunitis  
**Learning Path:** General Skills in CTFs II  
**Problem Set:** 3

## Problem Description
Can you find the flag in [file](strings) without running it?

## Solution
The challenge gives us a binary file named `strings` and asks us to find the flag inside it without actually running the file.

We can achieve this by simply searching the binary for the prefix `picoCTF`. 

**Linux / macOS:**
Use the `strings` command to extract readable text, and `grep` to filter for the flag:
```bash
strings strings | grep picoCTF
```

**Windows (PowerShell):**
We can use `Select-String` directly on the binary file, which will scan for the text just like `grep`:
```powershell
Select-String "picoCTF" strings
```

Running this command reveals the hidden flag in the binary's data!

## Flag
`picoCTF{5tRIng5_1T_dB2CEA76}`
