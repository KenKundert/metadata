from setuptools import setup
from textwrap import dedent

# Create/update manpage before installling
#import manpage
#manpage.write()

setup(
    name='metadata'
  , description=dedent("""\
        Edit audio file metadata.
    """)
  , author="Ken Kundert"
  , author_email='theNurd@nurdletech.com'
  , scripts=['mdexport', 'mdimport']
)
