**Challenge:** Bases

**Level:** Easy

**Challenge Author:** Sanjay C/Danny T

### Description: 
What does this `bDNhcm5fdGgzX3IwcDM1` mean? I think it has something to do with bases.

### Step-by-Step Walkthrough:
We have the encoded message above, but how do we recognize which encryption it's using?

#### Learning - Encryption Investigation
To figure out which encryption or encoding is being used, you can:

1. Look for clues in the challenge description or file names (e.g., mentions of `Caesar, ROT13, base64` etc.)
2. Examine the format of the data:
If it uses only `A-Z, a-z, 0-9, +, /, and =`, and is a multiple of 4 in length, it might be `base64`.
3. If it looks like random letters but is readable after shifting letters, it could be a Caesar cipher or ROT cipher.
4. If it’s hexadecimal `(0-9, a-f)`, it could be hex encoding.
5. If it’s a long string of numbers, it might be ASCII codes or binary.
5. Try common decoders: Use online tools like `CyberChef` or `dcode.fr` to test different encodings and ciphers.

If you’re stuck, try decoding with the most common methods first: `base64, hex, ROT13, Caesar, and ASCII`.

Given the hint in the title, we can start with an assumption that it's `base64` or some variant:

#### Learning - base64
You can recognize `base64-encoded` data by these features:

* It uses only the characters: `A-Z, a-z, 0-9, +, /` (sometimes `-, _` for URL-safe `base64`), and `=`, which is used for padding.
* The length is usually a multiple of 4.
* It often ends with one or two `=` signs (padding), but not always.
* The content looks like random letters and numbers, e.g., `U29tZVRleHQ=`, `aGVsbG8=`, etc.

#### Action - Decoding from base64
Linux has a simple method for decoding `base64`:

`echo <string> | base64 -d`

Just replace `<string>` with the encoded message and submit the flag. Remember to input the flag in the correct format!

<details><summary>Flag</summary>
    <pre>
    picoCTF{l3arn_th3_r0p35}
    </pre>
   </details>