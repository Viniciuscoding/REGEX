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

### Find dates (using Word Boundaries)

TEST
```
this is the date 10/2/2011 of all
192.23.128.34 10-02-11 they did that
01-01-2000 or 01 01 20001
what is this 12/2/20 not me
12.21.2001
1 1 2000
1_2_30008
1-12:1956
12-23_20
01---22---2000
```
REGEX
```
\b[012]{1,2}([^a-zA-Z0-9])[0123]{1,2}\1(([12]{1}\d{1})|([12]{1}\d{3}))\b
```
RESULT
```
10/2/2011
10-02-11
01-01-2000
12/2/20
12.21.2001
1 1 2000
```

### Finding Palindromes

This regex palindromes finding is limited to 21 characters long. It excludes words with 1 or 2 characters.

TEST
```
canevacaniseebeesinacave
evacaniseebeesinacave
redrumsirismurder
steponnopets
repaper
rotator
dadier
rotor
mom
mm
s
w
```
REGEX
```
\b(\w)?(\w)?(\w)?(\w)?(\w)?(\w)?(\w)?(\w)?(\w)?(\w){1}\w{1,2}\10\9\8\7\6\5\4\3\2\1\b
```
RESULT
```
evacaniseebeesinacave
redrumsirismurder
steponnopets
repaper
rotator
rotor
mom
ww
```

### Finding IP Addresses

TEST
```
255.255.255.255
198.12.128.27
0.0.0.0
This is a character O not a number 0 in the IP O.255.123.12
198.12.128.255
198.255.128.0
this is my IP: 198.12.128.125
Wow her/his IP address is 255.0.255.11? No way!!!!
The IP 0.255.123..12 has a typo
```
REGEX
```
\b(([01]?\d{1,2}?\.){1}|(2[0-5]{2}\.){1})(([01]?\d{1,2}?\.){1}|(2[0-5]{2}\.){1})(([01]?\d{1,2}?\.){1}|(2[0-5]{2}\.){1})(([01]?\d{1,2})|(2[0-5]{2}))\b
```
RESULT
```
255.255.255.255
198.12.128.27
0.0.0.0
198.12.128.255
198.255.128.0
198.12.128.125
255.0.255.11
```

### Finding lowercase characters that repeats 4 or more times consecutively

TEST
```
fffffff uuuu ccc kk!
Why people say ffff when they are angry
This is the institution IEEE I spoke about.
Zzzzzz
EEEE
fffffggggghhhhdddssa
aaaa nao da nao
bbbbbboa irmao
9999
```
REGEX
```
a{4,}|b{4,}|c{4,}|d{4,}|e{4,}|f{4,}|g{4,}|h{4,}|i{4,}|j{4,}|k{4,}|l{4,}|m{4,}|n{4,}|o{4,}|p{4,}|q{4,}|r{4,}|s{4,}|t{4,}|u{4,}|v{4,}|w{4,}|x{4,}|y{4,}|z{4,}
```
RESULT
```
fffffff uuuu ccc kk!
Why people say ffff when they are angry
Zzzzzz
fffffggggghhhhdddssa
aaaa nao da nao
bbbbbboa irmao
```

### Using FORWARD REFERENCE

**group_2** = tac
**group_1** = **group_2** and tic OR **group_2**

First it will try to match **group_2** and tic but still we didn't captured **group_2** so we don't get it at first place.
So it will match **group_2** == tac [this will make **group_1** == (tactic|tac)] than beacuse of + we can match any alternatives from (tactic|tac) more than 1 times.

TEST
```
tactactic
tactictac
tactactictactic
tactactictactictictac
```
REGEX
```
'^(\2tic|(tac))+$'
```
RESULT
```
tactactic
tactactictactic
```



TEST
```

```
REGEX
```

```
RESULT
```

```



TEST
```

```
REGEX
```

```
RESULT
```

```








