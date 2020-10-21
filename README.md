# REGEX
Practicing with Regular Expressions


### Trimming whitespaces from the beginning and end of a phrase.

TEST
"				   The quick brown fox..."
"jumps over the lazy dog.     "

REGEX = ^\s*(.*)[^\s]*$

RESULT
"The quick brown fox..."
"jumps over the lazy dog."



### Matching specific formats such as jpg, jpeg, gif, and png 

TEST
.bash_profile
workspace.doc
img0912.jpg
updated_img0912.png
documentation.html
favicon.gif
img0912.jpg.tmp
access.lock
damn.jpeg

REGEX = ^(\w+)\.(jpg|jpeg|gif|png)$

RESULT
img0912.jpg
updated_img0912.png
favicon.gif
damn.jpeg




