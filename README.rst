MetaData
========

A pair of programs used to make it easy to update the metadata of audio files 
(mp3, mp4, m4a, ogg, and flac files).

The first program, *mdexport* extracts the metadata from a collection of audio 
files and stores it in a `NestedText <https://nestedtext.org>`_ file, 
``metadata.nt``.  You would then edit this file to correct the metadata, then 
run *mdimport*, which updates the metadata in each of the files and renames the 
files in a way consistent with the new metadata. In this way, you can clean up 
a large library of audio files efficiently.

Requires Python 3.6 or later.  You will need install the mutagen package for 
python.  To do so, add root, run::

    yum install python-mutagen

mdexport
--------
To change the metadata for audio files run::

    mdexport *.ogg

The program supports .ogg, .mp3, and .flac files. It also supports .m3u 
playlists and directories.  If you specify a playlist, all of the music files 
referenced in the play list are read. If you specify a directory, all of the 
music files, playlists and directories in that directory are included.  
*mdexport* creates ``metadata.nt`` that includes all of the metadata.

You can create a playlist using the original file names using::

    mdexport -p *.ogg

mdimport
--------
Edit the metadata listed in ``metadata.nt`` to what you want it to be. Then 
run::

    mdimport

Besides updating the metadata, it will also rename the audio files so that they 
comply with the standard I have chosen.

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
