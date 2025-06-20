**Challenge:** flags are stepic

**Level:** Medium

**Challenge Author:** Ricky

### Description: 
A group of underground hackers might be using this legit site to communicate. Use your forensic techniques to uncover their message

### Step-by-Step Walkthrough:


#### Learning - stepic
stepic is a Python library used for steganography, specifically for hiding (encoding) and extracting (decoding) secret messages or data within images. It works by modifying the least significant bits of image pixels to embed information without visibly altering the image.

Example usage:

* Encoding: Hide a message in an image.
* Decoding: Extract a hidden message from an image.
Note:

stepic is an older library and may not be maintained or compatible with the latest versions of Python and PIL/Pillow. For modern projects, consider using updated steganography libraries.

#### Investigation - steganography review
Some common tools for steganography I've used include:

- [aperisolve](https://www.aperisolve.com/)
- `Steghide` - only works for jpg, bmp, wav, and AU
- `zsteg` - only png and bmp

All of the images are `.png` so we'll need to use either `stepic` or `zsteg`. Because the challenge clearly wants you to utilize `stepic`, that's what I'll be doing. 

The first challenge will be doing this in an automated manner. I tried downloading a single image and inspecting it and I didn't notice anything out of the ordinary. There's simply too many to do that for all of them, which means we'll need to scrape the website.

#### Investigation - Web Scraping
I wrote a quick script to connect to the site and download all the images to a local folder 

```
import requests
import re
import os

url = "http://standard-pizzas.picoctf.net:52978/" #change to the appropriate instance port
response = requests.get(url)
js_array = re.findall(r'img:\s*"(flags/[^"]+)"', response.text)\

#create the local directory
os.makedirs("downloaded_flags", exist_ok=True)

for i, img_path in enumerate(js_array):
    img_data = requests.get(url + img_path).content #grab the source of each flag
    filename = os.path.basename(img_path)
    with open(f"downloaded_flags/{filename}", "wb") as f:
        f.write(img_data) #write each flag to my local folder
    print(f"Downloaded {filename}")

```

This will download all of the images to a local folder: `downloaded_flags`

#### Investigation - Stepic
Now it's just a matter of syntax. Iterate over your flag images in the best manner you can. I did it from the CLI. Because of the mass number of images that were not "in the correct format", I used `2>/dev/null` to avoid printing so many error messages, then used `grep` to quickly show the flag.

```
for flag in *.png; do 
echo $flag; 
stepic -d -i "$flag" 2>/dev/null | grep "picoCTF"; 
done
```

<details><summary>Flag</summary>
    <pre>
    picoCTF{fl4g_h45_fl4g6f5548ea}
    </pre>
   </details>