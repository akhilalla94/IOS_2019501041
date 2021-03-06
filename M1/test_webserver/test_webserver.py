# 1. web server under construction
# 2. other than get is invalid request response with error code
# 3. /index.html, match contents.
# 4. list of directory with files and folders. (html template for printing)
# 5. Handling threads

# 1. /scripts/file.py, check for the output
# 2. /file.py, other than scripts folder
# 3. /scripts/file.py, checking with the parameters in the uri
# 4. /scripts/file.py, infinite loop checking
# 5. Handling threads

# -*- coding: utf-8 -*-
"""Test_webserver.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1--N3SeVNrh6fSAK77MMzrbz-m-MQu6V3
@author Praveen Garimella
@author Laxmi Narayana Murthy
@author Deepak Kumar Reddy
@author Vipul
@author Siva Sankar
"""

# import statements here.
import requests

# driver to run all testcases
def Testcase(r, expstatuscode, expcontenttype, exptext, count):
    print("-----TestCase-" , count, "-----")
    if r.status_code != expstatuscode:
        print (r.status_code, " :: " , expstatuscode)
        print("Wrong status code")
        return False
    if r.headers['Content-Type'] != expcontenttype:
        print("Wrong content-type")
        return False
    if r.text != exptext:
        print(r.text, ": :", exptext)
        print("Wrong content")
        return False
    return True

# Test case
# give your local host and port number here.

# Testcase 1: Checking whether your server is handling requests or not.
# if it handle requests, the default response should be 
# <h1>Webserver Under construction</h1>
# This response should only be sent when the variable 
#enable_directory_browsing is set to False
r = requests.get('http://127.0.0.1:8888')
print()
# print(r.headers)
# print(r.status_code)
# print(r.text)
if Testcase(r, 200, "text/html", "<h1>Webserver Under construction</h1>",1):
	print("Testcase 1 meets the given specificatoin")
else:
	print("Testcase 1 failed")