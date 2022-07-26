import os
import string

path = r"C:/Users/leele/Desktop/Bootcamp/GoogleProject/Archive/"
os.chdir(path)


def add_to_word_dict(word: str, word_dict: dict, sentence: str, current_file_path: str) -> None:
    alpha_num_word = word.translate(str.maketrans('', '', string.punctuation))
    if alpha_num_word not in word_dict:
        word_dict[alpha_num_word] = []
    word_dict[alpha_num_word].append((sentence, current_file_path))


def read_files(current_file_path: str, word_dict: dict) -> None:
    with open(current_file_path, 'r') as current_file:
        sentences = list(current_file.readlines())
        for sentence in sentences:
            words_of_sentence = sentence.split(" ")
            for word in words_of_sentence:
                add_to_word_dict(word, word_dict, sentence, current_file_path)
        current_file.close()


def offline_function() -> dict:
    word_dict = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                read_files(file_path, word_dict)
    return word_dict


if __name__ == '__main__':
    word_dict = offline_function()
    for word in word_dict:
        print(f"{word}: {word_dict[word]}")
