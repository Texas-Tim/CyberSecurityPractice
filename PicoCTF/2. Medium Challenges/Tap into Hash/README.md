**Challenge:** Tap into Hash

**Level:** Medium

**Challenge Author:** NGIRIMANA Schadrack

### Description: 
Can you make sense of this source code file and write a function that will decode the given encrypted file content?

### Step-by-Step Walkthrough:
Another reverse engineering challenge, let's analyze the python file step by step.

First, let's print out a result. If I run the script with `picoCTF` I return

```
Key: b'\xd8\xd4\x81\x9dg\xb8\x1f\xd2\x13?I\x95\xa24\xd0\xa1\x15\xd7:?sC7w\x00e\xae\xd7\xe33 J'

Encrypted Blockchain: b'\xf2\xf9k\xdd^\xfcw\xec\x07\x9fD\xc1w1\xd1\xc5\xf2\xa9h\xd2[\xaav\xe9Y\x90N\x98wh\x81\xc0\xf5\xa8?\xd2Y\xf1!\xe9]\x9d\x10\xccwb\x81\x92\xa2\xfeb\xd8\x06\xffq\xe8\x0b\xcdN\xcf#g\x83\xc2\xba\xfbj\xd2\x07\xf8t\xbc\\\xcb@\xcf.i\x86\xcf\xf3\xffk\x8f\x0c\xad\'\xbcZ\xceG\x9d!c\xdd\x90\xa4\xfak\xde\x0b\xaap\xec]\x90\x12\xc1&h\xdd\x90\xf4\xaao\x8f\x07\xfep\xea\x0f\x9c\x15\xc8p1\xd1\xc1\xae\xe6j\xdb\x0e\xafs\xec\t\x9dA\xc0%4\x84\xc5\xf6\xfej\xda\r\xa8\'\xe9^\x90O\xcasg\xd1\xcf\xaf\xaf*\x82\\\xa6Q\x8cy\xcd@\x9fp1\x86\xce\xa4\xfek\x8a\x0e\xfe\'\xba\x08\xce\x10\x9bs3\xd3\x95\xf3\xfdk\xdf\x0b\xfd&\xefY\x85F\xc9sh\x87\xc6\xf6\xfdj\xdbY\xac"\xb9\t\x9aO\xcf.6\x80\x93\xa6\xafk\xdd\x0b\xfb"\xebY\xc9\x10\x98$b\xd7\xc2\xf2\xafh\xdb\n\xad \xbb]\x91B\xcbuf\xd5\xc3\xa2\xfd9\xdc\x06\xaa&\xea\x07\x9f[\xc9&6\xd4\x92\xf4\xfei\x8d\n\xfb*\xe8\n\x9eG\x9a!6\x87\x90\xae\xfd;\xd3\n\xf0 \xec\x08\x9dB\xc1wc\xdd\xcf\xf2\xf3c\x8d\t\xaf&\xec\x0e\x9fG\xcb.d\x86\x94\xae\xf9<\x8d\x06\xff&\xbd\x0e\xcb\x17\xfc\x13U\xe0\xf3'
```

It's worth noting that if I run it again exactly the same, there's an element of randomness to it and I get a different encryption.


## Investigation - block_chain
1. Take in an argument `text`
2. Generate a random token of length `64` bytes, of groups of two hex characters, transform it to bytes and call it `key`
3. generate a `Block` object called `genesis_block`, which is a custom class. `Block` objects generate a `sha256` hash of its parameter values concatenated in a string
    * index: `0`
    * previous_hash: `0`
    * timestamp: `current epoch time in seconds`
    * encoded_transactions: `EncodedGenesisBlock` string object
    * nonce: `0`
4. Create a list called `blockchain` with the `genesis_block` as the first item
5. Iterate 4 times the following:
    * Make a string: `Transaction_#` where # is the iteration value
    * encode the `string` into `bytes`
    * encode the `bytes` with `base64`
    * transform from `bytes` into `string`
    * create a `new_block` and call the function `proof_of_work()` with the following parameters
        - the last index in the `blockchain`
        - the encoded `string`
    * `proof_of_work()` performs the following
        - sets index to be the next index in the `blockchain` list
        - generates current `EpochTime` in seconds
        - sets nonce = 0
        - create a `Block` object with `previous_hash` equal to the hash of the previous `Block` object
        - iterate through nonce until first two characters of a generated hash is `00`
        - sets new nonce to `Block` object
    * append `new_block` to the end of the `blockchain`
6. create a new `string`, with all 5 `blockchain` objects joined together, separated by `-`
7. encrypt the `blockchain` object with a custom `encrypt` function
8. the `encrypt` function performs the following:
    * take the `blockchain string` and put the `token` aka the flag, in the middle of the `blockchain string` for a `modified string`
    * pad the `modified string` with up to 16 bytes (I found the padding to be the same every time with 5 bytes in hex form. Thus the padding is `\x05\x05\x05\x05\x05`)
    * hash the `key` with a `sha256` hash to make a `key_hash`
    * Since we know the sizes of the values input (`for i in range(0, 336, 16)`), we can say that we now iterate through the `modified string`, `16 bytes` at a time.
    * For each `block` of `32 bytes`, perform `xor` transformation with the `key_hash`
    * The `xor_bytes` function performs:
        - for each value `a` in `block` and `b` in `key_hash` perform an `xor transformation`  
        - create a bytes object with all the values from the above transformation and return
    * create a `ciphertext` object made up of all the `blocks` above and return as `encrypted_blockchain`
9. print the `encrypted_blockchain` 

## Investigation - reverse engineering
First, the only hashed objects are the key, which we can recreate, and the blockchain, which we don't need. What we need, is the flag that's embedded in the middle. So the only thing we need to worry about, is the encryption.

Therefore, reverse engineering this will be fairly simple. We can iterate through the `16 bytes` at a time and perform an `xor` transformation to reverse the previous `xor` process. At this point, the flag should be embedded in the middle of the resulting string, so we can just `pipe` to `grep` to highlight it, or just `print` and copy


## Note - Solution
The solution was much simpler than I thought it would be, especially with all of the hashing and random `time.time()` calls. It goes to show that we don't always need to understand the entirety of the code, but if we focus on the goal, where the flag is being printed, and just work backwards from that point, we might be able to accomplish the challenge much faster

## Note - submitting byte objects
I'm not really sure why a `bytes object` doesn't submit very well to a python function. I was unable to find a way to submit a `bytes object` encoded correctly, it would simply translate it to a `string` and encoding it again would add additonal `\` to every byte. More than a little frustrating. I ended up just embedding the key and encoded blockchain inside the script

<details><summary>Flag</summary>
    <pre>
    picoCTF{block_3SRhViRbT1qcX_XUjM0r49cH_qCzmJZzBK_8bb7bc38}
    </pre>
   </details>