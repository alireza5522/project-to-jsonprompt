from setuptools import setup

setup(
    name='makejson-cli',
    version='0.1.0',
    py_modules=['makejson'],
    install_requires=[
        'click',
        'pathspec',
    ],
    entry_points={
        'console_scripts': [
            'makejson=makejson:cli',
        ],
    },
)