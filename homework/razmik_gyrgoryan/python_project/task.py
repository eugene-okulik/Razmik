import argparse
import os
import inspect


def find_word_in_code(filename, word_to_find):
    with open(filename, 'r') as source_file:
        source_lines = source_file.readlines()

    for i, line in enumerate(source_lines, start=1):
        if word_to_find in line:
            print(f"Слово '{word_to_find}' найдено в файле '{filename}' на строке {i}")


def main():
    parser = argparse.ArgumentParser(description='Logger')
    parser.add_argument('file', type=str, help='File or dir path')
    parser.add_argument('--text', help='Text in logs')
    args = parser.parse_args()

    if os.path.isfile(args.file):
        find_word_in_code(args.file, args.text)
    elif os.path.isdir(args.file):
        for root, dirs, files in os.walk(args.file):
            for file in files:
                file_path = os.path.join(root, file)
                find_word_in_code(file_path, args.text)
    else:
        print(f'{args.file} - не является ни файлом, ни папкой')
