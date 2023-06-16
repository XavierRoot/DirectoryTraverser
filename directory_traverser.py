#!/usr/bin/env python3
#-*- coding utf-8 -*-

import argparse
from tqdm import tqdm
import os

banner = '''
-------------------------
     Directory Traverser
-------------------------
Traverse directory and output file paths.
Created by Xavier
'''

default_excluded_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.css', '.swf']
default_included_extensions = []

def traverse_directory(path, output_file, excluded_extensions=[], included_extensions=[]):
    file_count = sum(len(files) for _, _, files in os.walk(path))
    progress_bar = tqdm(total=file_count, desc='Progress', unit='file')
    num=0

    with open(output_file, 'w') as file:
        for root, dirs, files in os.walk(path):
            for directory in dirs:
                file_path = os.path.relpath(os.path.join(root, directory), path)
                file.write(f'{file_path}\n')

            for file_name in files:
                progress_bar.update(1)
                extension = os.path.splitext(file_name)[1]

                if excluded_extensions and extension in excluded_extensions:
                    continue

                if included_extensions and extension not in included_extensions:
                    continue

                file_path = os.path.relpath(os.path.join(root, file_name), path)
                file.write(f'{file_path}\n')
                num += 1                

    progress_bar.close()
    print(f'\n[*] find {num}/{file_count} files.')


def main():
    parser = argparse.ArgumentParser(prog='directory_traverser', description='Traverse directory and output file paths.')

    parser.add_argument('directory_path', metavar='directory_path', type=str, help='the directory path to traverse')
    parser.add_argument('-o', '--output', metavar='output_file', type=str, default='output.txt',
                        help='the output file path (default: output.txt)')
    parser.add_argument('-x', '--x_extensions', metavar='x_extensions', type=str,
                        help='additional excluded file extensions (comma-separated),\neg: \'-x js,css\'')
    parser.add_argument('-e', '--extensions', metavar='extensions', type=str,
                        help='only use these file extensions (comma-separated),  eg: \'-e php,jsp,html\'')

    args = parser.parse_args()

    if args.extensions and args.x_extensions:
        parser.error('\n[!] -x and -e options are mutually exclusive. Please use either -x or -e.')
        

    included_extensions = default_included_extensions
    excluded_extensions = default_excluded_extensions

    if args.extensions:
        included_extensions += [ext if ext.startswith('.') else f'.{ext}' for ext in args.extensions.split(',')]

    if args.x_extensions:
        excluded_extensions += [ext if ext.startswith('.') else f'.{ext}' for ext in args.x_extensions.split(',')]

    print('[+] Exclude_extends:', ', '.join(excluded_extensions))
    print('[+] Include_extends:', ', '.join(included_extensions))
    print()
    traverse_directory(args.directory_path, args.output, excluded_extensions, included_extensions)

    print(f'\n[*] Directory traversal completed. The output file is saved at: "{args.output}"')


if __name__ == '__main__':
    print(banner)
    main()
