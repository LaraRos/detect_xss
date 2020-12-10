# detect_xss
A quick example of detecting malicious XSS strings using kNN

Made with Python.

## Some quick examples
* `hello`
* `<script>alert(${document.cookie})</script>`
* `<IMG SRC=&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041>`
