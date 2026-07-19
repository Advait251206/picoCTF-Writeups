# picoCTF Writeup: Program Execution

**Author:** Advait Kawale  
**Event:** picoCTF  
**Difficulty:** Trivial  
**Challenge Author:** picoCTF  
**Learning Path:** Low Level Binary Intro  
**Problem Set:** Warmup

## Problem Description
Programs tend to execute or run statements top to bottom in a program. In the last problem, this was perhaps obfuscated by the fact that the first dozens of lines were definitions of functions. In fact, the first item executed normally is `while(True)` at line 161. Everything before is part of a function definition which means execution of these statements is delayed until the function is called, which in this code is possible at `eval(user_input + '()')`, line 165.

## Solution
This is an informational checkpoint challenge explaining control flow and function definitions in Python, directly referencing the code from the previous **Picker I** challenge.

It highlights a fundamental concept in reverse engineering and programming:
1. **Function Definitions** (`def` blocks) are not executed when the script starts. They are simply loaded into memory.
2. **Main Execution** begins at the first unindented line outside a function block (in Picker I, that was the `while(True):` loop).
3. Code inside a function only runs when it is explicitly **called** (e.g., via `eval()`).

Since this is purely an introductory checkpoint, there are no files to download or code to execute. Simply click the **Mark Complete** button on the picoCTF learning path to proceed!

## Flag
*No flag required - just mark as complete.*
