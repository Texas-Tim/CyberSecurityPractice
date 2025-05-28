# Bandit Level 11

### Level Goal
The password for the next level is stored in the file data.txt, which contains base64 encoded data

### Commands you may need to solve this level
> grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

### Helpful Reading Material
- Base64 on Wikipedia

### Step by Step Walkthrough:
The text in this file is encoded with a base64 format. I encourage learning about different numbered formats, but the command "base64" allows for data manipulation in files directly, just make sure you're decoding and not encoding. The final command is 

```cat data.txt | base64 -d```


* UserName: bandit11

<details><summary>Flag</summary>
    <pre>
    pwd: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
    </pre>
   </details>