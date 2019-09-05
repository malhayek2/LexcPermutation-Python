# Permutation
Generating the Next Permutation in Lexicographic Order
##### What is Lexicographic Order? 
I think it is the next largest Permutation, ex [1,2,3] < [1,3,2] < [2,1,3] ...etc
## ALGORITHM
**procedure** next permutation( a <sub>1</sub> a<sub>2</sub> . . . a<sub>n</sub>  : permutation of {1, 2, . . . , n} not equal to n n − 1 . . . 2 1)
j := n − 1
**while** a <sub>j</sub> > a <sub>j+1</sub>
j := j − 1
{j is the largest subscript with a <sub>j</sub> < a <sub>j+1</sub> }
k := n
**while** a <sub>j</sub> > a <sub>k</sub>
k := k − 1
{a <sub>k</sub> is the smallest integer greater than a j to the right of a <sub>j</sub> }
interchange a <sub>j</sub> and a <sub>k</sub>
r := n
s := j + 1
while r > s
interchange a <sub>r</sub> and a <sub>s</sub>
r := r − 1
s := s + 1
***What does it mean??***
Ex 12365
- cacluate the target; left number less than right number. which is 3
- the smallest of the biggest number on the right of it.(5)
- swap them numbers the two numbers => 12563
- order the rest the number from the samellest ot the biggest! ==> 12536
# New Features!

  - Import a HTML file and watch it magically convert to Markdown
  - Drag and drop images (requires your Dropbox account be linked)


You can also:
  - Import and save files from GitHub, Dropbox, Google Drive and One Drive
  - Drag and drop markdown and HTML files into Dillinger
  - Export documents as Markdown, HTML and PDF

Markdor Markdown's syntax, type some text into the left window and watch the results in the right.

### Tech

Dillinger uses a number of open source projects to work properly:

* [AngularJS] - HTML enhanced for web apps!
* [Ace Editor] - awesome web-based text editor
* [markdown-it] - Markdown parser done right. Fast and easy to extend.
* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [node.js] - evented I/O for the backend
* [Express] - fast node.js network app framework [@tjholowaychuk]
* [Gulp] - the streaming build system
* [Breakdance](http://breakdance.io) - HTML to Markdown converter
* [jQuery] - duh

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

### Installation

This application requires python and git.

Install the dependencies in Ubuntu just like this
```
sudo apt-get python3
sudo apt-get git
```
## How to Run
```
python3 ./main.py
```


### Development
Done


### Todos

 - Write MORE Tests

License
----
**Free Software, Hell Yeah!**


