**Challenge:** information

**Level:** Easy

**Challenge Author:** susie

### Description: 
Files can always be changed in a secret way. Can you find the flag?

### Step-by-Step Walkthrough:
The first step to analyzing an image, should be the tool `exiftool`

## Learning - exiftool
exiftool is a command-line application used to read, write, and edit metadata in image, audio, and video files. It supports a wide variety of file formats and can extract information such as camera settings, timestamps, GPS data, and more from files.

## Investigation - exiftool
run the command: `exiftool cat.jpg`

```
ExifTool Version Number         : 12.76
File Name                       : cat.jpg
Directory                       : .
File Size                       : 878 kB
File Modification Date/Time     : 2025:06:09 05:34:53-04:00
File Access Date/Time           : 2025:06:09 05:34:54-04:00
File Inode Change Date/Time     : 2025:06:09 05:34:53-04:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1
```

Does anything stand out among this list of information?

## Investigation - base64
That License looks like a string that may be encoded. I'm no expert of what should be in the license section, but it certainly feels suspicious to me.

A very common encoding pattern is `base64`. We can run the following command to decode the string and see if we are right:

`echo "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 -d`

And we have our flag!

<details><summary>Flag</summary>
    <pre>
    picoCTF{the_m3tadata_1s_modified}
    </pre>
   </details>