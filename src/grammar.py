

import os
import iglob from glob


def fetch_grammar_files(directory):

    if not directory.endsWith('/'):
        directory += '/'


    return iglob(directory + '**/*.g4')


def remove_comments(grammarText):

    pattern = '(<=^\')/\*.*?\*/(

