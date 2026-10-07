# First Find Writeup
*Author: Advait Kawale*

## 1. Challenge Overview
- **Name:** First Find
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** LT 'syreal' Jones
- **Event:** picoCTF
- **Description:** Unzip this archive and find the file named `uber-secret.txt`
- **Flag Format:** `academy{...}`
- **Repository Files:**
  - Archive File: [`./files.zip`](./files.zip)
- **Date and Time of Completion:** 2026-10-07 23:05:00+05:30

---

## 2. Initial Triage & File Analysis

The challenge provides a zip archive named `files.zip`.

When extracted, it expands into a relatively large directory structure containing multiple folders and many text files.

```bash
$ unzip files.zip
Archive:  files.zip
   creating: files/
   creating: files/satisfactory_books/
   creating: files/satisfactory_books/more_books/
  inflating: files/satisfactory_books/more_books/37121.txt.utf-8  
  ...
   creating: files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/
 extracting: files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt  
  ...
```

The challenge description explicitly instructs us to find a file named `uber-secret.txt`. Manually navigating through every subfolder (`satisfactory_books`, `adequate_books`, `acceptable_books`, etc.) to find this specific file would be tedious and time-consuming.

---

## 3. Step-by-Step Solution

### Method 1: Using `find` (The Intended Way)

The challenge title "First Find" heavily hints at using the Unix `find` command. `find` is designed exactly for this purpose: recursively searching a directory tree for files that match specific criteria (like a filename).

1. First, search for the file using the `find` command:
   ```bash
   find . -name "uber-secret.txt"
   ```

2. The output immediately gives us the exact path:
   ```bash
   ./files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
   ```

3. We can then output the contents of the file using `cat`:
   ```bash
   cat ./files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
   ```

**Output:**
```text
academy{f1nd_15_f457_ab443fd1}
```

---

### Method 2: Combining `find` and `cat` 

We can optimize the above workflow into a single command line by using command substitution or the `-exec` flag:

```bash
# Using -exec flag
find . -name "uber-secret.txt" -exec cat {} +

# Or using command substitution
cat $(find . -name "uber-secret.txt")
```

Both methods automatically search for the file and instantly print its contents in one go.

---

## 4. Technical Deep-Dive: The `find` Command

The `find` command is incredibly powerful for directory traversal and file discovery in Linux. Unlike `grep` which searches for text *inside* files, `find` searches for the *files themselves* based on metadata.

### Useful `find` Flags for CTFs:
- `-name "pattern"`: Searches for files matching the exact name or a wildcard pattern (e.g., `*.txt`).
- `-iname "pattern"`: Case-insensitive search.
- `-type f`: Restricts the search to only files (ignoring directories, symlinks, etc.).
- `-type d`: Restricts the search to directories.
- `-mmin -10`: Finds files modified within the last 10 minutes (useful during incident response or post-exploitation).
- `-size +10M`: Finds files larger than 10 Megabytes.

In our scenario, `find . -name "uber-secret.txt"` tells the system to start searching from the current directory (`.`) downwards for any file explicitly named `uber-secret.txt`.

---

## 5. Flag Recovery

Executing the combined `find` and `cat` command reveals the hidden flag:

$$\text{cat(find}(\text{"uber-secret.txt"})) \longrightarrow \text{academy\{f1nd\_15\_f457\_ab443fd1\}}$$

**Recovered Flag:**
```text
academy{f1nd_15_f457_ab443fd1}
```

---

## 6. Key Takeaways & Defense Relevance
- **File System Discovery:** Searching for misconfigured sensitive files (like `.env`, `id_rsa`, or `config.json`) is a staple technique in both red-teaming (privilege escalation/discovery) and blue-teaming (auditing). `find` allows automation of these sweeps.
- **Hidden Directories:** Notice that `uber-secret.txt` was placed inside a directory named `.secret`. In Linux, any file or folder starting with a dot (`.`) is hidden from the standard `ls` command unless `ls -a` is used. `find` naturally searches through hidden directories, making it perfect for uncovering concealed data.
