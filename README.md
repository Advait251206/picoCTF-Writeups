# 🚩 picoCTF Writeups & Cybersecurity Journey

Welcome to my personal collection of **picoCTF Writeups**! 

This repository serves as a centralized hub for all my solutions, methodologies, and learning notes as I progress through various picoCTF challenges and explore the expansive world of cybersecurity. Whether you're here to learn a new technique, compare solutions, or just browse through different exploitation methodologies, I hope you find these writeups helpful and informative.

## 🎯 Purpose and Goals

The main goal of this repository is to systematically document my journey in cybersecurity and capture the underlying problem-solving processes I use for CTF (Capture The Flag) challenges. 

By writing detailed explanations for each challenge, I aim to:
- **Solidify Concepts:** Teaching and documenting is the best way to master complex topics like memory corruption and reverse engineering.
- **Build a Knowledge Base:** Create a searchable, personal wiki of tools, scripts, and techniques that I can refer back to in future competitions.
- **Help Others:** Provide clear, step-by-step guides for beginners who might be stuck on similar challenges.

## 📂 Repository Structure

The repository is organized directly by learning paths and problem sets to make navigation intuitive. Instead of just throwing all scripts into a single directory, each challenge is isolated into its own dedicated environment.

Inside each challenge's folder, you will typically find:
- **Detailed Writeup (`.md`):** A comprehensive markdown file containing the problem description, my thought process, the exact tools used (like `gdb`, `objdump`, or Python), the solution, and the final flag.
- **Source Code & Binaries:** The vulnerable C code, compiled ELF binaries, or text files provided by the challenge to allow for local testing and debugging.
- **Exploit Scripts:** Any Python (often utilizing `pwntools` or `socket`), Bash, or other scripts written to automate the exploitation process and grab the flag from the remote server.

## 📚 Learning Paths

<details>
  <summary><strong>General Skills in CTF's</strong></summary>

  <div style="padding-left: 15px;">
    <details>
      <summary><strong>General Skills in CTF's II</strong></summary>

      <ul>
        <li><a href="Learning%20Paths/General%20Skills%20in%20CTF's/General%20Skills%20in%20CTF's%20II/Problem%20Set%201">Problem Set 1</a></li>
        <li><a href="Learning%20Paths/General%20Skills%20in%20CTF's/General%20Skills%20in%20CTF's%20II/Problem%20Set%202">Problem Set 2</a></li>
        <li><a href="Learning%20Paths/General%20Skills%20in%20CTF's/General%20Skills%20in%20CTF's%20II/Problem%20Set%203">Problem Set 3</a></li>
      </ul>
    </details>
    <details>
      <summary><strong>General Skills in CTFs I</strong></summary>

      <ul>
        <li><a href="Learning%20Paths/General%20Skills%20in%20CTF's/General%20Skills%20in%20CTFs%20I/Problem%20Set%201">Problem Set 1</a></li>
        <li><a href="Learning%20Paths/General%20Skills%20in%20CTF's/General%20Skills%20in%20CTFs%20I/Problem%20Set%202">Problem Set 2</a></li>
      </ul>
    </details>
  </div>
</details>

<details>
  <summary><strong>Low Level Binary Intro</strong></summary>

  <div style="padding-left: 15px;">
    <details>
      <summary><strong>Binary Exploitation</strong></summary>

      <ul>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Binary%20Exploitation/Binary%20Exploitation">Binary Exploitation</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Binary%20Exploitation/buffer%20overflow%200">buffer overflow 0</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Binary%20Exploitation/buffer%20overflow%200%20solution">buffer overflow 0 solution</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Binary%20Exploitation/buffer%20overflow%201">buffer overflow 1</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Binary%20Exploitation/buffer%20overflow%201%20solution">buffer overflow 1 solution</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Binary%20Exploitation/Local%20Target">Local Target</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Binary%20Exploitation/Local%20Target%20solution">Local Target solution</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Binary%20Exploitation/Picker%20IV">Picker IV</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Binary%20Exploitation/Picker%20IV%20solution">Picker IV solution</a></li>
      </ul>
    </details>
    <details>
      <summary><strong>Interlude</strong></summary>

      <ul>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Interlude/Interlude">Interlude</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Interlude/Picker%20II">Picker II</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Interlude/Picker%20II%20solution">Picker II solution</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Interlude/Picker%20III">Picker III</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Interlude/Picker%20III%20solution">Picker III solution</a></li>
      </ul>
    </details>
    <details>
      <summary><strong>Intro to Assembly</strong></summary>

      <ul>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Intro%20to%20Assembly/Assembly%20Arithmetic">Assembly Arithmetic</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Intro%20to%20Assembly/Assembly%20Branching">Assembly Branching</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Intro%20to%20Assembly/Assembly%20Pointers">Assembly Pointers</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Intro%20to%20Assembly/Bit-O-Asm-1">Bit-O-Asm-1</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Intro%20to%20Assembly/Bit-O-Asm-2">Bit-O-Asm-2</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Intro%20to%20Assembly/Bit-O-Asm-3">Bit-O-Asm-3</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Intro%20to%20Assembly/Bit-O-Asm-4">Bit-O-Asm-4</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Intro%20to%20Assembly/Intro%20to%20Assembly">Intro to Assembly</a></li>
      </ul>
    </details>
    <details>
      <summary><strong>Intro to Debuggers</strong></summary>

      <ul>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Intro%20to%20Debuggers/ASCII%20FTW">ASCII FTW</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Intro%20to%20Debuggers/Breakpoints">Breakpoints</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Intro%20to%20Debuggers/Calling%20functions">Calling functions</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Intro%20to%20Debuggers/Disassembly%20Capstone">Disassembly Capstone</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Intro%20to%20Debuggers/Disassembly%20Capstone%20solutions">Disassembly Capstone solutions</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Intro%20to%20Debuggers/Examining%20memory">Examining memory</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Intro%20to%20Debuggers/GDB">GDB</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Intro%20to%20Debuggers/GDB%20baby%20step%201">GDB baby step 1</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Intro%20to%20Debuggers/GDB%20baby%20step%202">GDB baby step 2</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Intro%20to%20Debuggers/GDB%20baby%20step%203">GDB baby step 3</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Intro%20to%20Debuggers/GDB%20baby%20step%204">GDB baby step 4</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Intro%20to%20Debuggers/Static%20analysis%20of%20debugger0_b">Static analysis of debugger0_b</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Intro%20to%20Debuggers/Static%20and%20Dynamic%20Analysis">Static and Dynamic Analysis</a></li>
      </ul>
    </details>
    <details>
      <summary><strong>Outro</strong></summary>

      <ul>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Outro">Outro</a></li>
      </ul>
    </details>
    <details>
      <summary><strong>Warmup</strong></summary>

      <ul>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Warmup/ASCII%20Numbers">ASCII Numbers</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Warmup/Hexadecimal">Hexadecimal</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Warmup/Obedient%20Cat">Obedient Cat</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Warmup/Picker%20I">Picker I</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Warmup/Program%20Execution">Program Execution</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Warmup/Python">Python</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Warmup/Sanity%20check%20problems">Sanity check problems</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Warmup/The%20ASCII%20encoding">The ASCII encoding</a></li>
        <li><a href="Learning%20Paths/Low%20Level%20Binary%20Intro/Warmup/Warmed%20Up">Warmed Up</a></li>
      </ul>
    </details>
  </div>
</details>


## 🛠️ Tools & Technologies Used

Throughout these writeups, you'll see a variety of industry-standard tools being utilized:
- **Debuggers & Disassemblers:** GDB, objdump
- **Scripting:** Python 3, Bash
- **Networking:** netcat (nc), sockets
- **Version Control:** Git

## 🚀 About the Author

I am Advait Kawale, an enthusiast exploring the fascinating and challenging world of cybersecurity. My interests span across reverse engineering, binary exploitation, cryptography, and web exploitation. I believe that hands-on practice through platforms like picoCTF is the best way to transition from theoretical knowledge to practical offensive security skills.

Feel free to explore the writeups, and happy hacking!

---

*“Security is a process, not a product.” – Bruce Schneier*
