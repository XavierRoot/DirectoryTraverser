import os

banner = '''
-------------------------
       Directory Traverser
-------------------------
Created by Xavier

Traverse directory and output file paths.
'''


excluded_extensions = ['.png', '.jpg', '.svg', '.css','.gif']

directory_path = './'
output_file_path = 'output.txt'

def traverse_directory(path, output_file):
    with open(output_file, 'w') as file:
        for root, dirs, files in os.walk(path):
            for directory in dirs:
                file.write(os.path.join(root, directory) + '\n')
            for file_name in files:
                extension = os.path.splitext(file_name)[1]
                if extension not in excluded_extensions:
                    file.write(os.path.relpath(os.path.join(root, file_name), path) + '\n')



print(banner)
traverse_directory(directory_path, output_file_path)
print(f'\nDirectory traversal completed. The output file is saved at: "{output_file_path}" ')