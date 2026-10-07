# Tab, Tab, Attack Writeup
*Author: Advait Kawale*

## 1. Challenge Overview
- **Name:** Tab, Tab, Attack
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** syreal
- **Event:** picoCTF 2021
- **Description:** Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames. [Addadshashanammu.zip](./Addadshashanammu.zip)
- **Flag Format:** `academy{...}`
- **Repository Archive Path:** [`./Addadshashanammu.zip`](./Addadshashanammu.zip) (`General Skills in CTF's/General Skills in CTF's II/Problem Set 1/Tab, Tab, Attack/Addadshashanammu.zip`)
- **Date and Time of Completion:** 2026-10-07 09:58:00+05:30

---

## 2. Initial Triage & Directory Tree Analysis

The challenge provides a compressed ZIP archive titled `Addadshashanammu.zip`. Uncompressing the archive reveals a heavily nested, 7-level deep directory hierarchy named after obscure mythological and esoteric locales.

### 🔬 Directory Nesting Hierarchy Diagram

```text
Addadshashanammu.zip
└── 📁 Addadshashanammu/
    └── 📁 Almurbalarammi/
        └── 📁 Ashalmimilkala/
            └── 📁 Assurnabitashpi/
                └── 📁 Maelkashishi/
                    └── 📁 Onnissiralis/
                        └── 📁 Ularradallaku/
                            ├── 📄 fang-of-haynekhtnamet.c   (Source Code)
                            └── ⚙️ fang-of-haynekhtnamet     (ELF Executable)
```

Navigating through these complex, multisyllabic directory names manually by typing every character is slow and prone to typographical errors. This highlights the indispensable power of **terminal tab-completion** (GNU Readline).

---

## 3. Step-by-Step Solution

### Method 1: Terminal Tab-Completion (Intended Learning Workflow)
When only one folder exists at a directory level, pressing the `Tab` key automatically autocompletes the directory name. You can traverse the entire 7-level hierarchy in seconds:

1. Extract the archive:
   ```bash
   unzip Addadshashanammu.zip
   ```
2. Navigate rapidly using `cd` and `Tab` keystrokes:
   ```bash
   cd Add[TAB]/Alm[TAB]/Ash[TAB]/Ass[TAB]/Mae[TAB]/Onn[TAB]/Ula[TAB]
   ```
3. Execute the binary using tab-completion:
   ```bash
   ./fan[TAB]
   ```

**Terminal Output:**
```text
*ZAP!* academy{l3v3l_up!_t4k3_4_r35t!_9d928112}
```

---

### Method 2: Fast CLI File Traversal (`find` & Direct Execution)
In real-world forensics and CTFs, when faced with deeply nested directory trees, you can skip directory navigation entirely using the POSIX `find` command:

```bash
# Locate and execute the binary in one command
find . -type f -executable -exec {} \;
```

Or read the embedded C source code directly:
```bash
find . -name "*.c" -exec cat {} +
```

**Terminal Output:**
```c
#include <stdio.h>

int main(){
printf("*ZAP!* academy{l3v3l_up!_t4k3_4_r35t!_9d928112}\n");
}
```

---

### Method 3: Windows PowerShell Recursive Search
On Windows environments, PowerShell's `Get-ChildItem` effortlessly walks recursive structures:

```powershell
# Find and read the source code file
Get-ChildItem -Recurse -Filter "*.c" | Get-Content
```

**Terminal Output:**
```text
*ZAP!* academy{l3v3l_up!_t4k3_4_r35t!_9d928112}
```

---

### Method 4: Automated In-Memory Python Solver (`solve.py`)
To demonstrate advanced scripting, this solver reads and extracts the flag from the ZIP archive completely in-memory without even extracting the nested folders to disk:

```python
#!/usr/bin/env python3
"""
Challenge: Tab, Tab, Attack
Author: Advait Kawale
Category: General Skills
"""
import zipfile
import re
import os
import sys

def solve():
    zip_path = os.path.join(os.path.dirname(__file__), "Addadshashanammu.zip")
    
    if not os.path.exists(zip_path):
        print(f"[-] Error: Archive '{zip_path}' not found!")
        sys.exit(1)
        
    print(f"[*] Opening archive: {zip_path}")
    
    with zipfile.ZipFile(zip_path, 'r') as archive:
        for file_info in archive.infolist():
            if file_info.filename.endswith(".c") or file_info.filename.endswith("haynekhtnamet"):
                data = archive.read(file_info.filename)
                match = re.search(rb"academy\{[^\}]+\}", data)
                if match:
                    flag = match.group(0).decode("utf-8")
                    print(f"[*] Discovered Artifact: {file_info.filename}")
                    print(f"[+] Recovered Flag:     {flag}")
                    return flag
                    
    print("[-] Flag not found inside archive.")
    sys.exit(1)

if __name__ == "__main__":
    solve()
```

**Execution Output:**
```text
[*] Opening archive: e:\Advait Kawale\CTF\picoCTF-Writeups\General Skills in CTF's\General Skills in CTF's II\Problem Set 1\Tab, Tab, Attack\Addadshashanammu.zip
[*] Discovered Artifact: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet.c
[+] Recovered Flag:     academy{l3v3l_up!_t4k3_4_r35t!_9d928112}
```

---

## 4. Technical Deep-Dive & Real-World Relevance

### 🛡️ Why Terminal Productivity Matters in Security:
1. **The Readline Engine (`Tab` Autocompletion):**
   - Most Unix shells (Bash, Zsh) utilize the GNU **Readline** library for command-line editing. When you hit `Tab`, Readline checks the current path, enumerates directory entries matching your prefix, and expands unambiguous matches. If multiple entries match, a double-tab (`Tab` `Tab`) displays all available candidates.
2. **Directory Obfuscation & Nested Droppers:**
   - Malware authors and packers often create deep or hidden nested directory trees (e.g., hidden under deeply nested `%APPDATA%` or `/var/tmp/.local/...` subdirectories) to deter manual discovery. Knowing how to quickly traverse or recursively search (`find`, `grep -r`, `Get-ChildItem -Recurse`) bypasses manual obfuscation instantly.
3. **In-Memory Zip Inspection:**
   - Security incident responders and triage automation pipelines frequently analyze archive contents in memory without extracting them to disk. This prevents dropped binaries from potentially triggering unauthorized hooks or stomping filesystem timestamps.

---

## 5. Flag Recovery

Executing the discovered binary `./fang-of-haynekhtnamet` outputs the challenge flag:

$$\text{Execution}(\text{fang-of-haynekhtnamet}) \longrightarrow \text{academy\{l3v3l\_up!\_t4k3\_4\_r35t!\_9d928112\}}$$

**Recovered Flag:**
```text
academy{l3v3l_up!_t4k3_4_r35t!_9d928112}
```

---

## 6. Key Takeaways & Pro-Tips
- **Muscle Memory:** Master the `Tab` key. It prevents typing errors in complex paths and confirms whether a target file actually exists before running a command.
- **Bypass Deep Nesting:** When dealing with deep archives, use `find . -type f` or `unzip -j archive.zip` (which strips the directory paths and extracts all files into the current folder).
