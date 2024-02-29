import argparse
import os
import datetime


parser = argparse.ArgumentParser(description='Logger')
parser.add_argument('file', type=str, help='File or dir path')
parser.add_argument('data', help='Errors data')
parser.add_argument('text', help='Text in logs')
args = parser.parse_args()
print(args.file, args.data, args.text)


def get_data(file_or_directory):
    date_format = "%Y-%m-%d %H:%M:%S.%f"
    for i in file_or_directory:
        date = datetime.strptime(i[:23], date_format)
        if date:
            print(date)
        elif args.data > data:
            print(args.data + data)
        elif args.data < data:
            print(data - args.data)
        elif args.data == "%Y-%m-%d %H:%M:%S.%f %Y-%m-%d %H:%M:%S.%f":
            print(args.data)
        else:
            print("Это не дата")


def get_str(file_or_directory):
    for i in file_or_directory:
        if i == args.text:
            print(i)
        elif i == args.text and i in args.text:
            print(i)


if os.path.isfile(args.file):
    with open(args.file) as file:
        content = file.read()
        get_data(content)
elif os.path.isdir(args.file):
    for root, dirs, files in os.walk(args.file):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path) as current_file:
                content = current_file.read()
                get_data(content)
else:
    print(f'{args.file} - не является ни файлом, ни папкой')
