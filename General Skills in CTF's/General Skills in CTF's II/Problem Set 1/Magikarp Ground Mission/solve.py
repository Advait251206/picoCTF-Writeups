#!/usr/bin/env python3
"""
Magikarp Ground Mission - Automated SSH Flag Collector
Author: Advait Kawale
Category: General Skills
Event: picoCTF 2021
"""

import sys
import paramiko

def solve(host="chatelaine.cylabacademy.net", port=31607, username="ctf-player", password="f6904eaa"):
    print(f"[*] Connecting to {username}@{host}:{port}...")
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(host, port=port, username=username, password=password, timeout=15)
        print("[+] SSH connection established successfully.")
    except Exception as e:
        print(f"[-] Connection failed: {e}")
        sys.exit(1)

    # 1. Retrieve Part 1 & instruction from drop-in directory
    _, stdout_1, _ = ssh.exec_command("cat ~/drop-in/1of3.flag.txt")
    part1 = stdout_1.read().decode().strip()
    
    _, stdout_instr1, _ = ssh.exec_command("cat ~/drop-in/instructions-to-2of3.txt")
    instr1 = stdout_instr1.read().decode().strip()
    print(f"[*] Part 1 Recovered: {part1}")
    print(f"[*] Instruction 1:    {instr1}")

    # 2. Retrieve Part 2 & instruction from root directory (/)
    _, stdout_2, _ = ssh.exec_command("cat /2of3.flag.txt")
    part2 = stdout_2.read().decode().strip()
    
    _, stdout_instr2, _ = ssh.exec_command("cat /instructions-to-3of3.txt")
    instr2 = stdout_instr2.read().decode().strip()
    print(f"[*] Part 2 Recovered: {part2}")
    print(f"[*] Instruction 2:    {instr2}")

    # 3. Retrieve Part 3 from home directory (~)
    _, stdout_3, _ = ssh.exec_command("cat ~/3of3.flag.txt")
    part3 = stdout_3.read().decode().strip()
    print(f"[*] Part 3 Recovered: {part3}")

    ssh.close()
    print("[*] SSH connection closed.")

    full_flag = f"{part1}{part2}{part3}"
    print(f"\n[+] Full Assembled Flag: {full_flag}")
    return full_flag

if __name__ == "__main__":
    if len(sys.argv) == 5:
        solve(host=sys.argv[1], port=int(sys.argv[2]), username=sys.argv[3], password=sys.argv[4])
    else:
        solve()
