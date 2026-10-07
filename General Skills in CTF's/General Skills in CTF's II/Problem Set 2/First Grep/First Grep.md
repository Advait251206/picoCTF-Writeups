# First Grep Writeup
*Author: Advait Kawale*

## 1. Challenge Overview
- **Name:** First Grep
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** Alex Fulton/Danny Tunitis
- **Event:** picoCTF 2019
- **Description:** Can you find the flag in the file? This would be really tedious to look through manually, something tells me there is a better way. The flag is in this [file](./file).
- **Flag Format:** `academy{...}`
- **Repository Files:**
  - Challenge File: [`./file`](./file)
- **Date and Time of Completion:** 2026-10-07 23:00:00+05:30

---

## 2. Initial Triage & File Analysis

The challenge provides a single artifact simply named `file`. 

Inspecting the file properties:
```bash
$ file file
file: ASCII text, with very long lines (14546)

$ wc -c file
14546 file
```

Opening the file in a text editor or printing it to the terminal reveals a massive wall of text containing thousands of random alphanumeric characters and symbols. 
Since the challenge description hints that looking through it manually would be "really tedious" and asks us to use a "better way", the intended solution clearly revolves around text-searching tools.

The flag format for this repository is strictly `academy{...}` (adapted from the original `picoCTF{...}` format). Knowing this prefix makes it trivial to locate the exact string within the 14.5 KB of junk data.

---

## 3. Step-by-Step Solution

### Method 1: Using `grep` (The Intended Way)

The challenge title "First Grep" is a direct nod to the Unix/Linux `grep` command, which stands for **G**lobal **R**egular **E**xpression **P**rint. It searches files for a specific string or regular expression and prints the matching lines.

1. Download the challenge file:
   ```bash
   wget https://challenge-files.cylabacademy.net/library/3ff907ca5b2c4bf9b5c47914ad89787b1dcbf5e88d99b96c52eb652a6b5f3729/file
   ```

2. Run `grep` specifying the known flag prefix:
   ```bash
   grep "academy{" file
   ```

3. `grep` instantly filters out all the noise and outputs the exact sequence containing our flag.

**Output:**
```text
academy{grep_is_good_to_find_things_d00Ca181}
```

---

### Method 2: Using Python to Search

For those in an environment without `grep` (like a default Windows Command Prompt), a simple Python script achieves the exact same result:

```python
# solve.py
with open("file", "r") as f:
    contents = f.read()
    
    # Find the starting index of our known prefix
    start_idx = contents.find("academy{")
    
    if start_idx != -1:
        # Find the closing brace starting from the prefix
        end_idx = contents.find("}", start_idx)
        
        # Extract and print the flag
        print(contents[start_idx:end_idx+1])
```

Running this script yields the same flag string immediately.

---

## 4. Technical Deep-Dive: The `grep` Command

`grep` is one of the most foundational and ubiquitous tools in a Unix environment for text processing and log analysis. 

### Core Mechanics
- **Pattern Matching:** By default, `grep` uses Basic Regular Expressions (BRE). It reads the target file line-by-line and checks if the pattern exists anywhere within that line.
- **Line-Oriented:** `grep` outputs the *entire line* that contains a match. In our challenge, the file essentially consisted of a single giant line, which is why `grep` outputs the surrounding characters unless specifically constrained.

### Useful `grep` Flags for CTFs:
- `-i`: Case-insensitive search (e.g., matching both `academy` and `ACADEMY`).
- `-r` / `-R`: Recursive search. Vital for finding flags hidden deep within a nested folder structure (e.g., `grep -r "academy{" .`).
- `-o`: Only output the exact matching string, not the whole line. If we used `grep -o "academy{.*}" file`, it would strictly return the flag without any surrounding junk.
- `-E`: Extended Regular Expressions (equivalent to `egrep`), allowing for more complex pattern matching.

---

## 5. Flag Recovery

Executing the `grep` search reveals the hidden string:

$$\text{grep}(\text{"academy\{"}, \text{file}) \longrightarrow \text{academy\{grep\_is\_good\_to\_find\_things\_d00Ca181\}}$$

**Recovered Flag:**
```text
academy{grep_is_good_to_find_things_d00Ca181}
```

---

## 6. Key Takeaways & Defense Relevance
- **Log Analysis and Forensics:** In real-world security operations (SOC), analysts rarely read log files manually. Tools like `grep`, `awk`, and `sed` are essential for parsing massive access logs, event traces, or system artifacts to find Indicators of Compromise (IoCs).
- **Data Exfiltration:** Threat actors often hide malicious payloads or stolen data within large, seemingly benign files (a basic form of steganography or obfuscation). Knowing how to rapidly search for known data patterns (like credit card formats, SSNs, or specific file signatures) is a mandatory skill for Incident Response.
