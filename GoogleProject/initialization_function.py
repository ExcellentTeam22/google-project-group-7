import os

path = r"C:\Users\leele\Desktop\Bootcamp\GoogleProject\Archive"
os.chdir(path)


def read_files(current_file_path, words):
    with open(current_file_path, 'r') as current_file:
        print(current_file.readlines())
        # sentences = list(current_file.readlines())
        # for sentence in sentences:
        #     print(list(sentence))


words = {}

for file in os.listdir():
    if file.endswith('.txt'):
        file_path = f"{path}/{file}"
        read_files(file_path, words)

