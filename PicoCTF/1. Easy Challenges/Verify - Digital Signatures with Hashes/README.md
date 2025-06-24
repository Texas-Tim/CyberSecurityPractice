**Challenge:** Verify

**Level:** Easy

**Challenge Author:** Jeffery John

### Description

People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.

### Step-by-Step Walkthrough
Start the instance, and input the password. It asks you to ssh so you can use either your machine or the provided webshell

## Investigation - hashing
Checksum: `3ad37ed6c5ab81d31e4c94ae611e0adf2e9e3e6bee55804ebc7f386283e366a4`

To decrypt the file once you've verified the hash, run `./decrypt.sh files/<file>.`

Now that we're logged in, there are three available resources. 

- checksum.txt which holds our hashed value
- decrypt.sh - which is what we'll use to confirm the hashed value
- files/ - which is a folder containing 301 hashes!

Before we continue, let's explain a little about what we are doing.

## Learning - what are hashes?
Hashes are ways to validate the integrity of data. A "hash" is simply a term for a mathematical function that is intended to be

1. Unbreakable - There are some algorithms that have been cracked, we don't use these anymore
2. Consistent - One data set will always create the same hash no matter what
3. One Direction - ie can't be reversed to the original data
4. Collision Free - ie two different sets of data cannot create the same hash

The point of a hash, is again to verify that the original data has not been tampered with, so the above makes more sense with that in mind. It is not intended to be utilized as a form of authentication, or authorization, so don't get those confused.

Some common hashing algorithms the industry uses is 

- MD5
- SHA-256
- SHA-3

For this exercise, the description tells us we are using the SHA-256 version. The command to use this hash version is `sha256sum`

## Investigation - CheckSum
Now that we've covered Hashing, lets set our goal. In order to verify which folder has the right hash, we have to compare our "checksum" hash with the hash values in the files in the folder "files". I ran the following to quickly compare each file with the checksum

```
sha256sum files/* | grep 3ad37ed6c5ab81d31e4c94ae611e0adf2e9e3e6bee55804ebc7f386283e366a4
```

which returns

```
3ad37ed6c5ab81d31e4c94ae611e0adf2e9e3e6bee55804ebc7f386283e366a4  files/e018b574
```

The file is of course encrypted, so lets use our decrypt file

`./decrypt.sh files/e018b574`

<details><summary>Flag</summary>
    <pre>
    picoCTF{trust_but_verify_e018b574}
    </pre>
   </details>