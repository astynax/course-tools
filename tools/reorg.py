#!/usr/bin/env python
'''
Org-to-Markdown exporter
'''
from os import scandir, path
import plumbum


PANDOC = plumbum.local['pandoc']


def pandoc(source, destination):
    '''
    Pandoc program wrapper
    '''
    return PANDOC[
        source,
        '-t', 'gfm',
        '-o', destination,
        '--filter', 'reorg-filter'
    ].run(retcode=None)


def main():
    '''
    program's entry point
    '''
    print("Working in {}".format(
        path.split(path.abspath(path.curdir))[1]
    ))

    files = {e.name: e for e in scandir('.') if e.is_file()}

    for source, spec in files.items():
        name, ext = path.splitext(source)
        if not ext.lower() == '.org':
            continue
        print('Processing {}...'.format(source))
        destination = name + path.extsep + 'md'
        dspec = files.get(destination)
        # check for existance and compare modification times
        outdated = not dspec or (
            dspec and dspec.stat().st_mtime < spec.stat().st_mtime
        )
        if not outdated:
            print('...skipped.')
            continue
        (exit_code, _, err) = pandoc(source, destination)
        if exit_code:
            print('...failed with:')
            print(err)
            break


if __name__ == '__main__':
    main()
