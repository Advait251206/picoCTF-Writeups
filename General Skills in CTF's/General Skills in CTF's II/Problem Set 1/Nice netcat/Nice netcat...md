# Nice netcat... Writeup
*Author: Advait Kawale*

## 1. Challenge Overview
- **Name:** Nice netcat...
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** syreal
- **Event:** picoCTF 2021
- **Description:** There is a nice program that you can talk to by using this command in a shell: `$ nc xebec.cylabacademy.net 40055`, but it doesn't speak English...
- **Flag Format:** `academy{...}`
- **Active Connection Endpoint:** `nc xebec.cylabacademy.net 40055`
- **Date and Time of Completion:** 2026-10-07 09:54:00+05:30

> [!NOTE]
> **Dynamic Instance & Port Notice:** Remote challenge instances and ports on CyLab Academy / picoCTF are dynamically provisioned per user session. The active hostname (e.g., `xebec.cylabacademy.net`) and port number (e.g., `40055`) assigned to your session will vary, but the interaction and decoding methodology remain identical.

---

## 2. Initial Triage & Protocol Analysis

Connecting to the remote service using Netcat does not return human-readable text; instead, the remote daemon continuously streams newline-delimited decimal integers:

```text
97 
99 
97 
100 
101 
109 
121 
123 
103 
48 
...
```

### 🔬 Pattern Identification & ASCII Mapping
Looking closely at the initial sequence of integers:
- `97`  ➔ `'a'`
- `99`  ➔ `'c'`
- `97`  ➔ `'a'`
- `100` ➔ `'d'`
- `101` ➔ `'e'`
- `109` ➔ `'m'`
- `121` ➔ `'y'`
- `123` ➔ `'{'`

The numbers correspond directly to decimal ASCII character codes spelling out the target flag header **`academy{`**. The remote program is sending character code points line-by-line across raw TCP.

---

### 📐 Stream Transformation & Parsing Pipeline

```text
Remote Daemon: xebec.cylabacademy.net:40055
             │
             ▼  (Raw TCP Stream: Newline-separated Integers)
┌────────────────────────────────────────────────────────┐
│  Data Stream: 97 \n 99 \n 97 \n 100 \n 101 \n 109 ... │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼  (UNIX Pipe '|' / Standard In)
┌────────────────────────────────────────────────────────┐
│     Decoding Logic: Character Conversion (chr(n))      │
│  97 ➔ 'a' │ 99 ➔ 'c' │ 97 ➔ 'a' │ 100 ➔ 'd' ...        │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼  (Concatenated String)
Terminal Output: academy{g00d_k1tty!_n1c3_k1tty!_35e0c}
```

---

## 3. Step-by-Step Solution

### Method 1: Linux / Bash Netcat to Python Pipeline (Fastest & One-Liner)
Pipe the raw socket stream directly from Netcat into an inline Python processor that casts each integer to its corresponding ASCII character:

```bash
nc xebec.cylabacademy.net 40055 | python3 -c "import sys; print(''.join(chr(int(line.strip())) for line in sys.stdin if line.strip().isdigit()))"
```

**Terminal Output:**
```text
academy{g00d_k1tty!_n1c3_k1tty!_35e0c}
```

---

### Method 2: Pure Linux / AWK One-Liner
For minimal resource consumption on POSIX shells without invoking Python, the standard text processor `awk` formats integers using `%c`:

```bash
nc xebec.cylabacademy.net 40055 | awk '{printf "%c", $1}' ; echo ""
```

**Terminal Output:**
```text
academy{g00d_k1tty!_n1c3_k1tty!_35e0c}
```

---

### Method 3: Windows PowerShell Socket Decoder
On Windows systems without Netcat installed, PowerShell establishes the TCP connection, buffers the response, splits whitespace tokens, and casts each value into `.NET` `[char]`:

```powershell
$client = New-Object System.Net.Sockets.TcpClient("xebec.cylabacademy.net", 40055)
$stream = $client.GetStream()
$reader = New-Object System.IO.StreamReader($stream)
$raw = $reader.ReadToEnd()
$client.Close()

$flag = -join (($raw.Trim() -split "\s+") | ForEach-Object { [char][int]$_ })
Write-Output $flag
```

**Terminal Output:**
```text
academy{g00d_k1tty!_n1c3_k1tty!_35e0c}
```

---

### Method 4: Automated Standalone Python Solver (`solve.py`)
A self-contained solver handling socket lifecycle, timeout safety, and regex flag extraction:

```python
#!/usr/bin/env python3
"""
Challenge: Nice netcat...
Author: Advait Kawale
Category: General Skills
"""
import socket
import re
import sys

def solve(host="xebec.cylabacademy.net", port=40055):
    print(f"[*] Connecting to {host}:{port}...")
    
    raw_buffer = b""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(10.0)
            s.connect((host, port))
            
            while True:
                chunk = s.recv(4096)
                if not chunk:
                    break
                raw_buffer += chunk
                
    except socket.timeout:
        pass
    except socket.error as err:
        print(f"[-] Connection failed: {err}")
        sys.exit(1)
        
    raw_text = raw_buffer.decode("utf-8", errors="ignore")
    tokens = [t.strip() for t in raw_text.split() if t.strip().isdigit()]
    
    print(f"[*] Received {len(tokens)} ASCII character codes.")
    
    # Decode integers to characters
    decoded_string = "".join(chr(int(token)) for token in tokens)
    
    flag_match = re.search(r"academy\{[^\}]+\}", decoded_string)
    if flag_match:
        flag = flag_match.group(0)
        print(f"[+] Recovered Flag: {flag}")
        return flag
    else:
        print(f"[-] Could not find flag in decoded output: {decoded_string}")
        sys.exit(1)

if __name__ == "__main__":
    solve()
```

**Execution Output:**
```text
[*] Connecting to xebec.cylabacademy.net:40055...
[*] Received 38 ASCII character codes.
[+] Recovered Flag: academy{g00d_k1tty!_n1c3_k1tty!_35e0c}
```

---

## 4. Technical Deep-Dive & Real-World Relevance

### 🛡️ Why Decimal/ASCII Encoding Recognition Matters:
1. **WAF & Evasion Detection:**
   - In web and network security, attackers frequently encode strings as decimal sequences (e.g., in SQL injection payloads like `CHAR(97,99,97,100,101,109,121)` or XSS HTML numeric entities `&#97;&#99;...`) to evade rudimentary regex-based intrusion detection filters that only look for plaintext words. Recognizing decimal ASCII sequences is vital for SOC analysts and incident responders triaging alert payloads.
2. **UNIX Pipe Composition (`|`):**
   - The UNIX philosophy stresses creating small, modular utilities that do one job well and compose seamlessly via standard streams (`stdin` / `stdout`). Piping the output of network tools like `nc` directly into parsers like `awk` or `python` allows rapid on-the-wire decoding without intermediate file writes.
3. **End-of-Transmission Handling:**
   - Notice that the remote server transmits the bytes and then closes the connection (sending a TCP `FIN`). Handling network streams requires checking for empty chunks (`if not chunk: break`) to recognize that the remote side has finished writing.

---

## 5. Flag Recovery

Translating each decimal integer received from the network socket into its respective ASCII character yields the flag:

$$\text{ASCII}([97, 99, 97, 100, \dots]) \longrightarrow \text{academy\{g00d\_k1tty!\_n1c3\_k1tty!\_35e0c\}}$$

**Recovered Flag:**
```text
academy{g00d_k1tty!_n1c3_k1tty!_35e0c}
```

---

## 6. Key Takeaways & Pro-Tips
- **Recognize Flag Signatures in Decimal:**
  - `academy{` starts with: `97, 99, 97, 100, 101, 109, 121, 123`
  - `picoCTF{` starts with: `112, 105, 99, 111, 67, 84, 70, 123`
  Spotting these decimal sequences instantly indicates unformatted ASCII text.
- **Pipe Directly:** Never copy hundreds of numbers into web converters manually during a competition. Combine `nc` with `awk` or `python` for instantaneous terminal flag recovery.
