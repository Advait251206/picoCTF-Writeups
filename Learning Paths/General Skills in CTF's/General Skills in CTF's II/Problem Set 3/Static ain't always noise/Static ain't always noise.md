# picoCTF Writeup: Static ain't always noise

**Author:** Advait Kawale  
**Event:** picoCTF 2021  
**Difficulty:** Easy  
**Challenge Author:** syreal  
**Learning Path:** General Skills in CTFs II  
**Problem Set:** 3

## Problem Description
Can you look at the data in this binary? The bash script might help!

[Download static](static)  
[Download ltdis.sh](ltdis.sh)

## Solution
The challenge provides us with a compiled binary (`static`) and a bash script (`ltdis.sh`). While the bash script uses `objdump` and `strings` to disassemble and extract text from the binary on Linux, we can also bypass it entirely and extract the flag directly using string analysis tools!

**Linux / macOS:**
If you have the bash script and are on a Linux environment, you can simply run it against the binary:
```bash
./ltdis.sh static
```
This will create two text files. Reading `static.ltdis.strings.txt` and piping it into `grep` will reveal the flag:
```bash
cat static.ltdis.strings.txt | grep picoCTF
```
Alternatively, you can just run `strings` directly on the binary:
```bash
strings static | grep picoCTF
```

**Windows (PowerShell):**
Since `ltdis.sh` relies on Linux utilities like `objdump`, you won't be able to run it directly on Windows without WSL. However, we can use PowerShell's equivalent of `strings` + `grep` directly on the binary file:
```powershell
Select-String "picoCTF" static
```
This will look through the binary file and extract the readable flag!

## Flag
`picoCTF{d15a5m_t34s3r_20335e41}`
