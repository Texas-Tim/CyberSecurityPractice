**Challenge:** endianness

**Level:** Easy

**Challenge Author:** Nana Ama Atombo-Sackey

### Description: 
Know of little and big endian?

### Step-by-Step Walkthrough:

#### What is little and big endian?

Little endian is a way of storing multi-byte data types (like integers) in computer memory where the least significant byte is stored at the lowest memory address, and the most significant byte is stored at the highest address.

Example:
Suppose you have the 4-byte hexadecimal value 0x12345678:

Little endian storage in memory:
Address:   0x00  0x01  0x02  0x03
Value:     78    56    34    12

Big endian is the opposite of little endian where the most significant byte is stored at the lowest memory address, and the least significant byte is stored at the highest address.

Example:
Suppose you have the 4-byte hexadecimal value 0x12345678:

Big endian storage in memory:
Address:   0x00  0x01  0x02  0x03
Value:     12    34    56    78

#### Step 1
Start the instance and `netcat` into the instance. We are presented with a problem: ```You need to find both the little endian and big endian representations of a word.
If you get both correct, you will receive the flag.```

My word was `hujwq`

#### Step 2
Solving the little endianness of hujwq is a little ambiguous. We know that to find our solution, we will need to start with the end and work backwards. However, it's not clear whether you need hexadecimal representation or something else. My first attempt to provide qwjuh as the answer did not work. So let's try the conversion to hex.

Transformation to hex can be done multiple ways, I will use the following: `word.encode().hex()` which results in `68756a7771`. As we've learned this is the Big Endian hex representation of `hujwq`. The Little Endian is just the reverse. Reversing the process we get `71776a7568`

Entering in both answers nets us the flag!

<details><summary>Flag</summary>
    <pre>
    picoCTF{3ndi4n_sw4p_su33ess_d58517b6}
    </pre>
   </details>