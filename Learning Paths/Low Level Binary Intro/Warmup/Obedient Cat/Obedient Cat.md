# picoCTF Writeup: Obedient Cat

**Author:** Advait Kawale  
**Event:** picoCTF 2021  
**Difficulty:** Easy  
**Challenge Author:** syreal  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Warmup

## Problem Description
This file has a flag in plain sight (aka "in-the-clear").

## Solution
The challenge provides us with a file named `flag` that contains the flag in plain text.

**Linux / macOS:**
You can read the contents of the file directly in your terminal using the `cat` command:
```bash
cat flag
```

**Windows (PowerShell):**
In PowerShell, the native equivalent to read a file's content is `Get-Content` (or simply using the `type` alias):
```powershell
Get-Content flag
```

Running either of these commands will output the flag directly to your console!

## Flag
`picoCTF{s4n1ty_v3r1f13d_9b8fa0bc}`
