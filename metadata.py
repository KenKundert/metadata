# Common data and utilities used by mdexport and mdimport

from inform import warn

metadata_filename = 'metadata.nt'
playlist_filename = 'playlist.m3u'
ogg_extensions = '.ogg'.split()
id3_extensions = '.mp3 .mp4 .m4a'.split()
flac_extensions = '.flac'.split()
music_extensions = ogg_extensions + id3_extensions + flac_extensions
playlist_extension = 'm3u'

map_space_to = '_'

# Required filename mappings (must include slash)
# These mappings always occur
required_filename_string_mappings = {
    ' / ': '; ',
    '/': '-',
}

# Other filename mappings
# These are performed only if user requests filename mapping
optional_filename_string_mappings = {
    "'": '',
    '"': '',
    "!": '',
    ",": '',
    u'\u2019': "'",
#    u'\xe9': "e",
}
aggressive_mapping = False

def use_aggressive_mapping():
    global aggressive_mapping
    aggressive_mapping = True

def map_directory(name):
    if name:
        return map_filename(name)
    return '.'

def map_filename(name):
    name = str(name)
    for bad, good in required_filename_string_mappings.items():
        name = good.join(name.split(bad))
    if aggressive_mapping:
        for bad, good in optional_filename_string_mappings.items():
            name = good.join(name.split(bad))
        #try:
        #    name = name.encode(encoding='ascii', errors='strict')
        #except UnicodeEncodeError:
        #    warn("Illegal character found, search for '&#' to fix", culprit=name)
        #    name = name.encode(encoding='ascii', errors='xmlcharrefreplace')
        name = name.lower().replace(' ', map_space_to)
    return name
