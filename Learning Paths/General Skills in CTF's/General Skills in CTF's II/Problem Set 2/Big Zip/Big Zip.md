# picoCTF Writeup: Big Zip

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Easy  
**Challenge Author:** LT 'syreal' Jones  
**Learning Path:** General Skills in CTFs II  
**Problem Set:** 2

## Problem Description
Unzip this archive and find the flag.

[Download zip file](big-zip-files.zip)

## Solution
This challenge requires us to find the flag hidden inside an extremely large zip file containing hundreds of files and folders.

1. **Unzip the Archive:**
   First, you need to extract the zip file:
   - **Linux / macOS:** `unzip big-zip-files.zip`
   - **Windows (PowerShell):** `Expand-Archive big-zip-files.zip`

2. **Recursive Search for the Flag:**
   Instead of opening each file individually, we can recursively search through all the extracted files for the text string `picoCTF`.

   **Linux / macOS:**
   Use the `grep` command with the `-r` (recursive) flag:
   ```bash
   grep -r "picoCTF" big-zip-files/
   ```

   **Windows (PowerShell):**
   Use `Get-ChildItem` to get all files, and pipe them into `Select-String`:
   ```powershell
   Get-ChildItem -Recurse -File .\big-zip-files | Select-String "picoCTF{"
   ```

Executing either command will scan through every single file in the directory tree and output the line containing our flag!

## Flag
`picoCTF{gr3p_15_m4g1c_ef8790dc}`
