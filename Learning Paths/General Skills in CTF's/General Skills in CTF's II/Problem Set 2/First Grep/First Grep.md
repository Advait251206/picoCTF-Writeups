# picoCTF Writeup: First Grep

**Author:** Advait Kawale  
**Event:** picoCTF 2019  
**Difficulty:** Easy  
**Challenge Author:** Alex Fulton/Danny Tunitis  
**Learning Path:** General Skills in CTFs II  
**Problem Set:** 2

## Problem Description
Can you find the flag in the file? This would be really tedious to look through manually, something tells me there is a better way.

[Download file](file)

## Solution
This challenge introduces us to `grep` (or equivalent tools on Windows), which is incredibly useful for finding specific text inside a large file. The provided file is filled with random characters, making it virtually impossible to find the flag manually.

We can search for the flag pattern (`picoCTF`) directly from the terminal.

**Linux / macOS:**
Use the `grep` command to search the file:
```bash
grep "picoCTF" file
```

**Windows (PowerShell):**
Use the `Select-String` cmdlet, which is PowerShell's equivalent to grep:
```powershell
Select-String "picoCTF" file
```

Running either of these commands will instantly output the line containing our flag!

## Flag
`picoCTF{grep_is_good_to_find_things_01aE5e9d}`
