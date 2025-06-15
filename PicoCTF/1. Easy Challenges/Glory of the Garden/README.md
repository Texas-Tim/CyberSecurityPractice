**Challenge:** Glory of the Garden

**Level:** Easy

**Challenge Author:** jedavis/Danny

### Description: 
This garden contains more than it seems.

### Step-by-Step Walkthrough:
To start, we'll follow the steps outlined in [Aperi'Solve](https://www.aperisolve.com/faq)

Since uploading the image nets us an error, we'll have to run through the steps in the faq

First, let's check the file extension using:

`file garden.jpg`

The results are what we would expect so we'll move on.

Second, lets use the tool `exiftool` to extract the metadata of the image

#### Investigation - Image metadata

```exiftool garden.png```

which returns with:

```
ExifTool Version Number         : 12.76
File Name                       : garden.jpg
Directory                       : .
File Size                       : 2.3 MB
File Modification Date/Time     : 2025:06:15 07:11:00-04:00
File Access Date/Time           : 2025:06:15 07:11:01-04:00
File Inode Change Date/Time     : 2025:06:15 07:11:00-04:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Linotronic
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 1998:02:09 06:49:00
Profile File Signature          : acsp
Primary Platform                : Microsoft Corporation
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : Hewlett-Packard
Device Model                    : sRGB
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Hewlett-Packard
Profile ID                      : 0
Profile Copyright               : Copyright (c) 1998 Hewlett-Packard Company
Profile Description             : sRGB IEC61966-2.1
Media White Point               : 0.95045 1 1.08905
Media Black Point               : 0 0 0
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Device Mfg Desc                 : IEC http://www.iec.ch
Device Model Desc               : IEC 61966-2.1 Default RGB colour space - sRGB
Viewing Cond Desc               : Reference Viewing Condition in IEC61966-2.1
Viewing Cond Illuminant         : 19.6445 20.3718 16.8089
Viewing Cond Surround           : 3.92889 4.07439 3.36179
Viewing Cond Illuminant Type    : D50
Luminance                       : 76.03647 80 87.12462
Measurement Observer            : CIE 1931
Measurement Backing             : 0 0 0
Measurement Geometry            : Unknown
Measurement Flare               : 0.999%
Measurement Illuminant          : D65
Technology                      : Cathode Ray Tube Display
Red Tone Reproduction Curve     : (Binary data 2060 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 2060 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 2060 bytes, use -b option to extract)
Image Width                     : 2999
Image Height                    : 2249
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2999x2249
Megapixels                      : 6.7
```

Nothing really going on here, there does seem to be some binary data in the `red, blue, and green` tones, but i'm not sure what to do with this so I'll move on for now.

Next, we'll use a hex editor online with [hexed.it](hexed.it)

#### Investigation - Hex Editor
Upload the file, and although hex editing is beyond my skills right now, I'm going to just do a search of the page for the flag. 

Voila! There it is, hidden in the hex of the image

#### Learning - Hex Editor
Since a hex editor solved the challenge, lets learn a bit mroe about it.

A hexadecimal editor (or hex editor) is a tool that allows you to view and edit the raw binary data of a file, displaying the contents in hexadecimal (base 16) format. For an image, a hex editor lets you see and modify the underlying bytes that make up the image file, including metadata, headers, and pixel data.

Hex editors are useful in CTFs and digital forensics for analyzing or manipulating files at the byte level.

<details><summary>Flag</summary>
    <pre>
    picoCTF{more_than_m33ts_the_3y3657BaB2C}
    </pre>
   </details>