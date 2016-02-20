from core import (
    drive, DIR_MIME_TYPE, GOOGLE_APPS_MIME_TYPE_STEM,
    format_owner_names, format_mime_type, format_title,
    gen_paths
)
import os
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument('paths', metavar='path', nargs='*', type=str)
parser.add_argument('-r', action='store_true')
ns = parser.parse_args()


for (abspath, relpath) in gen_paths(ns.paths):
    entry_id = 'root'
    if relpath:
        relpath_pieces = relpath.split('/')
        for title in relpath_pieces:
            entries = drive.ListFile({'q': "'%s' in parents and title='%s' and trashed=false" % (entry_id, title)}).GetList()
            if len(entries) < 1:
                raise Exception('%s does not exist' % title)
            elif len(entries) > 1:
                raise Exception('%s has more than one parent?' % title)
            entry_id = entries[0]['id']
            if "'" in entry_id:
                raise Exception('%s has evil id %s' % (entries[0]['title'], entry_id))

    f = drive.CreateFile({'id': entry_id})
    f.GetContentFile(abspath)
