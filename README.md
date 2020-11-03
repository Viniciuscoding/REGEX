# REGEX
Practicing with Regular Expressions

**\w** -> word characters are defined as: English alphabetic characters [a-zA-Z], decimal digits [0-9] and underscore "_"



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

### Finding IP Addresses (IPv4)

TEST
```
121.18.19.20
111.218.219.290
2001:0db8:0000:0000:0000:ff00:0042:8329  
21:db8:0:0:0:ff00:42:8320
255.255.255.255
198.12.128.27
0.0.0.0
00.00.00.00
000.000.000.000
011.022.033.044
001.002.003.004
110.220.110.220
101.202.103.244
2.2.2.144
100.100.100.100
02.02.02.144
22.02.02.144
This is a character O not a number 0 in the IP O.255.123.12
198.12.128.255
198.255.128.001
this is my IP: 198.12.128.125
Wow her/his IP address is 255.0.255.11? No way!!!!
The IP 0.255.123..12 has a typo
```
REGEX
```
\b(([01]?\d{1,2}?\.){1}|(2[0-5]{2}\.){1})(([01]?\d{1,2}?\.){1}|(2[0-5]{2}\.){1})(([01]?\d{1,2}?\.){1}|(2[0-5]{2}\.){1})(([01]?\d{1,2})|(2[0-5]{2}))\b

This codeline removes IPs with zeros anteceding a digit such as 001.001.001.255, 0.0.0.0 or 000.001.002.255
\b((((?!0)([01]?\d))?\d\.)|(2[0-5]{2}\.)){3}((((?!0)([01]?\d))?\d)|(2[0-5]{2}))\b
```
RESULT
```
121.18.19.20
255.255.255.255
198.12.128.27
0.0.0.0
110.220.110.220
101.202.103.244
2.2.2.144
100.100.100.100
198.12.128.255
this is my IP: 198.12.128.125
Wow her/his IP address is 255.0.255.11? No way!!!!
```

### Finding IP Addresses (IPv6)

TEST
```
2001:0db8:0000:0000:0000:ff00:0042:8329  
21:db8:0:0:0:ff00:42:8320
ffff:ffff:ffff:1000:42:8320:7
ffff:ffff:ffff:0001:0002:0003:0004
ffff:ffff:ffff:001:02:0300:0040
255.255.255.255
198.12.128.27
0.0.0.0
is 21:db8:0:1:2:ff00:42:8320 this IPv4 or IPv6
```
REGEX
```
\b([a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}\b
```
RESULT
```
2001:0db8:0000:0000:0000:ff00:0042:8329  
21:db8:0:0:0:ff00:42:8320
ffff:ffff:ffff:1000:42:8320:7
ffff:ffff:ffff:0001:0002:0003:0004
ffff:ffff:ffff:001:02:030:040:0002 THIS SHOULD FAIL [NEED TO IMPROVE THIS CODE]
is 21:db8:0:1:2:ff00:42:8320 this IPv4 or IPv6
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

### Positive Lookahead (?=)
by Hackerrank (https://www.hackerrank.com/challenges/positive-lookahead/problem)

**regex1(?=regex2)**<br />
The positive lookahead (?=) asserts **regex1** to be immediately followed by **regex2**. The lookahead is excluded from the match. It does not return matches of **regex2**. The lookahead only asserts whether a match is possible or not.

TEST
```
goooool!
look at that
coooolio
cool beans
ooo|o(0.*)ooo|o
very goood
```
REGEX
```
r'o(?=o{2})'
```
RESULT
```
goooool! -> ooo
coooolio -> oo
ooo|o(0.*)ooo|o -> o o
very goood -> o
```

### Negative Lookahead (?!)
by Hackerrank https://www.hackerrank.com/challenges/negative-lookahead/problem <br />

**regex_1(?!regex_2)**<br />
The negative lookahead (?!) asserts **regex_1** not to be immediately followed by **regex_2**. Lookahead is excluded from the match (do not consume matches of **regex_2**), but only assert whether a match is possible or not.

Write a regex which can match all characters which are not immediately followed by that same character.
Example: If = goooo, then regex should match goooo. Because the first g is not follwed by g and the last o is not followed by o.

TEST
```
loooooooooooooool
goooool!
coooolio
goooo
ooops
cool
```
REGEX
```
(.)(?!\1)
```
RESULT
```
loooooooooooooool -> lol
goooool! -> gol!
coooolio -> colio
goooo -> go
ooops -> ops
cool -> col
```

### Positive Lookbehind (?<=)
by Hackerrank

**(?<=regex_2)regex_1**<br />
The positive lookbehind **(?<=)** asserts **regex_1** to be immediately preceded by **regex_2**. Lookbehind is excluded from the match (do not consume matches of **regex_2**), but only assert whether a match is possible or not.

Write a regex which can match all the occurences of digit which are immediately preceded by odd digit.

TEST
```
he13o
123Go!
```
REGEX
```
(?<=[013579])\d
```
RESULT
```
he31o -> 1
123Go! -> 2
```

### Negative Lookbehind (?<!)

**(?<!regex_2)regex_1**<br />
The negative lookbehind (?<!) asserts **regex_1** not to be immediately preceded by **regex_2**. Lookbehind is excluded from the match (do not consume matches of **regex_2**), but only assert whether a match is possible or not.

TEST
```
1o1s
a23upp
ppppp
aeioull
```
REGEX
```
r'(?<![aeiouAEIOU]).'
```
RESULT
```
1os
a3up
ppppp
al
```

### Finding HTLM tags: ```<a> <p> <t> <dir> <h1> </p> </t> </a> </dir> <p/>```

NOTE: This solution only looks for the opening tag rather than both opening and ending tags. If you want to find the context within the tags than the ending tag must be found as well. 

TEST
```
html = '<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p> \
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>"'
```
REGEX
```
r'(?<=<\/?)\w+' # If the regex only supports lookahead fixed-width pattern the use the bellow patterns
r'(?<=<)\w+|\w+(?=>)' or r'(?<=<)\w+|(?<=</)\w+' # positive lookbehind + positive lookahead or positive lookbehind + positive lookbehind

This solution keeps the <>
r'<\/?\w+\/?>?'
```
PYTHON
```
print(';'.join(sorted(set(re.findall('(?<=<)\w+', html)))))
print(re.findall('(?<=<)\w+', html)))
```
RESULT
```
a;div;p
['<p>', '<a', '</a>', '</p>', '<div', '<a', '</a>', '</div>']
```

### Finding a word which ignores space and end of line or other symbols

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



TEST
```

```
REGEX
```

```
RESULT
```

```






