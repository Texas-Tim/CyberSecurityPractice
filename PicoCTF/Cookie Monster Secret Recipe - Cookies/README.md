**Challenge:** Cookie Monster Secret Recipe

**Level:** Easy

**Challenge Author:** Brhane Giday and Prince Niyonshuti N.

### Description: 
Cookie Monster has hidden his top-secret cookie recipe somewhere on his website. As an aspiring cookie detective, your mission is to uncover this delectable secret. Can you outsmart Cookie Monster and find the hidden recipe?

- Web link: ```http://verbal-sleep.picoctf.net:64848/```

We'll start with a quick refresher. Cookies are an essential part of any website. These small bits of data are stored on a users device while browsing and are referenced by the website to "remember" information about the user. This user information can include things such as
* Login credentials
* Preferences
* Session Data
* etc..

#### Types of Cookies
1. Session Cookies:

Temporary cookies that are deleted when the browser is closed.
Used to maintain session state (e.g., keeping a user logged in during a session).

2. Persistent Cookies:

Stored on the user's device for a specified duration.
Used for remembering preferences or login details across sessions.

3. Third-Party Cookies:

Created by domains other than the one the user is visiting.
Commonly used for tracking and advertising purposes.

### Step-by-Step Walkthrough:
This challenge is very straight forward, intending to teach you more that cookies exist than anything else.

#### Cookie location
First, let's check where cookies are stored. To do that, we need to pull up the developer tools on the website, this can be done by either clicking `F12`, or by right clicking and clicking "inspect"

On the developer tools, The cookies we're looking for are stored in either the 
- Network > {page} > Response Header 
or 
- Application > Storage > Cookies 
tab, but at the moment, nothing is there!

In order for a cookie to be stored, we have to interact with the webpage. This can be done simply by attempting to login! Once we do, we'll see the expected secret recipe in one of the previously mentioned locations, but it's encrypted!

```Cooke: cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzc3MUQ1RUIwfQ==```

Hint: If you seee the cookie in a slightly different form, look up the ASCII or Hexadecimal representation of an ```=``` sign

#### Encrypted Cookie
The cookie is encoded in base64, this is given away by the ending ```==``` which is usually a good indicator of this particular algorithm. The symbols are added as padding to ensure the string length is a multiple of 4 characters. Each equal sign represents two bits of zero-padding.

So plug it into your favorite [cryptography tool](https://www.dcode.fr/cipher-identifier), I like the website dcode.fr which has tons of helpful decoders available in many different formats. Once we do, we'll get our flag!

<details><summary>Flag</summary>
    <pre>
    picoCTF{c00k1e_m0nster_l0ves_c00kies_771D5EB0}
    </pre>
   </details>
