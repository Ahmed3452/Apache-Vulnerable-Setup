#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import os

print("Content-Type: text/html;charset=utf-8")
print()  

print("<html>")
print("<head><title>Test CGI Script</title></head>")
print("<body>")
print("<h1>Test Page for Command Injection</h1>")
print("<p>Enter an IP address to ping:</p>")


form = cgi.FieldStorage()
ip = form.getvalue("ip")

print("<pre>")
if ip:
    print(f"--- Pinging {ip} ---")

    os.system(f"ping -c 3 {ip}")
else:
    print("No IP address provided. Use ?ip=127.0.0.1 in the URL.")

print("</pre>")
print("</body>")
print("</html>")
