# picoCTF Writeup: First Find

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Easy  
**Challenge Author:** LT 'syreal' Jones  
**Learning Path:** General Skills in CTFs II  
**Problem Set:** 2

## Problem Description
Unzip this archive and find the file named 'uber-secret.txt'

[Download zip file](files.zip)

## Solution
The challenge provides us with a zip file (`files.zip`) and asks us to locate a file named `uber-secret.txt` hidden within its extracted contents.

1. **Unzip the Archive:**
   First, you need to extract the zip file. You can do this by right-clicking it in your file explorer and selecting "Extract All", or you can use the command line:
   - **Linux / macOS:** `unzip files.zip`
   - **Windows (PowerShell):** `Expand-Archive files.zip`

2. **Find the Secret File:**
   The extracted folder has a very deep directory structure filled with decoy files. Instead of manually clicking through every folder, we can use a command to search for `uber-secret.txt` automatically.
   
   **Linux / macOS:**
   Use the `find` command to search the extracted directory:
   ```bash
   find . -name "uber-secret.txt"
   ```
   This will output the exact path to the file. You can then print its contents:
   ```bash
   cat ./path/to/uber-secret.txt
   ```

   **Windows (PowerShell):**
   Use `Get-ChildItem` to search recursively for the file:
   ```powershell
   Get-ChildItem -Recurse -Filter "uber-secret.txt"
   ```
   Once you see where it is, or if you just want to immediately read its contents in one go:
   ```powershell
   Get-ChildItem -Recurse -Filter "uber-secret.txt" | Get-Content
   ```

Running these commands will directly read the contents of `uber-secret.txt` and reveal the flag!

## Flag
`picoCTF{f1nd_15_f457_ab443fd1}`
