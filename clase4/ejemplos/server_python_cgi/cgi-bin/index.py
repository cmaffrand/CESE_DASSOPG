#!/usr/bin/env python3

# Correr con http://127.0.0.1:8001/cgi-bin/index.py

import cgi
import cgitb; cgitb.enable()

print("Content-Type: text/html\n")
print("<!doctype html><title>Hello</title><h2>prueba cgi python</h2>")

arguments = cgi.FieldStorage()
for i in arguments.keys():
    print(i + "=" + arguments[i].value)