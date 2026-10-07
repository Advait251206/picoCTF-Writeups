# plumbing Writeup
*Author: Advait Kawale*

## 1. Challenge Overview
- **Name:** plumbing
- **Category:** General Skills
- **Difficulty:** Medium
- **Author:** Alex Fulton/Danny Tunitis
- **Event:** picoCTF 2019
- **Description:** Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to `xebec.cylabacademy.net 21496`.
- **Flag Format:** `academy{...}`
- **Date and Time of Completion:** 2026-10-07 23:35:00+05:30

> [!NOTE]
> **Dynamic Instance Notice:** The hostname (`xebec.cylabacademy.net`) and port (`21496`) shown here were dynamically provisioned for this CTF instance. When replicating this challenge on picoCTF, replace these values with your active instance details.

---

## 2. Initial Triage & Problem Analysis

The challenge instructs us to connect to a remote server (`xebec.cylabacademy.net`) on port `21496` and states that we need to handle "process data outside of a file."

Connecting to remote ports is standard practice in CTFs and is almost exclusively done using the `netcat` (or `nc`) command. 

When we connect to the server, it continuously prints a massive stream of decoy strings to the terminal:
```bash
nc xebec.cylabacademy.net 21496
```
*Output snippet:*
```text
This is defintely not a flag
Not a flag either
Again, I really don't think this is a flag
Not a flag either
This is defintely not a flag
...
```

Because the output is thousands of lines long, finding the flag manually by scrolling through the terminal is inefficient (and sometimes impossible if the terminal buffer isn't large enough). We need a way to filter the output programmatically.

---

## 3. Step-by-Step Solution

### Using Piping and `grep`

The challenge title "plumbing" is a massive hint. In Linux, "plumbing" refers to the concept of **Piping**. A pipe (`|`) takes the standard output (`stdout`) of one command and feeds it directly into the standard input (`stdin`) of another command.

We can pipe the live output from `netcat` directly into `grep` to filter for the flag format (`academy{`).

1. Execute the `netcat` connection and pipe the output to `grep`:
   ```bash
   nc xebec.cylabacademy.net 21496 | grep "academy{"
   ```

2. The `grep` command parses the massive stream of text on-the-fly and instantly prints out the only line containing our target string.

**Output:**
```text
academy{digital_plumb3r_dFED73D2}
```

*Alternative Approach:*
If you wanted to save the output instead of piping it live, you could redirect it to a file and search the file later:
```bash
nc xebec.cylabacademy.net 21496 > output.txt
grep "academy{" output.txt
```

---

## 4. Technical Deep-Dive: I/O Redirection

Linux provides three standard data streams:
1. **Standard Input (stdin / `0`):** Data going into a program.
2. **Standard Output (stdout / `1`):** Data coming out of a program.
3. **Standard Error (stderr / `2`):** Error messages coming out of a program.

Piping (`|`) connects the `stdout` of the left command to the `stdin` of the right command. 
Redirection (`>`) captures the `stdout` of a command and writes it to a file.

Mastering plumbing (piping and redirection) is fundamental to Linux command-line efficiency.

---

## 5. Flag Recovery

**Recovered Flag:**
```text
academy{digital_plumb3r_dFED73D2}
```

---

## 6. Key Takeaways
- **Pipes are Powerful:** You don't always have to save output to a file to analyze it. Using pipes (`|`) allows for real-time, on-the-fly filtering and processing.
- **Log Parsing:** This exact technique (`cat | grep` or `tail -f | grep`) is used extensively in DevOps and Security Operations to filter real-time access logs or error logs on live servers.
