**Challenge:** CanYouSee

**Level:** Easy

**Challenge Author:** Mubarak Mikail

### Description: 
How about some hide and seek?

### Step-by-Step Walkthrough:
We are provided with an image and a title telling us to seek the hidden flag. Our first step with images should always be to use `exiftool`

## Investigation - exiftool
`run exiftool ukn_reality.jpg`

```
ExifTool Version Number         : 12.76
File Name                       : ukn_reality.jpg
Directory                       : .
File Size                       : 2.3 MB
File Modification Date/Time     : 2025:06:01 14:30:51-04:00
File Access Date/Time           : 2025:06:01 14:30:52-04:00
File Inode Change Date/Time     : 2025:06:01 14:30:51-04:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
XMP Toolkit                     : Image::ExifTool 11.88
Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fYjMyMDQwYjh9Cg==
Image Width                     : 4308
Image Height                    : 2875
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4308x2875
Megapixels                      : 12.4
```

## Investigation - base64 translation
Within the `Attribution URL` we see a string that is quite suspicious with those trailing `==`. That's a common pattern for `base64`, so we can either use an online tool, or run a decoder in the CLI.

run: `echo cGljb0NURntNRTc0RDQ3QV9ISUREM05fYjMyMDQwYjh9Cg== | base64 --decode`

to obtain your flag!

<details><summary>Flag</summary>
    <pre>
    picoCTF{ME74D47A_HIDD3N_b32040b8}
    </pre>
   </details>