#!/usr/bin/env python
'''
Scaffolds the lesson
'''
import os
import sys


def ask(about):
    return


def create(name, fname, content):
    if os.path.exists(fname):
        print('{} exists: skipped.'.format(fname))
        return
    if input('Create ' + name + '? [Y/n]:')[:1].lower() == 'n':
        return
    with open(fname, 'w') as f:
        f.write(content)


def main():
    '''
    An entry point
    '''
    print('Scaffolding...')
    create('spec', 'spec.yml', '''---
lesson:
  name: TODO
  goal: TODO
''')
    create('questions', 'questions.yml', '''---
questions:
  TODO:
    type: answers
    question: |
      TODO
    answers:
      wrong:
        - TODO
      correct:
        - TODO
''')
    sys.exit(0)


if __name__ == '__main__':
    main()
