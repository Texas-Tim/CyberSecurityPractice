**Challenge:** Scan Surprise

**Level:** Easy

**Challenge Author:** Jeffery John

### Description

I've gotten bored of handing out flags as text. Wouldn't it be cool if they were an image instead?

### Step-by-Step Walkthrough
The challenge provides us a QR code. The goal would be to scan this with some sort of tool. First though, a quick aside about QR codes

#### QR Codes

A QR code (Quick Response code) is a type of two-dimensional barcode that can store information in a grid of color (usually black) and white squares. It is designed to be scanned by a camera or a QR code reader, which decodes the information embedded in the code. QR codes are widely used for various purposes, such as:

* Storing URLs: Quickly directing users to websites.
* Encoding text: Storing plain text, such as messages or contact details.
* Payment systems: Facilitating mobile payments.
* Authentication: Used in two-factor authentication (2FA) systems.
* Tracking: For inventory management or product tracking.

QR codes can store more data than traditional barcodes and are highly versatile. They are commonly scanned using smartphone cameras or dedicated QR code scanners.

#### Solution

The tool I used is called `zbarimg`. You can use your own system, or the webshell provided by Pico. Scan the image with

```
zbarimg flag.txt
```

and voila!

<details><summary>Flag</summary>
    <pre>
    picoCTF{p33k_@_b00_19eccd10}
    </pre>
   </details>