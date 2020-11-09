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

### Using regex with multiple variables in within using re.findall(regex, string)

I solved this question I had on StackOverflow
https://stackoverflow.com/questions/14059596/python-regular-expression-findall-with-variable/64690235#64690235

REGEX
```
re.find(rf'{var1} {var2} ... {varN}', string)
```
PYTHON
```
text = "regex is the best"    
var1 = "is the"
var2 = " best"
yes = re.findall(rf"regex {var1} {var2}", text)
print(yes)
```
RESULT
```
['regex is the best']
```

### Finding all sort of emails
Source: https://en.wikipedia.org/wiki/Email_address#:~:text=The%20general%20format%20of%20an,username%20and%20a%20domain%20name.

**Local-Part**

The local-part of the email address may be unquoted or may be enclosed in quotation marks.

If unquoted, it may use any of these ASCII characters:
```
1. uppercase and lowercase Latin letters A to Z and a to z
2. digits 0 to 9
3. allowed printable characters !#$%&'*+-/=?^_`{|}~
4. only allowed between double quotes \s"(),:;<>@[\]
5. dot ., provided that it is not the first or last character and provided also that it does not appear consecutively (e.g., John..Doe@example.com is not allowed).
If quoted, it may contain Space, Horizontal Tab (HT), any ASCII graphic except Backslash and Quote and a quoted-pair consisting of a Backslash followed by HT, Space or any ASCII graphic; it may also be split between lines anywhere that HT or Space appears. In contrast to unquoted local-parts, the addresses ".John.Doe"@example.com, "John.Doe."@example.com and "John..Doe"@example.com are allowed.
```
The maximum total length of the local-part of an email address is 64 octets.

Note that some mail servers support wildcard recognition of local parts, typically the characters following a plus and less often the characters following a minus, so fred+bah@domain and fred+foo@domain might end up in the same inbox as fred+@domain or even as fred@domain. This can be useful for tagging emails for sorting (see below), and for spam control.[7] Braces { and } are also used in that fashion, although less often.

```
space and special characters "(),:;<>@[\] are allowed with restrictions (they are only allowed inside a quoted string, as described in the paragraph below, and in addition, a backslash or double-quote must be preceded by a backslash);
comments are allowed with parentheses at either end of the local-part; e.g., john.smith(comment)@example.com and (comment)john.smith@example.com are both equivalent to john.smith@example.com.
In addition to the above ASCII characters, international characters above U+007F, encoded as UTF-8, are permitted by RFC 6531, though even mail systems that support SMTPUTF8 and 8BITMIME may restrict which characters to use when assigning local-parts.
```
A local part is either a Dot-string or a Quoted-string; it cannot be a combination. Quoted strings and characters, however, are not commonly used. RFC 5321 also warns that "a host that expects to receive mail SHOULD avoid defining mailboxes where the Local-part requires (or uses) the Quoted-string form".

The local-part postmaster is treated specially—it is case-insensitive, and should be forwarded to the domain email administrator. Technically all other local-parts are case-sensitive, therefore jsmith@example.com and JSmith@example.com specify different mailboxes; however, many organizations treat uppercase and lowercase letters as equivalent. Indeed, RFC 5321 warns that "a host that expects to receive mail SHOULD avoid defining mailboxes where ... the Local-part is case-sensitive".

Despite the wide range of special characters which are technically valid, organisations, mail services, mail servers and mail clients in practice often do not accept all of them. For example, Windows Live Hotmail only allows creation of email addresses using alphanumerics, dot (.), underscore (_) and hyphen (-). Common advice is to avoid using some special characters to avoid the risk of rejected emails.

**Domain**

The domain name part of an email address has to conform to strict guidelines: it must match the requirements for a hostname, a list of dot-separated DNS labels, each label being limited to a length of 63 characters and consisting of:
```
1. uppercase and lowercase Latin letters A to Z and a to z;
2. digits 0 to 9, provided that top-level domain names are not all-numeric;
3. hyphen -, provided that it is not the first or last character.
```
This rule is known as the LDH rule (letters, digits, hyphen). In addition, the domain may be an IP address literal, surrounded by square brackets [], such as jsmith@[192.168.2.1] or jsmith@[IPv6:2001:db8::1], although this is rarely seen except in email spam. Internationalized domain names (which are encoded to comply with the requirements for a hostname) allow for presentation of non-ASCII domains. In mail systems compliant with RFC 6531 and RFC 6532 an email address may be encoded as UTF-8, both a local-part as well as a domain name.

Comments are allowed in the domain as well as in the local-part; for example, john.smith@(comment)example.com and john.smith@example.com(comment) are equivalent to john.smith@example.com.


TEST
```
VALID EMAILS
simple@example.com
very.common@example.com
disposable.style.email.with+symbol@example.com
other.email-with-hyphen@example.com
fully-qualified-domain@example.com
user.name+tag+sorting@example.com (may go to user.name@example.com inbox depending on mail server)
x@example.com (one-letter local-part)
example-indeed@strange-example.com
admin@mailserver1 (local domain name with no TLD, although ICANN highly discourages dotless email addresses[10])
example@s.example (see the List of Internet top-level domains)
" "@example.org (space between the quotes)
"john..doe"@example.org (quoted double dot)
mailhost!username@example.org (bangified host route used for uucp mailers)
user%example.com@example.org (% escaped mail route to user@example.com via example.org)

INVALID EMAILS
Abc.example.com (no @ character)
A@b@c@example.com (only one @ is allowed outside quotation marks)
a"b(c)d,e:f;g<h>i[j\k]l@example.com (none of the special characters in this local-part are allowed outside quotation marks)
just"not"right@example.com (quoted strings must be dot separated or the only element making up the local-part)
this is"not\allowed@example.com (spaces, quotes, and backslashes may only exist when within quoted strings and preceded by a backslash)
this\ still\"not\\allowed@example.com (even if escaped (preceded by a backslash), spaces, quotes, and backslashes must still be contained by quotes)
1234567890123456789012345678901234567890123456789012345678901234+x@example.com (local part is longer than 64 characters)
i_like_underscore@but_its_not_allow_in_this_part.example.com (Underscore is not allowed in domain part)
```
REGEX
```
r(?<=[^a-zA-Z0-9])[a-zA-Z0-9_.-]+@[\w\.]+\.\w+(?=[^a-zA-Z0-9])
MORE ACCURATE -> r(?<=[^a-zA-Z0-9])([a-zA-Z0-9][\"!#$%&'*+/=?^_`{|}~_.-]?[a-zA-Z0-9]?)+@[a-zA-Z0-9-.]+\.\w+(?=[^a-zA-Z0-9])
```
RESULT
```
simple@example.com
very.common@example.com
disposable.style.email.with+symbol@example.com
other.email-with-hyphen@example.com
fully-qualified-domain@example.com
user.name+tag+sorting@example.com (may go to user.name@example.com inbox depending on mail server)
x@example.com (one-letter local-part)
example-indeed@strange-example.com
example@s.example (see the List of Internet top-level domains)
doe"@example.org # This should not be found. I need to write something that catch in between double quotes
mailhost!username@example.org (bangified host route used for uucp mailers)
user%example.com@example.org
1234567890123456789012345678901234567890123456789012345678901234+x@example.com # Should not find this
```

### Finding domains and getting specific groups

IMPORTANT 
```[i.group(0) for i in re.finditer(r'regex', text)]``` is a powerful way to only return certain groups in regular expression.

TEST
```
'<div class="reflist" style="list-style-type decimal;"><ol class="references"><li id="cite_note-1"><span class="mw-cite-backlink"><b>^ ["Train (noun)"](http://www.askoxford.com/concise_oed/train?view=uk). <i>(definition – Compact OED)</i>. Oxford University Press<span class="reference-accessdate">. Retrieved 2008-03-18</span>.</span><span title="ctx_ver=Z39.88-2004&rfr_id=info%3Asid%2Fen.wikipedia.org%3ATrain&rft.atitle=Train+%28noun%29&rft.genre=article&rft_id=http%3A%2F%2Fwww.askoxford.com%2Fconcise_oed%2Ftrain%3Fview%3Duk&rft.jtitle=%28definition+%E2%80%93+Compact+OED%29&rft.pub=Oxford+University+Press&rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal" class="Z3988"><span style="display:none;"> </span></span></span></li><li id="cite_note-2"><span class="mw-cite-backlink"><b>^</b></span> <span class="reference-text"><span class="citation book">Atchison, Topeka and Santa Fe Railway (1948). <i>Rules: Operating Department</i>. p. 7.</span><span title="ctx_ver=Z39.88-2004&rfr_id=info%3Asid%2Fen.wikipedia.org%3ATrain&rft.au=Atchison%2C+Topeka+and+Santa+Fe+Railway&rft.aulast=Atchison%2C+Topeka+and+Santa+Fe+Railway&rft.btitle=Rules%3A+Operating+Department&rft.date=1948&rft.genre=book&rft.pages=7&rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook" class="Z3988"><span style="display:none;"> </span></span></span></li><li id="cite_note-3"><span class="mw-cite-backlink"><b>^ [Hydrogen trains](http://www.hydrogencarsnow.com/blog2/index.php/hydrogen-vehicles/i-hear-the-hydrogen-train-a-comin-its-rolling-round-the-bend/)</span></li><li id="cite_note-4"><span class="mw-cite-backlink"><b>^ [Vehicle Projects Inc. Fuel cell locomotive](http://www.bnsf.com/media/news/articles/2008/01/2008-01-09a.html)</span></li><li id="cite_note-5"><span class="mw-cite-backlink"><b>^</b></span> <span class="reference-text"><span class="citation book">Central Japan Railway (2006). <i>Central Japan Railway Data Book 2006</i>. p. 16.</span><span title="ctx_ver=Z39.88-2004&rfr_id=info%3Asid%2Fen.wikipedia.org%3ATrain&rft.au=Central+Japan+Railway&rft.aulast=Central+Japan+Railway&rft.btitle=Central+Japan+Railway+Data+Book+2006&rft.date=2006&rft.genre=book&rft.pages=16&rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook" class="Z3988"><span style="display:none;"> </span></span></span></li><li id="cite_note-6"><span class="mw-cite-backlink"><b>^ ["Overview Of the existing Mumbai Suburban Railway"](http://web.archive.org/web/20080620033027/http://www.mrvc.indianrail.gov.in/overview.htm). _Official webpage of Mumbai Railway Vikas Corporation_. Archived from [the original](http://www.mrvc.indianrail.gov.in/overview.htm) on 2008-06-20<span class="reference-accessdate">. Retrieved 2008-12-11</span>.</span><span title="ctx_ver=Z39.88-2004&rfr_id=info%3Asid%2Fen.wikipedia.org%3ATrain&rft.atitle=Overview+Of+the+existing+Mumbai+Suburban+Railway&rft.genre=article&rft_id=http%3A%2F%2Fwww.mrvc.indianrail.gov.in%2Foverview.htm&rft.jtitle=Official+webpage+of+Mumbai+Railway+Vikas+Corporation&rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal" class="Z3988"><span style="display:none;"> </span></span></span></li></ol></div>'
```
REGEX
```
r'https?:\/\/(ww[w2]\.)?(([a-zA-Z0-9-]+\.)+[a-zA-Z]+)'
```
RESULT
```
Full domain found
['http://web.archive.org', 'http://www.askoxford.com', 'http://www.bnsf.com', 'http://www.hydrogencarsnow.com', 'http://www.mrvc.indianrail.gov.in']

Group 2
['askoxford.com', 'bnsf.com', 'hydrogencarsnow.com', 'mrvc.indianrail.gov.in', 'web.archive.org']
```
PYTHON
```
Returns the full domain found
domain_full = sorted(set([i.group(0) for i in re.finditer(r'https?:\/\/(ww[w2]\.)?(([a-zA-Z0-9-]+\.)+[a-zA-Z]+)', text)]))

Returns the group 2 in the regular expression (([a-zA-Z0-9-]+\.)+[a-zA-Z]+)
domain_group2 = sorted(set([i.group(2) for i in re.finditer(r'https?:\/\/(ww[w2]\.)?(([a-zA-Z0-9-]+\.)+[a-zA-Z]+)', text)]))
```





