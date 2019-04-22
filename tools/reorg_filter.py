#!/usr/bin/env python
'''
Pandoc filter that increases the header levels
'''
from panflute import run_filter, Header


def increase_header_level(elem, doc):
    '''
    The filter
    '''
    if type(elem) == Header:
        elem.level += 2


def main(doc=None):
    '''
    An entry point of the program
    '''
    return run_filter(increase_header_level, doc=doc)


if __name__ == '__main__':
    main()
