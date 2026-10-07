# Static ain't always noise Writeup
*Author: Advait Kawale*

## 1. Challenge Overview
- **Name:** Static ain't always noise
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** syreal
- **Event:** picoCTF 2021
- **Description:** Can you look at the data in this binary? The bash script might help!
- **Flag Format:** `academy{...}`
- **Repository Files:**
  - `static` - The binary file to analyze.
  - `ltdis.sh` - A provided bash script for disassembly and string extraction.
- **Date and Time of Completion:** 2026-10-07 23:25:00+05:30

---

## 2. Initial Triage & File Analysis

The challenge provides two files: a binary named `static` and a bash script named `ltdis.sh`. 

Inspecting the provided bash script (`ltdis.sh`), we can see it attempts to automate two tasks:
1. Disassembling the binary using `objdump -Dj .text`.
2. Extracting readable strings from the binary using `strings -a -t x`.

Here is a snippet from the script:
```bash
echo "Attempting disassembly of $1 ..."
objdump -Dj .text $1 > $1.ltdis.x86_64.txt

if [ -s "$1.ltdis.x86_64.txt" ]
then
	echo "Disassembly successful! Available at: $1.ltdis.x86_64.txt"
	echo "Ripping strings from binary with file offsets..."
	strings -a -t x $1 > $1.ltdis.strings.txt
	echo "Any strings found in $1 have been written to $1.ltdis.strings.txt with file offset"
```

This tells us that passing the binary to the script will automatically generate a text file containing all the strings within the binary. Since flags are usually plain text stored within the binary's data section, extracting strings is the perfect approach.

---

## 3. Step-by-Step Solution

1. First, make the script executable:
   ```bash
   chmod +x ltdis.sh
   ```

2. Run the script against the `static` binary:
   ```bash
   ./ltdis.sh static
   ```
   *Output:*
   ```text
   Attempting disassembly of static ...
   Disassembly successful! Available at: static.ltdis.x86_64.txt
   Ripping strings from binary with file offsets...
   Any strings found in static have been written to static.ltdis.strings.txt with file offset
   ```

3. The script generated a new file containing all the strings from the binary: `static.ltdis.strings.txt`.

4. We can open this file or `grep` it to look for the flag format (`academy{`):
   ```bash
   grep "academy{" static.ltdis.strings.txt
   ```
   *Output:*
   ```text
      3020 academy{d15a5m_t34s3r_fac3431a}
   ```

---

## 4. Technical Deep-Dive: The `strings` Command

While the script did the heavy lifting for us, it's important to understand the command it executed under the hood:

$$\text{strings -a -t x static}$$

- `strings`: This tool scans any file (typically binaries) and extracts sequences of printable characters that are at least 4 characters long and end with a null byte (`\0`).
- `-a` (or `--all`): Scans the entire file, not just the initialized data sections.
- `-t x`: Prints the offset (the location in the file) where the string was found in hexadecimal format.

In compiled binaries (like C/C++ programs), hardcoded strings, variable values, and flag strings are stored directly inside the binary's `.rodata` (Read-Only Data) section. The `strings` tool allows us to rip these human-readable characters out of the machine code without needing to decompile or run the program.

---

## 5. Flag Recovery

After extracting the strings from the binary, the flag was found hardcoded at the hex offset `3020`.

**Recovered Flag:**
```text
academy{d15a5m_t34s3r_fac3431a}
```

---

## 6. Key Takeaways & Defense Relevance
- **Static Analysis Basics:** Using `strings` is almost always the very first step in malware analysis, reverse engineering, and forensics. It instantly provides context (e.g., IP addresses, URLs, error messages, flags) before attempting complex disassembly.
- **Hardcoding Secrets:** This challenge demonstrates the danger of hardcoding sensitive information (like passwords, API keys, or flags) directly into application source code. Compiled binaries do not hide these strings; they are entirely visible to anyone who runs `strings` on the executable.
