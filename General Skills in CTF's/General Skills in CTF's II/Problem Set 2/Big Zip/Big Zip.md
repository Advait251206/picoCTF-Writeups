# Big Zip Writeup
*Author: Advait Kawale*

## 1. Challenge Overview
- **Name:** Big Zip
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** LT 'syreal' Jones
- **Event:** picoCTF
- **Description:** Unzip this archive and find the flag.
- **Flag Format:** `academy{...}`
- **Repository Files:**
  - Archive File: [`./big-zip-files.zip`](./big-zip-files.zip)
- **Date and Time of Completion:** 2026-10-07 23:10:00+05:30

---

## 2. Initial Triage & File Analysis

The challenge provides a heavily nested zip archive, `big-zip-files.zip`.

Upon extraction, it creates a massive directory named `big-zip-files` that contains hundreds of sub-folders (many with randomized names like `folder_pmbymkjcya`, `folder_cawigcwvgv`, etc.) and thousands of nested `.txt` files. 

```bash
$ unzip big-zip-files.zip
Archive:  big-zip-files.zip
   creating: big-zip-files/
   creating: big-zip-files/folder_pmbymkjcya/
   ...
  inflating: big-zip-files/folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt
```

Unlike the "First Find" challenge where we knew exactly which file name to look for (`uber-secret.txt`), this challenge only tells us to "find the flag". Since the flag could be in *any* of the thousands of files, we cannot simply use the `find` command on a filename. Instead, we must search the *contents* of all files simultaneously.

---

## 3. Step-by-Step Solution

### Using `grep` Recursively

The fastest way to search through the contents of thousands of files across deeply nested directories is by using the `grep` command with its recursive flag (`-r`). Since we know the flag format starts with `academy{`, we can use that as our target string.

1. First, extract the archive:
   ```bash
   unzip big-zip-files.zip
   ```

2. Navigate into the extracted root directory:
   ```bash
   cd big-zip-files
   ```

3. Execute a recursive `grep` search for the string "academy{":
   ```bash
   grep -r "academy{" .
   ```

4. The command rapidly scans all text files in all subdirectories and pinpoints the exact file and line containing the flag.

**Output:**
```text
./folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt:information on the record will last a billion years. Genes and brains and books encode academy{gr3p_15_m4g1c_ef8790dc}
```

---

## 4. Technical Deep-Dive: The `grep -r` Command

`grep` stands for **G**lobal **R**egular **E**xpression **P**rint. By default, `grep` only searches a single file (or a list of provided files). 

However, by passing the `-r` (or `-R` for following symlinks) flag, `grep` changes its behavior:
- It treats the provided path (in our case, `.` representing the current directory) as a starting point.
- It recursively iterates down the entire directory tree, opening every single file it encounters.
- It scans the contents of each file against the provided search string (`"academy{"`).
- When it finds a match, it prefixes the output line with the relative file path where the match was found.

This is infinitely more efficient than trying to script a loop to `cat` every file into `grep`.

---

## 5. Flag Recovery

Executing the recursive search reveals the hidden flag embedded at the end of a random text line:

$$\text{grep -r}(\text{"academy\{"}, \text{.}) \longrightarrow \text{academy\{gr3p\_15\_m4g1c\_ef8790dc\}}$$

**Recovered Flag:**
```text
academy{gr3p_15_m4g1c_ef8790dc}
```

---

## 6. Key Takeaways & Defense Relevance
- **Mass Log & File Parsing:** In cybersecurity, whether hunting for malware artifacts, discovering hardcoded credentials in source code repositories, or analyzing massive directory structures left by attackers, recursive searching (`grep -r` or newer tools like `ripgrep`) is an absolute necessity. 
- **Security Audits:** Blue teamers routinely use `grep -r` against `/etc/` or `/var/www/` directories to check for known misconfigurations or exposed secrets across all configuration files on a server simultaneously.
