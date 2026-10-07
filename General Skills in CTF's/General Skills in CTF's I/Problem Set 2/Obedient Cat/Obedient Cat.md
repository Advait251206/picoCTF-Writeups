# Obedient Cat Writeup
*Author: Advait Kawale*

## 1. Challenge Overview
- **Name:** Obedient Cat
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** syreal
- **Event:** picoCTF 2021
- **Description:** This file has a flag in plain sight (aka "in-the-clear"). [flag](./flag)
- **Flag Format:** `academy{...}`
- **Repository File Path:** [`./flag`](./flag) (`General Skills in CTF's/General Skills in CTF's I/Problem Set 2/Obedient Cat/flag`)
- **Date and Time of Completion:** 2026-10-07 09:37:00+05:30

---

## 2. Initial Triage & File Inspection

The title of the challenge—**"Obedient Cat"**—is a direct linguistic hint referencing the standard Unix utility `cat` (short for *concatenate*). The description states that the target flag is stored "in plain sight" (in plaintext without encryption, obfuscation, or compression).

### 🔬 Standard Stream File Processing Model

When reading an unencrypted text file from disk in a Unix-like environment, the `cat` binary opens the target file descriptor and streams raw byte buffers directly to standard output (`stdout`):

```text
Storage Disk: [./flag] (34 bytes ASCII Text)
       │
       ▼  (Kernel VFS: read() syscall)
┌──────────────────────────────────────────────┐
│       cat Process (Unix Core Utilities)       │
└──────────────────────────────────────────────┘
       │
       ▼  (File Descriptor 1: stdout stream)
Terminal Display:
academy{s4n1ty_v3r1f13d_61ddac22}
```

### Initial File Characteristics:
- **File Name:** `flag` (no extension)
- **File Size:** 34 bytes
- **MIME / Encoding:** `text/plain; charset=us-ascii`
- **Inspection Command:**
  ```bash
  file flag
  # Output: flag: ASCII text
  ```

---

## 3. Step-by-Step Solution

We can inspect and extract the contents of the file using multiple terminal workflows across Linux and Windows.

### Method 1: Native Linux / Bash `cat` Command (Intended Method)
Download or navigate to the file directory and invoke `cat`:

```bash
# Print file contents directly to standard output
cat flag
```

**Terminal Output:**
```text
academy{s4n1ty_v3r1f13d_61ddac22}
```

---

### Method 2: Windows PowerShell Commands
On Windows systems, PowerShell provides multiple native equivalents to read file contents:

```powershell
# Using PowerShell's Get-Content cmdlet (alias: gc, cat, type)
Get-Content ./flag

# Or using the native cmd 'type' command
type ./flag
```

**Terminal Output:**
```text
academy{s4n1ty_v3r1f13d_61ddac22}
```

---

### Method 3: Automated Reproducible Python Solver (`solve.py`)
To maintain a scriptable audit trail and ensure compatibility across any operating system, we created a Python solver script:

```python
#!/usr/bin/env python3
"""
Challenge: Obedient Cat
Author: Advait Kawale
Category: General Skills
"""
import os
import sys

def solve():
    # Target file in current challenge directory
    file_path = os.path.join(os.path.dirname(__file__), "flag")
    
    if not os.path.exists(file_path):
        print(f"[-] Error: Target file '{file_path}' not found!")
        sys.exit(1)
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().strip()
        
    print(f"[*] Target File:     {file_path}")
    print(f"[*] Character Count: {len(content)}")
    print(f"[+] Recovered Flag:  {content}")
    return content

if __name__ == "__main__":
    solve()
```

**Execution Output:**
```text
[*] Target File:     e:\Advait Kawale\CTF\picoCTF-Writeups\General Skills in CTF's\General Skills in CTF's I\Problem Set 2\Obedient Cat\flag
[*] Character Count: 33
[+] Recovered Flag:  academy{s4n1ty_v3r1f13d_61ddac22}
```

---

## 4. Technical Deep-Dive & Real-World Relevance

### 🛡️ Real-World Plaintext Vulnerabilities:
1. **Plaintext Credential Storage (CWE-312 / CWE-522):**
   - Storing sensitive tokens, API secrets, or passwords "in plain sight" without hashing or encryption is among the most pervasive vulnerabilities in real-world infrastructure. Sensitive keys stored in uncommitted `.env` files, world-readable `/etc/shadow` backups, or unauthenticated S3 buckets can be read by any local or remote user with basic read permissions.
2. **Terminal Stream Redirection & Pipelines:**
   - The power of Unix tools like `cat` stems from modular I/O redirection. Outputs from `cat` are routinely piped into parsers, filters, and analyzers:
     ```bash
     # Search for flag pattern using grep
     cat flag | grep -E "academy\{.*\}"
     
     # Hex dump the file to check for hidden null bytes or non-printable characters
     cat flag | xxd
     ```
3. **Safety Warning (`cat`ting Untrusted Files):**
   - Be cautious when using `cat` on unknown binary files or hostile inputs! Malicious payloads can contain ANSI escape code sequences that can clear your terminal, overwrite command history, or remap terminal keybindings (known as terminal injection). Always verify file types with `file <filename>` or use `less` / `xxd` for binary data.

---

## 5. Flag Recovery

Reading the contents of the downloaded `./flag` file directly reveals the flag:

$$\text{File Stream}(\text{flag}) \longrightarrow \text{academy\{s4n1ty\_v3r1f13d\_61ddac22\}}$$

**Recovered Flag:**
```text
academy{s4n1ty_v3r1f13d_61ddac22}
```

---

## 6. Key Takeaways & Pro-Tips
- **Verify File Types First:** Use `file <filename>` or `head -n 5 <filename>` before dumping entire files to avoid dumping raw binary or garbage characters into your terminal.
- **Master Quick CLI Viewers:** For short text files, `cat` is fastest. For longer files, use `less` (for scrollable navigation) or `head` / `tail` (to inspect headers and trailers).
