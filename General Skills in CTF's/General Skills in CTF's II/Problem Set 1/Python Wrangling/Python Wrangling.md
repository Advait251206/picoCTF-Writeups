# Python Wrangling Writeup
*Author: Advait Kawale*

## 1. Challenge Overview
- **Name:** Python Wrangling
- **Category:** General Skills
- **Difficulty:** Medium
- **Author:** syreal
- **Event:** picoCTF 2021
- **Description:** Python scripts are invoked kind of like programs in the Terminal... Can you run [ende.py](./ende.py) using [password.txt](./password.txt) to get [flag.txt.en](./flag.txt.en)?
- **Flag Format:** `academy{...}`
- **Repository Files:**
  - Python Script: [`./ende.py`](./ende.py)
  - Key / Password File: [`./password.txt`](./password.txt)
  - Encrypted Ciphertext: [`./flag.txt.en`](./flag.txt.en)
- **Date and Time of Completion:** 2026-10-07 10:05:00+05:30

---

## 2. Initial Triage & Code Analysis

The challenge provides three artifacts:
1. `ende.py` — A command-line Python script that encrypts and decrypts files using symmetric encryption.
2. `password.txt` — A plaintext file containing a 32-character hexadecimal secret string:
   ```text
   563e47ddeaf84eca8b2a31201381a898
   ```
3. `flag.txt.en` — A Base64-like encrypted token:
   ```text
   gAAAAABqsztJ43kjVaRVflgazu5AoJlLjErpi0AvUFcdPCrHlptbf9RiJsx7Kh3rYHHReV4TgC070k5cus0G5ZrRaX0pGGzR7IDId6jDku2sR--HIimBa2krmasxk2ADXHfP6vQyPAep
   ```

### 🔬 Dissecting `ende.py`

Inspecting the source code of `ende.py` reveals how it handles CLI arguments and performs cryptography:

```python
import sys
import base64
from cryptography.fernet import Fernet

usage_msg = "Usage: "+ sys.argv[0] +" (-e/-d) [file]"
help_msg = usage_msg + "\n" +\
        "Examples:\n" +\
        "  To decrypt a file named 'pole.txt', do: " +\
        "'$ python "+ sys.argv[0] +" -d pole.txt'\n"

if len(sys.argv) < 2 or len(sys.argv) > 4:
    print(usage_msg)
    sys.exit(1)
```

Key observations:
1. **Argument Parsing:** The script expects at least an operation flag (`-e` for encrypt, `-d` for decrypt) and a file path.
2. **Undocumented CLI Argument:**
   ```python
   elif sys.argv[1] == "-d":
       if len(sys.argv) < 4:
           sim_sala_bim = input("Please enter the password:")
       else:
           sim_sala_bim = sys.argv[3]
   ```
   If 4 arguments (`sys.argv[0]` through `sys.argv[3]`) are provided, the script skips the interactive `input()` prompt and directly consumes `sys.argv[3]` as the encryption password!
3. **Key Derivation & Fernet Cipher:**
   ```python
   ssb_b64 = base64.b64encode(sim_sala_bim.encode())
   c = Fernet(ssb_b64)
   ```
   The password string is Base64-encoded to form a 44-byte string, which satisfies the Fernet key requirement (32 URL-safe Base64-encoded bytes).

---

## 3. Step-by-Step Solution

### Method 1: Interactive Execution (Standard Workflow)

Run `ende.py` with the `-d` (decrypt) flag pointing to `flag.txt.en`. When prompted, provide the contents of `password.txt`:

1. View the password:
   ```bash
   cat password.txt
   # 563e47ddeaf84eca8b2a31201381a898
   ```

2. Invoke the script:
   ```bash
   python3 ende.py -d flag.txt.en
   ```

3. Paste the password into the prompt:
   ```text
   Please enter the password: 563e47ddeaf84eca8b2a31201381a898
   academy{4p0110_1n_7h3_h0us3_d6af8f37}
   ```

---

### Method 2: CLI Parameter Execution (Undocumented 3rd Argument)

Because `ende.py` supports an optional fourth positional argument (`sys.argv[3]`), we can pass the password directly without entering interactive mode:

```bash
python3 ende.py -d flag.txt.en 563e47ddeaf84eca8b2a31201381a898
```

Or dynamically via command substitution in bash:
```bash
python3 ende.py -d flag.txt.en $(cat password.txt)
```

**Output:**
```text
academy{4p0110_1n_7h3_h0us3_d6af8f37}
```

---

### Method 3: Shell Redirection & Pipeline Automation

In automated CTF pipelines or headless environments, standard input can be redirected directly into the script:

```bash
# Using standard input redirection
python3 ende.py -d flag.txt.en < password.txt

# Or using a pipeline
cat password.txt | python3 ende.py -d flag.txt.en
```

**Output:**
```text
Please enter the password:academy{4p0110_1n_7h3_h0us3_d6af8f37}
```

---

### Method 4: Custom Python Decryption Script (`solve.py`)

If you want to understand or replicate the underlying Fernet decryption independently:

```python
#!/usr/bin/env python3
"""
Python Wrangling - Automated Fernet Decryptor
Author: Advait Kawale
"""
import base64
from cryptography.fernet import Fernet

def main():
    # 1. Load password and ciphertext
    with open("password.txt", "r") as f:
        password = f.read().strip()

    with open("flag.txt.en", "rb") as f:
        ciphertext = f.read().strip()

    # 2. Derive Fernet key
    fernet_key = base64.b64encode(password.encode())
    cipher = Fernet(fernet_key)

    # 3. Decrypt payload
    plaintext = cipher.decrypt(ciphertext)
    print(f"[+] Recovered Flag: {plaintext.decode('utf-8')}")

if __name__ == "__main__":
    main()
```

---

## 4. Cryptographic Deep-Dive: Fernet Architecture

The `cryptography.fernet` implementation in Python is a specification for authenticated, symmetric cryptography. It ensures that the ciphertext cannot be manipulated or read without the key.

### 📐 Anatomy of a Fernet Token

A Fernet token consists of 128-bit AES encryption with HMAC authentication:

```text
+----------------+----------------+-------------------+----------------+----------------+
|  Version (0x80)| Timestamp (8B) |    IV (16 Bytes)  | Ciphertext (NB)|   HMAC (32B)   |
|     1 Byte     |   Big-Endian   |  Random AES IV    |  AES-128-CBC   | SHA-256 Digest |
+----------------+----------------+-------------------+----------------+----------------+
\______________________________________________________________________________________/
                                Base64 URL-Safe Encoded
```

1. **Version Field (`0x80`):** Identifies the Fernet format version.
2. **Timestamp:** 64-bit unsigned integer representing the creation timestamp in seconds since Unix epoch.
3. **Initialization Vector (IV):** A 128-bit randomly generated IV used for CBC mode encryption.
4. **Ciphertext:** The plaintext encrypted under AES-128 in Cipher Block Chaining (CBC) mode with PKCS7 padding.
5. **HMAC:** An HMAC-SHA256 signature calculated over the concatenated Version, Timestamp, IV, and Ciphertext using the signing key to prevent tampering (ciphertext integrity).

Because `password.txt` contains a 32-character ASCII string (`563e47ddeaf84eca8b2a31201381a898`), Base64-encoding it produces exactly 44 URL-safe Base64 characters (32 raw bytes), perfectly matching Fernet's requirement of a 256-bit key (128-bit AES key + 128-bit HMAC key).

---

## 5. Flag Recovery

Executing decryption reveals the flag:

$$\text{Fernet}_{\text{Decrypt}}(\text{flag.txt.en}, \text{password.txt}) \longrightarrow \text{academy\{4p0110\_1n\_7h3\_h0us3\_d6af8f37\}}$$

**Recovered Flag:**
```text
academy{4p0110_1n_7h3_h0us3_d6af8f37}
```

---

## 6. Key Takeaways & Defense Relevance
- **Python CLI Conventions:** Always inspect `sys.argv` handling in source code. Developers often leave undocumented or convenient debug arguments (such as passing credentials as CLI arguments) that can simplify automated exploitation.
- **Handling External Dependencies:** `ende.py` requires `cryptography`. On environments where it is missing, `pip install cryptography` or executing in a virtual environment (`venv`) / Linux subsystem resolves `ModuleNotFoundError`.
- **Command Redirection:** Mastering bash pipelines (`<`, `|`, `$(...)`) enables seamless script execution in non-interactive CI/CD and automation environments.
