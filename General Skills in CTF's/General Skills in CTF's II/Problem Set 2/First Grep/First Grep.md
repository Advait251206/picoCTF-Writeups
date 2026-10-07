# First Grep

## Challenge Details
- **Event:** picoCTF 2019
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** Alex Fulton/Danny Tunitis

## Problem Statement
Can you find the flag in the file? This would be really tedious to look through manually, something tells me there is a better way. The flag is in this [file](https://challenge-files.cylabacademy.net/library/3ff907ca5b2c4bf9b5c47914ad89787b1dcbf5e88d99b96c52eb652a6b5f3729/file).

## Solution
The problem gives us a file that is full of random characters. However, we are told that the flag is inside it. Since we know the flag format is `academy{...}`, we can simply use the `grep` command to search for the string "academy" in the file.

1. First, download the file:
   ```bash
   wget https://challenge-files.cylabacademy.net/library/3ff907ca5b2c4bf9b5c47914ad89787b1dcbf5e88d99b96c52eb652a6b5f3729/file
   ```

2. Then, run `grep` on the file:
   ```bash
   grep "academy{" file
   ```

3. The output directly gives us the flag:
   ```text
   academy{grep_is_good_to_find_things_d00Ca181}
   ```

## Flag
`academy{grep_is_good_to_find_things_d00Ca181}`
