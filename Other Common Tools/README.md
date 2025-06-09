## Resources

#### [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master)
Repository for common injection tools


### zbarimg
zbarimg is a command-line tool that scans image files for barcodes or QR codes and prints the decoded data to standard output. It supports various barcode formats, including QR codes, EAN, UPC, and Code 128.

The following command will scan `image.png` for any barcodes or QR codes and display the decoded information.

- zbarimg <file>

### exiftool
exiftool is a command-line application used to read, write, and edit metadata in image, audio, and video files. It supports a wide variety of file formats and can extract information such as camera settings, timestamps, GPS data, and more from files.

This command will display all metadata found in `image.jpg`.

- `exiftool <image.jpg>`

### Checksec
checksec is a command-line tool used to analyze the security properties of executable files such as

* ELF binaries on Linux 

It checks for the presence of various security features such as stack canaries: 

* NX (No eXecute) bit
* PIE (Position Independent Executable)
* RELRO (Relocation Read-Only)

and more.

The following command will display which security protections are enabled for the specified `binary`.
- `checksec --file <binary>`

### Base64 encode/decode
Base64 is an encoding scheme used to represent binary data as ASCII text. It converts binary data into a set of 64 printable characters (A-Z, a-z, 0-9, +, and /), making it safe to transmit over text-based protocols like email or HTTP. Base64 is commonly used to encode files, images, or other binary data for embedding in text documents or web pages.

Base64 uses only the characters: A-Z, a-z, 0-9, +, / (sometimes - and _ for URL-safe base64), and =, which is used for padding at the end. It often ends with one or two = signs (padding), but not always.

Example usage in the console:

- `echo -n "hello" | base64`

Output: `aGVsbG8=`

Decode example:

- `echo "aGVsbG8=" | base64 -d`

Output: `hello`

Whenever using base64 decoding with multiple layers, one hint is that the resulting decoded string will be "shorter" then the original. If it's not, it may not be base64 or you may have forgot the `-d` flag

### Least Significant Bit (LSB)
Steganography is cloaking a hidden message inside an image or cover message. One way to achieve this is to use the Least Significant Bit (LSB) approach, which entails swapping out the least significant bits of the cover picture with those from the hidden message. 

For example, if we have a 480×480 colour image with the dataset, and we want to hide a secret message of 100 bits within the image using LSB steganography. The LSB approach replaces the least significant bit of each pixel in the image with a bit from the secret message. This results in a slight change in the pixel values that is not easily noticeable to the human eye, but the difference is sufficient to hide the message.

The following are tools for solving lsb challenges

- [aperisolve](https://www.aperisolve.com/) - This page runs a variety of steganography techniques in easy to read format
- Steghide - only works for jpg, bmp, wav, and AU
- zsteg - only png and bmp
- binwalk - unsure