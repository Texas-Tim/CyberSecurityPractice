# Bandit Level 12

### Level Goal
The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

### Commands you may need to solve this level
> grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

### Helpful Reading Material
- Rot13 on Wikipedia

### Step by Step Walkthrough:
This required a quick translation of the data. What's happening is what's called a "Caesar Cipher" which is simply rotating by x letters. For example, a Caesar Cipher of 2 would make the letter "a" into "c", it shifts by 2. Thus, to solve this challenge, we just need to shift the letters in the file by 13. 

This can be done with the "tr" command and I used Google to quickly come up with the command. The final command is: 

```cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'```

#### Addition: 
- 'A-Za-z': This defines the range of characters to be translated (all uppercase and lowercase letters). 
- 'N-ZA-Mn-za-m': This defines the replacement characters, where each letter is shifted 13 positions forward in the alphabet, wrapping around from 'Z' to 'A'.


* UserName: bandit12

<details><summary>Flag</summary>
    <pre>
    pwd: 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
    </pre>
   </details>