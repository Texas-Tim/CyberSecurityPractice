# Bandit Level 13

### Level Goal
The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work. Use mkdir with a hard to guess directory name. Or better, use the command “mktemp -d”. Then copy the datafile using cp, and rename it using mv (read the manpages!)

### Commands you may need to solve this level
> grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd, mkdir, cp, mv, file

### Helpful Reading Material
- Hex dump on Wikipedia

### Step by Step Walkthrough:
this was a tough one... it requires multiple steps, but the clues are given in the level information. Specifically, that the files have been repeatedly compressed. There's a few things I learned that are important. 

1. compressed files have a hex signature, this is very important as it will indicate what decompression that you need to use and will hint when you need to unarchive it with "tar"

2. "xxd" is the translation command in Linux to translate between Hex code and binary. You will need to use this to identify compression types

3. "gzip" and "bzip2" are the compression algorithms you'll be working with in this exercise. You will also need "tar" which is an archival tool. Tar will often use gzip to compress files during archival, but this can be triggered to avoid compression with a flag

To progress, it's best to copy to a new location. See the Useful Commands section at the root README for the command to do so. Once the file is copied, you can use the ```|``` command to decompress as you go, or save a new file each time. It's up to you.

The correct steps are: 
1. ```xxd -r``` 
2. ```gzip -d``` 
3. ```bzip2 -d``` 
4. ```gzip -d``` 
5. ```tar -xz``` 
6. ```tar -x``` 
7. ```bzip2 -d``` 
8. ```tar -x``` 
9. ```gzip -d```

The above steps require a little nuance, so you probably won't be able to just plug it in. I recommend saving a new file and tracking your progress. Remember to use ```xxd``` when necessary to identify the correct compression code.


* UserName: bandit13
* pwd: FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn