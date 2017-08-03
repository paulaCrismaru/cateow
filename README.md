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
- Expect a random kitty saying "Pet me human!"
```sh
$ cateow --meanie "Pet me human,human slave!!"
```

# customize
Add your kitties in the folder [cateow/kitties/](https://github.com/paulaCrismaru/cateow/tree/master/cateow/kitties) and add your mean phrases in the file [cateow/meanies/meanies.mean](https://github.com/paulaCrismaru/cateow/blob/master/cateow/meanies/meanies.mean).
