**Challenge:** RED

**Level:** Easy

**Challenge Author:** Shuailin Pan (LeConjuror)

### Description: 
RED, RED, RED, RED

### Step-by-Step Walkthrough:
I'm excited for this challenge. The art of hiding data in an image is something I've played around with and want to learn more about.

To start, lets use the tool "exiftool" to extract the metadata of the image

```exiftool red.png```

which returns with:

```
ExifTool Version Number         : 12.76
File Name                       : red.png
Directory                       : .
File Size                       : 796 bytes
File Modification Date/Time     : 2025:04:07 11:54:40-04:00
File Access Date/Time           : 2025:04:07 11:54:41-04:00
File Inode Change Date/Time     : 2025:04:07 11:54:40-04:00
File Permissions                : -rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 128
Image Height                    : 128
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Poem                            : Crimson heart, vibrant and bold,.Hearts flutter at your sight..Evenings glow softly red,.Cherries burst with sweet life..Kisses linger with your warmth..Love deep as merlot..Scarlet leaves falling softly,.Bold in every stroke.
Image Size                      : 128x128
Megapixels                      : 0.016
```

Let's take a closer look at that poem. I'll put it on single lines for easier reference

```
Crimson heart, vibrant and bold,
Hearts flutter at your sight
Evenings glow softly red,
Cherries burst with sweet life.
Kisses linger with your warmth.
Love deep as merlot.
Scarlet leaves falling softly,
Bold in every stroke.
```

The first letter of each section, separated by a ".", spells out: `CHECK LSB`. Now we're sure what we're looking for, let's find a tool or script that can help us

#### Steganography - LSB
Steganography is cloaking a hidden message inside an image or cover message. One way to achieve this is to use the Least Significant Bit (LSB) approach, which entails swapping out the least significant bits of the cover picture with those from the hidden message. 

For example, if we have a 480×480 colour image with the dataset, and we want to hide a secret message of 100 bits within the image using LSB steganography. The LSB approach replaces the least significant bit of each pixel in the image with a bit from the secret message. This results in a slight change in the pixel values that is not easily noticeable to the human eye, but the difference is sufficient to hide the message.

There are a suite of online tools that can assist us, I'll list some of them here. When I was reviewing them, many of them are older, no longer working, etc... So rather than installing a bunch of different tools, Instead I used the Pico Webshell which comes pre-prepared with many of them. Just use ```wget (image URL)``` and you can utilize many of the different tools below

- https://www.aperisolve.com/ - This page was down for me when I tried to visit, but apparently it runs a variety of steganography techniques in easy to read format
- Steghide - only works for jpg, bmp, wav, and AU - just for fun, I tried converting the image into a jpeg and got nothing
- zsteg - only png and bmp - this file is a .png file and zsteg gives us what we need
- binwalk - did nothing for me

I stopped here, as zsteg was able to give me the encoded message, but I was not impressed with the LSB tools that are available

#### Encoded Message
The message was a repeating `base64` encoding, as indicated by the `==` at the end

```
cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==
```

Putting it into a decoder gives me the flag

<details><summary>Flag</summary>
    <pre>
    picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}
    </pre>
   </details>