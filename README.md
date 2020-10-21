# REGEX
Practicing with Regular Expressions


### Trimming whitespaces from the beginning and end of a phrase.

TEST
```
"				   The quick brown fox..."
"jumps over the lazy dog.     "
```
REGEX
```
^\s*(.*)[^\s]*$
```
RESULT
```
"The quick brown fox..."
"jumps over the lazy dog."
```


### Matching specific formats such as jpg, jpeg, gif, and png 

TEST
```
.bash_profile
workspace.doc
img0912.jpg
updated_img0912.png
documentation.html
favicon.gif
img0912.jpg.tmp
access.lock
damn.jpeg
```
REGEX
```
^(\w+)\.(jpg|jpeg|gif|png)$
```
RESULT
```
img0912.jpg
updated_img0912.png
favicon.gif
damn.jpeg
```

### Extract the filename, method name and line number from

"at package.class.methodname(filename.linenumber)"

TEST
```
W/dalvikvm( 1553): threadid=1: uncaught exception
E/( 1553): FATAL EXCEPTION: main
E/( 1553): java.lang.StringIndexOutOfBoundsException
E/( 1553):   at widget.List.makeView(ListView.java:1727)
E/( 1553):   at widget.List.fillDown(ListView.java:652)
E/( 1553):   at widget.List.fillFrom(ListView.java:709)
```
REGEX
```
(w+)\(([\w\.]+):(\d+)\)
```
RESULT
```
makeView(ListView.java:1727)
fillDown(ListView.java:652)
fillFrom(ListView.java:709)
```

### Find the URL's Scheme, Host and Port(optional).

URIs, or Uniform Resource Identifiers, are a representation of a resource that is generally composed of a scheme, host, port (optional), and resource path, respectively highlighted below.
scheme://host:port/page -> http://regexone.com:80/page

TEST
```
ftp://file_server.com:21/top_secret/life_changing_plans.pdf
https://regexone.com/lesson/introduction#section
file://localhost:4040/zip_file
https://s3cur3-server.com:9999/
market://search/angry%20birds
```
REGEX
```
(\w+)://([\w\-\.]+)(:(\d+)\)?
```
RESULT
```
ftp://file_server.com:21
https://regexone.com
file://localhost:4040
https://s3cur3-server.com:9999
market://search
```



