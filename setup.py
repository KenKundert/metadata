from setuptools import setup

setup(
    name='metadata',
    description="Edit audio file metadata.",
    author="Ken Kundert",
    author_email='theNurd@nurdletech.com',
    py_modules = 'metadata'.split(),
    python_requires = '>=3.6',
    install_requires = """
        docopt
        inform
        mutagen
        nestedtext
        shlib
        voluptuous
    """.split(),
    scripts='mdexport mdimport'.split(),
    license='GPLv3',
)
