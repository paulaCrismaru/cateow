[![Build Status](https://travis-ci.org/paulaCrismaru/cateow.svg?branch=master)](https://travis-ci.org/paulaCrismaru/cateow)
# cateow
It's like cowsay but in Python. And with a cat. Saying things. Like cowsay. But in Python.

cats: https://user.xmission.com/~emailbox/ascii_cats.htm

# installation
```sh
$ git clone https://github.com/paulaCrismaru/cateow.git
$ cd cateow
$ pip install .
```

# usage
- Expect a random kitty with a random text.
```sh
$ cateow
```
- Expect the given kitty saying something random
```sh
$ cateow --kitty /path/to/file/containing/kitty
```
- Expect a random kitty saying "Pet me human!"
```sh
$ cateow --meanie "Pet me human!"
```
- Expect a random kitty saying something random from the given file
```sh
$ cateow --meanies /path/to/file/containing/mean/stuff
```

If both `meanies` and `meanie` options are given, `meanies` will be ignored.

# customize
Add your kitties in your next to be favorite folder and add your mean phrases in a demanding file and enjoy the magic.
