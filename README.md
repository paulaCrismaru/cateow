[![Build Status](https://travis-ci.org/paulaCrismaru/cateow.svg?branch=master)](https://travis-ci.org/paulaCrismaru/cateow)
[![Coverage Status](https://coveralls.io/repos/github/paulaCrismaru/cateow/badge.svg?branch=master)](https://coveralls.io/github/paulaCrismaru/cateow?branch=master)
# cateow

 ```
  _______________________________________  
< I will sit on your face while you sleep >
  ---------------------------------------  
    \
     \
      ,/|         _.--''^``-...___.._.,;
     /, \'.     _-'          ,--,,,--'''
    { \    `_-''       '    /}
     `;;'            ;   ; ;
 ._.--''     ._,,, _..'  .;.'
  (,_....----'''     (,..--''
```
It's like cowsay but in Python. And with a cat. Saying things. Like cowsay. But in Python.

cats: https://user.xmission.com/~emailbox/ascii_cats.htm

# installation
```sh
$ git clone https://github.com/paulaCrismaru/cateow.git
$ cd cateow
$ pip install .
```

# usage
- Random kitty with a random text.
```sh
$ cateow
```
- Random kitty thinking something random.
```sh
$ cateow --thinks
```
- Random kitty saying "Pet me human!"
**!!! Option `meanie` became deprecated !!!**
~~$ cateow --meanie "Pet me human!"~~
```sh
$ cateow "Pet me human!"
```
- Expect the given kitty saying something random
```sh
$ cateow --kitty /path/to/file/containing/kitty
```
- Random kitty saying something random from the given file
```sh
$ cateow --meanies /path/to/file/containing/mean/stuff
```
~~If both `meanies` and `meanie` options are given, `meanies` will be ignored.~~
If both specified text and `meanie` option are given, `meanies` will be ignored.

- Pipe from standard input
```sh
$ fortune | cateow
```
- Expect a random kitty saying something random from the given file
```sh
$ cateow --meanies /path/to/file/containing/mean/stuff
```

If both `meanies` and `meanie` options are given, `meanies` will be ignored.

# customize
Add your kitties in your next to be favorite folder and add your mean phrases in a demanding file and enjoy the magic.
