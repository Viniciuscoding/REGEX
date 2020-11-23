"""Detect HTML Attributes


Charlie's second assignment was given by the Professor as soon as he submitted the first one. Professor asked Charlie to create a list of all the attributes
of every tag found in HTML pages.

<p>This is a paragraph</p>  
The above HTML string has p as its tag but no attributes.

<a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a>
This string has a as a tag and href as an attribute.

Input Format

The first line contains N, the number of lines in the HTML fragment. This is followed by lines from a valid HTML document or fragment.

Constraints

Number of characters in the test fragments <= 10000 characters. Characters will be restricted to ASCII. Fragments for the tests will be picked up from Wikipedia.
Attributes are all lowercase alphabets.

Output Format

Each tag must be separated by a newline arranged in lexicographic order
Each attribute noted for a given tag must be arranged next to a tag in lexicographic order.

The output will be of the format

tag-1:attribute-1,attribute-2,attribute-3....
tag-2:attribute-1,attribute-2,attribute-3....
tag-3:attribute-1,attribute-2,attribute-3....
...
tag-n:attribute-1,attribute-2,attribute-3....
Where tag-1 is lexicographically smaller than tag-2 and attribute-1 is lexicographically smaller than attribute-2

Sample Input:1

2
<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>
Sample Output:1

a:href
div:class
p:
Sample Input:2

9
<li style="-moz-float-edge: content-box">... that <a href="/wiki/Orval_Overall" title="Orval Overall">Orval Overall</a> <i>(pictured)</i> is the only <b><a href="/wiki/List_of_Major_League_Baseball_pitchers_who_have_struck_out_four_batters_in_one_inning" title="List of Major League Baseball pitchers who have struck out four batters in one inning">Major League Baseball player to strike out four batters in one inning</a></b> in the <a href="/wiki/World_Series" title="World Series">World Series</a>?</li>
<li style="-moz-float-edge: content-box">... that the three cities of the <b><a href="/wiki/West_Triangle_Economic_Zone" title="West Triangle Economic Zone">West Triangle Economic Zone</a></b> contribute 40% of Western China's GDP?</li>
<li style="-moz-float-edge: content-box">... that <i><a href="/wiki/Kismet_(1943_film)" title="Kismet (1943 film)">Kismet</a></i>, directed by <b><a href="/wiki/Gyan_Mukherjee" title="Gyan Mukherjee">Gyan Mukherjee</a></b>, ran at the <a href="/wiki/Roxy_Cinema_(Kolkata)" title="Roxy Cinema (Kolkata)">Roxy, Kolkata</a>, for 3 years and 8 months?</li>
<li style="-moz-float-edge: content-box">... that <a href="/wiki/Vauix_Carter" title="Vauix Carter">Vauix Carter</a> both coached and played for the <b><a href="/wiki/1882_Navy_Midshipmen_football_team" title="1882 Navy Midshipmen football team">1882 Navy Midshipmen football team</a></b>?</li>
<li style="-moz-float-edge: content-box">... that <a href="/wiki/Zhu_Chenhao" title="Zhu Chenhao">Zhu Chenhao</a> was sentenced to <a href="/wiki/Slow_slicing" title="Slow slicing">slow slicing</a> for leading the <b><a href="/wiki/Prince_of_Ning_rebellion" title="Prince of Ning rebellion">Prince of Ning rebellion</a></b> against the <a href="/wiki/Ming_Dynasty" title="Ming Dynasty">Ming Dynasty</a> <a href="/wiki/Zhengde_Emperor" title="Zhengde Emperor">emperor Zhengde</a>?</li>
<li style="-moz-float-edge: content-box">... that <b><a href="/wiki/Mirza_Adeeb" title="Mirza Adeeb">Mirza Adeeb</a></b> was a prominent modern Pakistani <a href="/wiki/Urdu" title="Urdu">Urdu</a> playwright whose later work focuses on social problems and daily life?</li>
<li style="-moz-float-edge: content-box">... that in <i><b><a href="/wiki/La%C3%9Ft_uns_sorgen,_la%C3%9Ft_uns_wachen,_BWV_213" title="Lat uns sorgen, lat uns wachen, BWV 213">Die Wahl des Herkules</a></b></i>, Hercules must choose between the good cop and the bad cop?<br style="clear:both;" />
<div style="text-align: right;" class="noprint"><b><a href="/wiki/Wikipedia:Recent_additions" title="Wikipedia:Recent additions">Archive</a></b>  <b><a href="/wiki/Wikipedia:Your_first_article" title="Wikipedia:Your first article">Start a new article</a></b>  <b><a href="/wiki/Template_talk:Did_you_know" title="Template talk:Did you know">Nominate an article</a></b></div>
</li>
Sample Output:2

a:href,title
b:
br:style
div:class,style
i:
li:style
"""
# Solution by a_dobeerman
import re
tagAttributes = {}

for _ in range(int(input())):
    for tag, att in re.findall(r'<(\w+)(.*?)?>', input()):
        at = re.findall(r'\s(\w+)=', att)
        if tag in tagAttributes:
            tagAttributes[tag].update(at)
        else:
            tagAttributes[tag] = set(at)
# sep parameter in print does not work in Hackerrack
# print(*sorted(["{}:{}".format(k,",".join(sorted(v))) for k,v in tagAttributes.items()]), sep = '\n')
final = sorted(["{}:{}".format(k,",".join(sorted(v))) for k,v in tagAttributes.items()])
for _4print in final:
    print(_4print)


# Solution by v110_
tags = defaultdict(set)

for _ in range(int(input())):
    for tag, attrs in re.findall(r'<(\w+)(.*?)?>', input()):
        tags[tag].update(
            re.findall(r'\s(\w+)=', attrs)
        )
print(tags)
for tag, attrs in sorted(tags.items()):
    print(tag + ":" + ",".join(sorted(attrs)))
