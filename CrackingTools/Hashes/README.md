# Hashing Algorithms

### Description
Hashing is a data masking technique that is irreversible. The intention is to validate the integrity of the data and is commonly used for passwords, documents and files. The only way to check the integrity is to perform the same hashing technique, then compare the values with each other. Any variation in the original text, from a missing period, to an extra whitespace, will result in a wildly different hashed value.

Hashing is not a password technique! It is only for integrity verification

## Common Tools for cracking Hashes:

### HashCat
```hashcat``` - [Password cracking](https://hashcat.net/wiki/)

Hashcat is a tool you can use to hack hashed passwords

Usage: hashcat [options]... hash|hashfile|hccapxfile [dictionary|mask|directory]...

```-m``` - hash mode (such as md5=0, sha256=1400, etc. Each mode is tied to an id in the form of an int)

hashcat is not exactly intuitive, but it's not too hard to understand either. Running without options, (flags instantiated before presenting the files) runs it in observation mode. It will output what algorithms it thinks you should use based on the hash type. In order to "crack" a hash, it requires you to input a hash mode with ```-m```. Providing the algorithm in the command, outputs a result. If it successfully cracked it, it will output in the format

`<hash>:<password>`

#### Example
hashcat -m 1400 -a 0 secretPasswordHash.txt ../PasswordLists/rockyou1.txt --show

Outputs: **916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745:qwerty098**


## Common Algorithms:
There are hundreds of algorithms on the web for hashing, I'll share a couple of common ones. Note that not every one of these are secure, but you can use them to get a feel for how they work and what's different

### SHA256

```sha256sum``` - [SHA256 checksum (256-bit)](https://linux.die.net/man/1/sha256sum)

creates a hash of a file, or files in a directory: 

sha256sum -file-

sha256sum -directory/-

#### Example
```sha256sum secretPasswordHash.txt```

### SHA1

```sha1sum``` - [SHA1 checksum ](https://linux.die.net/man/1/sha1sum)

creates a hash of a file, or files in a directory: 

sha1sum -file-

sha1sum -directory/-

#### Example
```sha1sum secretPasswordHash.txt```


### md5

```md5sum``` - [MD5 checksum (128-bit)](https://linux.die.net/man/1/md5sum)

creates a hash of a file, or files in a directory: 

md5sum -file-
md5sum -directory/-

#### Example
```md5sum secretPasswordHash.txt```



