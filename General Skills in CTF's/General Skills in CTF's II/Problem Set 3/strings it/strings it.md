# strings it Writeup
*Author: Advait Kawale*

## 1. Challenge Overview
- **Name:** strings it
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** Sanjay C/Danny Tunitis
- **Event:** picoCTF 2019
- **Description:** Can you find the flag in file without running it?
- **Flag Format:** `academy{...}`
- **Repository Files:**
  - `strings` - The binary file containing the hidden flag.
- **Date and Time of Completion:** 2026-10-07 23:30:00+05:30

---

## 2. Initial Triage & File Analysis

The challenge provides a single binary file named `strings`. The description explicitly asks us to find the flag *without* running the file.

When we attempt to inspect the contents of a compiled binary file (like an ELF executable or a PE file) using standard text-viewing tools like `cat`, it typically prints out a garbled mess of unreadable characters because the file consists mostly of machine code instructions.

To analyze a binary without executing it (static analysis), we need a tool that can extract only the human-readable text.

---

## 3. Step-by-Step Solution

### Using the `strings` Command

The standard Linux utility `strings` is designed specifically for this purpose. It scans any file and prints out sequences of printable characters (by default, 4 or more characters long) that end with a null byte (`\0`), ignoring the non-printable machine code.

1. First, we download the `strings` binary provided by the challenge.

2. We run the `strings` command on the binary. Since the output might be massive (containing thousands of strings like imported library names, function names, and debugging text), we pipe (`|`) the output into `grep` to filter for our specific flag format.

```bash
strings strings | grep "academy{"
```

3. The command instantly filters the massive output and returns only the line containing our flag.

**Output:**
```text
academy{5tRIng5_1T_d47eAaCB}
```

---

## 4. Technical Deep-Dive

When developers compile a program (e.g., from C/C++ source code), any hardcoded strings—such as error messages, prompts, default passwords, or flags—are placed directly into the binary executable, typically within the `.rodata` (Read-Only Data) or `.data` sections. 

Because these strings remain in plain text format inside the binary, running the file is entirely unnecessary to read them. The `strings` utility parses the binary file structure and blindly prints anything that looks like an ASCII string.

In real-world cybersecurity scenarios, `strings` is often the very first command executed during malware analysis. Before setting up a sandbox or a disassembler, an analyst will run `strings` to quickly look for:
- Embedded IP addresses or Domains (Command & Control servers)
- Suspicious API calls (e.g., `VirtualAlloc`, `CreateRemoteThread`)
- Registry keys the malware might attempt to modify
- Hardcoded passwords or cryptographic keys

---

## 5. Flag Recovery

**Recovered Flag:**
```text
academy{5tRIng5_1T_d47eAaCB}
```

---

## 6. Key Takeaways
- **Static Analysis Basics:** Extracting strings is the foundational step of static binary analysis.
- **Never Hardcode Secrets:** Hardcoding sensitive data (API keys, passwords, flags) directly into the source code of an application provides zero security against anyone with access to the compiled binary.
