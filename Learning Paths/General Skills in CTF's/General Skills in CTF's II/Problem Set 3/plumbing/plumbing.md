# picoCTF Writeup: plumbing

**Author:** Advait Kawale  
**Event:** picoCTF 2019  
**Difficulty:** Medium  
**Challenge Author:** Alex Fulton/Danny Tunitis  
**Learning Path:** General Skills in CTFs II  
**Problem Set:** 3

## Problem Description
Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to `fickle-tempest.picoctf.net 64379`.

## Solution
The challenge requires us to connect to a netcat server, which will spew out a massive amount of decoy text (thousands of lines). To find the flag, we just need to pipe the output into `grep` (or `Select-String` on Windows).

**Linux / macOS:**
Use the `nc` (netcat) command to connect to the server, and pipe (`|`) the output into `grep`:
```bash
nc fickle-tempest.picoctf.net 64379 | grep picoCTF
```

**Windows (PowerShell):**
If you have `ncat` installed, you can use it alongside `Select-String`:
```powershell
ncat fickle-tempest.picoctf.net 64379 | Select-String "picoCTF"
```
*Note: If you don't have ncat on Windows, you can easily use a tiny Python script using the `socket` library to pull the data and search for the flag using regex!*

Running this will instantly filter out all the fake lines and print the exact line containing the flag.

## Flag
`picoCTF{digital_plumb3r_11fffFE5}`
