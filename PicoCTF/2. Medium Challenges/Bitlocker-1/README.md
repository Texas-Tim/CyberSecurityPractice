**Challenge:** Bitlocker-1

**Level:** Medium

**Challenge Author:** Venax

### Description:
Jacky is not very knowledgable about the best security passwords and used a simple password to encrypt their BitLocker drive. See if you can break through the encryption!

### Step-by-Step Walkthrough:
We are presented with another .dd file. This time though, there is an element of `bitlocker` which I'm currently unfamiliar with. We'll try some standard techniques of investigation before diving into anything related to `bitlocker`

#### Note
This challenge is unfinished

I'm going through a lot of unnecessary work to recall how to investigate disk drives. If you want to get to the content, skip to the `mounting the image` section

## Investigation - strings
My first step is to use `strings` command with `grep` to obtain what we need. I used the following command

`strings disko-2.dd | grep 'picoCTF{[^}]*}'`

This results in nothing, and I even tried outputting to a .txt file and discovered a lot of lines of just a few characters. I did try searching for parts of a flag but nothing significant really showed up.

## Investigation - partitions
Let's try looking at partitions. To check the existing partitions of our disk drive, we can run the command: 

`fdisk -l bitlocker-1.dd`

this results in

```
Disk bitlocker-1.dd: 100 MiB, 104857600 bytes, 204800 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x78787878

Device          Boot      Start        End    Sectors   Size Id Type
bitlocker-1.dd1      2021161080 4042322159 2021161080 963.8G 78 unknown
bitlocker-1.dd2      2021161080 4042322159 2021161080 963.8G 78 unknown
bitlocker-1.dd3      4294932600 8589899894 4294967295     2T 78 unknown
bitlocker-1.dd4      4294967295 5035196669  740229375   353G ff BBT
```

Three of the partitions are unknown types, the fourth one is type `BBT`, I'd bet that's related to `bitlocker`. We'll access that partition directly and go from there.

The command to extract the partition is as follows:

`dd if=bitlocker-1.dd of=bitlocker.img bs=512 skip=4294967295 count=740229375`

where skip is the number of bytes until the partition and count is the total number of bytes. The problem here is the total file size is `100 MiB`...which is smaller than `4294967295`, or the partition that we are targeting. There's no way we can reach it. 

## Investigation - mounting the image
The description to the challenge shares that the file is encrypted. We might have to mount it

I'm moving on from this challenge for now, I will come back to it at a later date. I believe we are expected to use another tool called `bitlocker2john` which I will install at a later date



<details><summary>Flag</summary>
    <pre>
    
    </pre>
   </details>