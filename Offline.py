import os
import string

path = r"C:\Users\leele\Desktop\Bootcamp\google-project-group-7\MyArchive/"
os.chdir(path)


def add_to_word_dict(word: str, word_dict: dict, sentence_id: int) -> None:
    alpha_num_word = str.lower(word.translate(str.maketrans('', '', string.punctuation)))
    if alpha_num_word not in word_dict:
        word_dict[alpha_num_word] = set()
    word_dict[alpha_num_word].add(sentence_id)


def read_file(current_file_path: str, word_dict: dict, sentence_dict: dict) -> None:
    with open(current_file_path, encoding="utf8") as current_file:
        sentences = list(current_file.readlines())
        for sentence in sentences:
            sentence = sentence.strip('\n')
            sentence_id = hash(sentence)
            sentence_dict[sentence_id] = (sentence, current_file_path)
            words_of_sentence = list(filter(None, sentence.split(' ')))
            for word in words_of_sentence:
                add_to_word_dict(word, word_dict, sentence_id)
        current_file.close()


def offline_function() -> tuple[dict, dict]:
    word_dict = {}
    sentence_dict = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                read_file(file_path, word_dict, sentence_dict)
    return word_dict, sentence_dict


# if __name__ == '__main__':
#     word_dict, sentences_dict = offline_function()
#     for word in word_dict:
#         print(f"{word}: {word_dict[word]}")
#     for sentence in sentences_dict:
#         print(f"{sentence}: {sentences_dict[sentence]}")
