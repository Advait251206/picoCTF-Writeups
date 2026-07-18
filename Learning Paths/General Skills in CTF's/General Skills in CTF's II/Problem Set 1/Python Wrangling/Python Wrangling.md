# picoCTF Writeup: Python Wrangling

**Author:** Advait Kawale  
**Event:** picoCTF 2021  
**Difficulty:** Medium  
**Challenge Author:** syreal  
**Learning Path:** General Skills in CTFs II  
**Problem Set:** 1

## Problem Description
Python scripts are invoked kind of like programs in the Terminal...

Can you run `ende.py` using `password.txt` to get `flag.txt.en`?

[Download ende.py](ende.py)  
[Download password.txt](password.txt)  
[Download flag.txt.en](flag.txt.en)  

## Solution
The challenge provides us with three files:
- `ende.py`: A Python script that encrypts or decrypts files.
- `password.txt`: A text file containing the password needed for decryption.
- `flag.txt.en`: The encrypted flag file.

We can view the usage of the script by passing the `-h` (help) flag:
```bash
python ende.py -h
```
This tells us that to decrypt a file, we should use `-d`.

First, let's look at the password inside `password.txt`. You can open the file or use a terminal command to print it:
**Linux / macOS:**
```bash
cat password.txt
```
**Windows (PowerShell):**
```powershell
type password.txt
```

Now, we can run the script to decrypt our flag file. It will prompt you for the password:
```bash
python ende.py -d flag.txt.en
```
*When prompted, paste the password you got from `password.txt`!*

Alternatively, looking at the source code of `ende.py`, we can see it accepts the password as a third argument, allowing us to decrypt the flag in a single command without the interactive prompt:

**Linux / macOS:**
```bash
python ende.py -d flag.txt.en $(cat password.txt)
```
**Windows (PowerShell):**
```powershell
python ende.py -d flag.txt.en (Get-Content password.txt)
```

*(Note: The Python script relies on the `cryptography` module. If you get a `ModuleNotFoundError`, you can install it using `pip install cryptography`, or simply run these commands within the picoCTF webshell where the environment is already set up for you).*

Running this successfully will print out your decrypted flag!

## Flag
`picoCTF{4p0110_1n_7h3_h0us3_9c5f9bcf}`
