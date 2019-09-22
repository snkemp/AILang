import os
import re
import argparse
import sys
from glob import iglob, glob

pattern = re.compile(r"(?:^/\\*[\\s\\S]*?\\*/)|(?:(?<=[^'])(?:/\\*[\\s\\S]*?\\*/))|(?:^//.*?$)|(?:(?<=[^'])(?://.*?$))")

def process_grammar_files(outfile, skip_multifile_languages=True, include_subdirs=False, remove_comments_bool=True):
    """
    1. Get an iterator over all the grammar files.
    2. Open each one and, based on some command line args, strip comments while writing them to
       another directory (again specified by command line args).
    """
    languages = glob('../ANTLR_GrammarFiles/*') # --> [tsv, tnt]
    subdir = '/**' if include_subdirs else ''
    print('langs: ',languages)
    with open(outfile, 'w') as out:
        for lang in languages:
            lang_name = lang.split('/')[-1]
            grammar_files = glob(lang + subdir + '/*.g4')
            
            # Perhaps skip over languages with multiple files (lexers/parsers). 
            if (skip_multifile_languages and not include_subdirs) and len(grammar_files) > 1:
                continue

            print("num of files: " , len(grammar_files))
            for grammar in grammar_files:
                with open(grammar, 'r') as fi:
                    out.write('// start ' + lang_name + '\n')
                    data = remove_comments(fi.read(), 0 if remove_comments_bool else 1)
                    out.write(data)
                    out.write('// end ' + lang_name + '\n')

def remove_comments(grammarText, count=1):
    global pattern
    return pattern.sub('', grammarText, count=count)

def main(args):
    process_grammar_files(args.outfile,
                          args.skip_multifile,
                          args.include_subdirs,
                          args.remove_comments)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Grammar File Processing')
    parser.add_argument('-s', '--skip-multifile', action='store_true', help='Whether or not to skip langs with multiple g4 files.')
    parser.add_argument('-o', '--outfile', type=str, required=True, help='The name of the output file to collate g4 files to.')
    parser.add_argument('-r', '--include-subdirs', action='store_true', help='Include sub directories of grammar files')
    parser.add_argument('-c', '--remove-comments', action='store_true', help='Remove all comments from the grammar files')
    args = parser.parse_args()
    main(args)