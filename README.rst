mdexport
========
To change the metadata for audio files run::

    mdexport *.ogg


The program supports .ogg, .mp3, and .flac files. It also supports .m3u 
playlists and directories.  It creates data.py.

You can create a playlist using the original file names using::

    mdexport -p *.ogg

mdimport
========
Edit the metadata listed in data.py to what you want it to be. Then run::

    mdimport

Besides updating the metadata, it will also rename the file so that it complies 
with the standard I have chosen.

Use::

    mdimport -a

to have it create directories for each of the albums and move the files into 
those directories

Use::

    mdimport -A

to have it create directories for the artist and within those directories for 
each of the albums and move the files into these directories.

You can create a playlist using the new file names using::

    mdexport -p *.ogg
