import os

banner = '''
-------------------------
       Directory Traverser
-------------------------
Created by Xavier

Traverse directory and output dirs paths.
本脚本只输出目录路径
'''

directory_path = './'
output_file_path = 'dirs.txt'

def traverse_directory(path, output_file):
    with open(output_file, 'w') as file:
        for root, dirs, files in os.walk(path):
            for directory in dirs:
                file.write(os.path.join(root, directory) + '\n')



print(banner)
traverse_directory(directory_path, output_file_path)
print(f'\nDirectory traversal completed. The output file is saved at: "{output_file_path}" ')