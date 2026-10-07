# Wave a flag Writeup
*Author: Advait Kawale*

## 1. Challenge Overview
- **Name:** Wave a flag
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** syreal
- **Event:** picoCTF 2021
- **Description:** Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information... [warm](./warm)
- **Flag Format:** `academy{...}`
- **Repository File Path:** [`./warm`](./warm) (`General Skills in CTF's/General Skills in CTF's I/Problem Set 2/Wave a flag/warm`)
- **Date and Time of Completion:** 2026-10-07 09:41:00+05:30

---

## 2. Initial Triage & Binary Inspection

The challenge provides a compiled Linux executable named `warm`. In command-line environments, utilities and binaries traditionally accept modifier switches or "flags" (such as `-h`, `--help`, or `-v`) to alter execution behavior or display usage instructions.

### 🔬 ELF Header & File Identification
Before executing any unknown binary, we first inspect its file format and architecture using the `file` utility:

```bash
file warm
```

**Output:**
```text
warm: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=cf6ec4227d2ad1cf6a2a349e13d0d2cdb2e159f7, for GNU/Linux 3.2.0, with debug_info, not stripped
```

### Key Artifact Properties:
- **Format:** ELF (Executable and Linkable Format) 64-bit
- **Architecture:** x86-64 (AMD64)
- **Position Independent Executable (PIE):** Enabled
- **Stripped Status:** `not stripped` (symbol tables and debugging information are intact)

---

### 📐 Control Flow & Argument Dispatch Diagram

```text
                  ┌──────────────────────────────┐
                  │    Process Launch: ./warm    │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │   Inspect Argument Vector    │
                  │       (argc and argv)        │
                  └──────────────┬───────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 │                               │
        [No Flags / Default]              [Flag: -h Passed]
                 │                               │
                 ▼                               ▼
  ┌──────────────────────────────┐ ┌──────────────────────────────┐
  │ Print Prompt:                │ │ Output Embedded Flag:        │
  │ "Hello user! Pass me a -h    │ │ "Oh, help? I actually don't  │
  │  to learn what I can do!"    │ │  do much, but I do have this │
  │                              │ │  flag: academy{...}"         │
  └──────────────────────────────┘ └──────────────────────────────┘
```

---

## 3. Step-by-Step Solution

### Method 1: Linux CLI Execution with Help Flag (Intended Solution)
Freshly downloaded binaries from the internet lack execute permissions (`+x`) by default on Unix-like filesystems. We grant executable rights using `chmod` and test both default execution and the `-h` flag:

```bash
# 1. Grant execute permission
chmod +x warm

# 2. Run binary without arguments
./warm
# Output: Hello user! Pass me a -h to learn what I can do!

# 3. Invoke with the requested -h help flag
./warm -h
```

**Terminal Output:**
```text
Oh, help? I actually don't do much, but I do have this flag here: academy{b1scu1ts_4nd_gr4vy_57d8c79}
```

---

### Method 2: Static String Extraction (No Execution Required)
Because the binary is unstripped and stores the flag as plaintext inside the read-only data segment (`.rodata`), we can extract the flag statically using `strings` without executing untrusted code:

```bash
strings warm | grep -E "academy\{.*\}"
```

**Terminal Output:**
```text
Oh, help? I actually don't do much, but I do have this flag here: academy{b1scu1ts_4nd_gr4vy_57d8c79}
```

---

### Method 3: Disassembly & Reverse Engineering (`objdump`)
Inspecting the compiled disassembly of `main` illustrates how the binary evaluates `argc` and `argv`:

```bash
objdump -d -M intel warm | grep -A 25 "<main>:"
```

**Assembly Logic Breakdown:**
1. The program compares the argument count (`argc`) stored in `edi`.
2. If `argc > 1`, it fetches the pointer at `argv[1]` and compares the string against `"-h"`.
3. If equal, execution branches to the code block loading the flag string address into `rdi` and calling `puts`.

---

### Method 4: Automated Reproducible Python Solver (`solve.py`)
A cross-platform Python solver that supports both direct binary regex extraction and sub-process execution:

```python
#!/usr/bin/env python3
"""
Challenge: Wave a flag
Author: Advait Kawale
Category: General Skills
"""
import os
import re
import sys

def solve():
    target_path = os.path.join(os.path.dirname(__file__), "warm")
    
    if not os.path.exists(target_path):
        print(f"[-] Error: Target binary '{target_path}' not found!")
        sys.exit(1)
        
    with open(target_path, "rb") as f:
        binary_data = f.read()
        
    # Search for flag pattern in binary stream
    match = re.search(rb"academy\{[^\}]+\}", binary_data)
    
    if match:
        flag = match.group(0).decode("utf-8")
        print(f"[*] Target Binary:   {target_path}")
        print(f"[*] Analysis Type:   Static String Analysis")
        print(f"[+] Recovered Flag:  {flag}")
        return flag
    else:
        print("[-] Flag pattern not found in binary.")
        sys.exit(1)

if __name__ == "__main__":
    solve()
```

**Execution Output:**
```text
[*] Target Binary:   e:\Advait Kawale\CTF\picoCTF-Writeups\General Skills in CTF's\General Skills in CTF's I\Problem Set 2\Wave a flag\warm
[*] Analysis Type:   Static String Analysis
[+] Recovered Flag:  academy{b1scu1ts_4nd_gr4vy_57d8c79}
```

---

## 4. Technical Deep-Dive & Real-World Relevance

### 🛡️ Why Command-Line Flags & Safe Triage Matter:
1. **POSIX Argument Standards:**
   - In C programs, `int main(int argc, char *argv[])` captures input arguments. `argc` contains the number of arguments (including the program name itself at index `0`), while `argv` contains pointers to the strings. Security analysts must understand how applications parse CLI arguments to identify command injection vulnerabilities or undocumented administrative flags.
2. **Static Triage Before Execution:**
   - In malware analysis, running an unknown binary directly on your primary workstation is dangerous. Analysts always perform **static triage** first:
     - Check file hashes and headers with `file`.
     - Extract strings with `strings` or `floss` to detect hardcoded IPs, URLs, or plain strings.
     - Move to an isolated virtual machine or sandbox before invoking `chmod +x` and executing.
3. **The `.rodata` Section:**
   - String literals in compiled C programs reside in the `.rodata` (Read-Only Data) ELF section. Unless an author obfuscates or encrypts the strings using XOR ciphers or packing techniques (e.g., UPX), all strings remain completely visible to reverse engineering tools.

---

## 5. Flag Recovery

Invoking `./warm -h` or extracting the printable strings yields the recovered flag:

$$\text{CLI Execution}(\text{warm } \mathbf{-h}) \longrightarrow \text{academy\{b1scu1ts\_4nd\_gr4vy\_57d8c79\}}$$

**Recovered Flag:**
```text
academy{b1scu1ts_4nd_gr4vy_57d8c79}
```

---

## 6. Key Takeaways & Pro-Tips
- **Remember `chmod +x`:** New binaries downloaded in Linux are not executable by default until you grant execution permissions.
- **Run `strings` First:** Always run `strings` on small CTF binaries—frequently, developers leave answers or debug prints directly in plaintext.
- **Explore Binary Arguments:** Try `-h`, `--help`, `-v`, `-?`, or passing intentional bad arguments to see how programs handle error branching and help menus.
