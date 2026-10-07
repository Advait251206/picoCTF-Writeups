# what's a net cat? Writeup
*Author: Advait Kawale*

## 1. Challenge Overview
- **Name:** what's a net cat?
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** Sanjay C/Danny Tunitis
- **Event:** picoCTF 2019
- **Description:** Using netcat (`nc`) is going to be pretty important. Can you connect to `chatelaine.cylabacademy.net` at port `40720` to get the flag?
- **Flag Format:** `academy{...}`
- **Active Connection Endpoint:** `nc chatelaine.cylabacademy.net 40720`
- **Date and Time of Completion:** 2026-10-07 09:51:00+05:30

> [!NOTE]
> **Dynamic Instance & Port Notice:** Remote challenge instances and ports on CyLab Academy / picoCTF are dynamically provisioned per user session. The active hostname (e.g., `chatelaine.cylabacademy.net`) and port number (e.g., `40720`) assigned to your session will vary, but the interaction methodology remains identical.

---

## 2. Initial Triage & Protocol Analysis

The challenge introduces **Netcat** (`nc`), historically dubbed the *"Swiss Army knife of TCP/IP"*. Netcat is a command-line networking utility that reads and writes data across network connections using TCP or UDP protocols.

### 🔬 Raw Socket vs. Application Layer Protocols
Unlike HTTP clients (such as web browsers or `curl`) that encapsulate messages within structured request headers (`GET / HTTP/1.1\r\nHost: ...`), Netcat interacts directly with raw transport-layer byte streams. When connecting to an arbitrary TCP service, Netcat handles the standard TCP 3-way handshake and bridges the remote socket directly to your terminal's standard input (`stdin`) and standard output (`stdout`).

### 📐 TCP Handshake & Data Stream Diagram

```text
Local Client Terminal (nc)                     Remote Challenge Host (Port 40720)
        │                                                    │
        │──────────── SYN (Synchronize: Seq=0) ─────────────>│
        │<─────────── SYN-ACK (Seq=0, Ack=1) ────────────────│  [TCP 3-Way Handshake]
        │──────────── ACK (Acknowledgment: Seq=1) ──────────>│
        │                                                    │
        │                                                    │
        │ [TCP Stream Established - Full Duplex Socket]       │
        │<─────────── Server Push / Banner Data ─────────────│
        │            "You're on your way to becoming..."     │
        │            "academy{nEtCat_Mast3ry_Bc0C3F60}"      │
        │                                                    │
        │──────────── FIN-ACK (Graceful Teardown) ──────────>│
        ▼                                                    ▼
```

---

## 3. Step-by-Step Solution

### Method 1: Linux / POSIX Terminal via Netcat (`nc`)
On any Linux distribution, macOS, or WSL terminal where `netcat` is installed, execute the command specifying the target host and port:

```bash
nc chatelaine.cylabacademy.net 40720
```

**Terminal Output:**
```text
You're on your way to becoming the net cat master
academy{nEtCat_Mast3ry_Bc0C3F60}
```

---

### Method 2: Windows PowerShell (.NET `TcpClient`)
On Windows workstations where third-party `nc.exe` binaries are not installed, PowerShell can establish raw TCP socket streams natively using the .NET framework's `System.Net.Sockets.TcpClient` class:

```powershell
$client = New-Object System.Net.Sockets.TcpClient("chatelaine.cylabacademy.net", 40720)
$stream = $client.GetStream()
$reader = New-Object System.IO.StreamReader($stream)
$response = $reader.ReadToEnd()
Write-Output $response
$client.Close()
```

**Terminal Output:**
```text
You're on your way to becoming the net cat master
academy{nEtCat_Mast3ry_Bc0C3F60}
```

---

### Method 3: Cross-Platform Python Socket One-Liner
If you lack administrative permissions or work across heterogeneous environments, Python's standard `socket` library provides an instant terminal one-liner:

```powershell
python -c "import socket; s = socket.socket(); s.connect(('chatelaine.cylabacademy.net', 40720)); print(s.recv(4096).decode())"
```

**Terminal Output:**
```text
You're on your way to becoming the net cat master
academy{nEtCat_Mast3ry_Bc0C3F60}
```

---

### Method 4: Automated Reproducible Solver Script (`solve.py`)
To archive automated solutions and support programmatically querying dynamic ports:

```python
#!/usr/bin/env python3
"""
Challenge: what's a net cat?
Author: Advait Kawale
Category: General Skills
"""
import socket
import re
import sys

def solve(host="chatelaine.cylabacademy.net", port=40720):
    print(f"[*] Initiating TCP connection to {host}:{port}...")
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
            client_sock.settimeout(10.0)
            client_sock.connect((host, port))
            
            raw_data = client_sock.recv(4096).decode("utf-8", errors="ignore")
            
        print("[*] Server Banner Received:")
        for line in raw_data.strip().split("\n"):
            print(f"    > {line}")
            
        # Parse flag from banner
        flag_match = re.search(r"academy\{[^\}]+\}", raw_data)
        if flag_match:
            flag = flag_match.group(0)
            print(f"[+] Recovered Flag: {flag}")
            return flag
        else:
            print("[-] Flag pattern not detected in server response.")
            sys.exit(1)
            
    except socket.error as err:
        print(f"[-] Connection failed: {err}")
        sys.exit(1)

if __name__ == "__main__":
    solve()
```

**Execution Output:**
```text
[*] Initiating TCP connection to chatelaine.cylabacademy.net:40720...
[*] Server Banner Received:
    > You're on your way to becoming the net cat master
    > academy{nEtCat_Mast3ry_Bc0C3F60}
[+] Recovered Flag: academy{nEtCat_Mast3ry_Bc0C3F60}
```

---

## 4. Technical Deep-Dive & Real-World Relevance

### 🛡️ Why Netcat is Essential in Cybersecurity:
1. **Banner Grabbing & Port Fingerprinting:**
   - Network penetration testers use Netcat to connect to open TCP ports discovered during port scanning (e.g., Nmap) to read service banners without triggering complex client-side handshakes:
     ```bash
     nc -vn 192.168.1.10 22    # Grab SSH version banner
     nc -vn 192.168.1.10 80    # Probe raw HTTP web service
     ```
2. **Reverse Shells & Bind Shells:**
   - In offensive operations, Netcat is widely used to catch remote command-execution payloads. An attacker listens on an external port:
     ```bash
     nc -lvnp 4444            # Listener awaiting inbound reverse connection
     ```
   - The compromised target then redirects its shell (`/bin/sh` or `cmd.exe`) over the established socket back to the attacker's listener.
3. **Piping & Network File Transfers:**
   - Netcat can effortlessly transmit files between hosts over arbitrary ports without needing FTP, SSH, or SMB credentials:
     ```bash
     # Receiver:
     nc -lp 9001 > received_file.bin
     # Sender:
     nc target_ip 9001 < file_to_send.bin
     ```

---

## 5. Flag Recovery

Connecting to the challenge endpoint on port `40720` immediately outputs the challenge banner and the flag:

$$\text{TCP Socket}(\text{chatelaine.cylabacademy.net}:\text{40720}) \longrightarrow \text{academy\{nEtCat\_Mast3ry\_Bc0C3F60\}}$$

**Recovered Flag:**
```text
academy{nEtCat_Mast3ry_Bc0C3F60}
```

---

## 6. Key Takeaways & Pro-Tips
- **Syntax Rememberer:** Netcat syntax is simply `nc <host> <port>` (space-separated, no colon `:` between host and port).
- **Socket Timeouts:** In scripting, always set explicit socket timeouts (`client.settimeout(...)`) to prevent network calls from hanging indefinitely if the remote server remains idle after transmission.
