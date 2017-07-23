from setuptools import setup


config = {

    'author': 'Paula Crismaru',
    'author_email': 'paula.crismaru@gmail.com',
    'description': 'It\'s like cowsay but in python. '
                    'And with a cat. Saying things. '
                    'Like cowsay. But in python.',


    'name': 'cateow',
    'version': '1.0',
    'packages': ['cateow'],
    'package_data': {
        'cateow': [
            'meanies/*.mean',
            'kitties/*.cat'
        ],
    },
    'install_requires': [
        'Click',
    ],
    'entry_points': {
        'console_scripts': ['cateow=cateow.cateow:cli'],
    }
}

setup(**config)
