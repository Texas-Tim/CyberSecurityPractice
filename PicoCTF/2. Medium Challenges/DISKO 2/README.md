**Challenge:** DISKO 2

**Level:** Medium

**Challenge Author:** Darkraicg492

### Description: 
Can you find the flag in this disk image? The right one is Linux! One wrong step and its all gone!


### Step-by-Step Walkthrough:
We are presented with another .dd file

#### Investigation - Strings
My first step is to use the same method to grab the flag as the first one. Since we already know the format of the data we are looking for, we can try to use `grep` to obtain what we need. I used the following command

`strings disko-2.dd | grep 'picoCTF{[^}]*}'`

Clearly this is not going to be as simple, we are met with a large number of flags, with the correct one hidden somewhere. We "could" try and input each of them one by one, but that's no fun. Let's take another look at the information provided

#### Investigation - Partitions
In the description, it makes a comment: `the correct one is Linux!`. What does that mean? Well disk drives can be separated and isolated into partitions.

A partition is a logically separated section of a storage device (like a hard drive or USB stick). Each partition acts as an independent unit, allowing you to install different operating systems, organize data, or separate system files from user files. Partitions are defined in the disk’s partition table and can be formatted with different filesystems (e.g., NTFS, ext4, FAT32).

To check the existing partitions of our disk drive, we can run the command: 

`fdisk -l disko-2.dd`

where `-l` says to list all the details of the partitions. We receive the following response:

```
Disk disko-2.dd: 100 MiB, 104857600 bytes, 204800 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x8ef8eaee

Device      Boot Start    End Sectors Size Id Type
disko-2.dd1       2048  53247   51200  25M 83 Linux
disko-2.dd2      53248 118783   65536  32M  b W95 FAT32
```

Now, my first time in this challenge, I didn't receive the second part with the partitions, so it's possible playing around broke the disk drive somehow. This is why backups are so important! I re-downloaded the .dd file and it showed up.

We can see that the disk has 2 partitions, a `Linux` and a `W95 FAT32` partition, which stands for Windows 95 FAT32 filesystem. Based on the description, we want to pay particular attention to the `Linux` distribution, but how do we extract it?

#### Investigation - Extraction
Extraction is the process of retrieving or isolating specific data from a larger set or source. In digital forensics or computing, extraction often refers to pulling out files, partitions, or information from disk images, archives, or other containers for analysis or use. For example, extracting a partition from a disk image means creating a separate file containing only that partition’s data.

The command to extract the partition is as follows:

`dd if=disk.img of=partition.img bs=512 skip=START count=SIZE`

where

* `dd`:The dd command is a Unix/Linux utility used to copy and convert raw data from one location to another. It is often used for tasks such as creating disk images, cloning drives, backing up partitions, and writing ISO files to USB drives.
* `if`: specifies the input file or device.
* `of`: specifies the output file or device.
* `bs`: sets the block size for reading and writing.
* `skip`: specifies how many input blocks to skip before starting to copy.
* `count`: specifies how many input blocks to copy.

Thus, based on our disk meta-data, we can run the following command to get our image:

`dd if=disko-2.dd of=partition.img bs=512 skip=2048 count=51200`

#### Action - Strings
Now that we've extracted and separated the correct partition, let's run our `strings` command again on `partition.img`:

`strings partition.img | grep 'picoCTF{[^}]*}'`

And voila! We've successfully identified the correct flag

<details><summary>Flag</summary>
    <pre>
    picoCTF{4_P4Rt_1t_i5_a93c3ba0}
    </pre>
   </details>