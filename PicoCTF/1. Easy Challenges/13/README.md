**Challenge:** 13

**Level:** Easy

**Challenge Author:** Alex Fulton/Daniel Tunitis

### Description: 
Cryptography can be easy, do you know what ROT13 is? cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}

### Step-by-Step Walkthrough:
The flag is provided to us in the description, but it's been encoded using ROT13!

#### Learning - ROT
`ROT ciphers` (short for "rotate ciphers") are more commonly known as a `Caesar cipher` are a type of substitution cipher where each letter in the plaintext is shifted by a fixed number of positions in the alphabet. The most common example is `ROT13`, which shifts each letter by 13 places. For example, A becomes N, B becomes O, and so on. Applying `ROT13` twice returns the original text.

It's probably faster to use an online tool such as [dcode](https://www.dcode.fr/caesar-cipher), but I'm going to teach you how to do it using the `tr` command

#### Learning - tr
tr is a command-line utility in Unix/Linux used to translate, replace, or delete characters from standard input and write the result to standard output. It is often used for simple text transformations, such as changing letter case or applying ciphers like ROT13.

Example:

`echo "hello" | tr 'a-z' 'A-Z'`

To decode our flag, we can translate 13 spaces using the following code:

`echo "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}" | tr 'A-Za-z' 'N-ZA-Mn-za-m'`

Congratulations! We have our flag

<details><summary>Flag</summary>
    <pre>
    picoCTF{not_too_bad_of_a_problem}
    </pre>
   </details>