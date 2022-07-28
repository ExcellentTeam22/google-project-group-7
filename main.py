import Offline
import string
import AutoCompleteData
import re
import jellyfish


def get_candidate_sentences(user_words: list[str], words_not_found: list[int], word_dict: dict) -> set:
    intersecting_sentences = set()

    for word in user_words:
        if word_dict.get(word):
            if not intersecting_sentences:
                intersecting_sentences = word_dict[word]
            else:
                intersecting_sentences = intersecting_sentences.intersection(word_dict[word])
        else:
            words_not_found.append(user_words.index(word))

    return intersecting_sentences


def score_sentences(user_sentence: str, sentence_id: int, completions: list[AutoCompleteData], words_not_found: list,
                    sentence: str, user_words: list[str], sentence_dict: dict):
    score = len(user_sentence) * 2
    reduced_score = 0

    if user_sentence not in sentence_dict[sentence_id][0]:
        if words_not_found[0] == 0:
            guiding_word_offset = 1
        else:
            guiding_word_offset = -1
        sentence_list = sentence.split(" ")
        word_of_sentence = sentence_list[sentence_list.index(user_words[words_not_found[0] + guiding_word_offset])
                                         + (guiding_word_offset * -1)]
        word_of_user = user_words[words_not_found[0]]
        if jellyfish.damerau_levenshtein_distance(word_of_user, word_of_sentence) == 1:
            word_index = 0
            sentence_index = sentence.index(word_of_sentence)
            while word_index in range(min(len(word_of_user), len(word_of_sentence))) \
                    and (sentence_index + word_index) < 4:
                if word_of_user[word_index] != word_of_sentence[word_index]:
                    reduced_score = (5 - (sentence_index + word_index))
                    break
                word_index += 1


            if not reduced_score:
                reduced_score = 1
            if len(word_of_user) != len(word_of_sentence):
                reduced_score *= 2
        else:
            score = 0
    completion = AutoCompleteData.AutoCompleteData(sentence_dict[sentence_id][0], sentence_dict[sentence_id][1],
                                                   0, score - reduced_score)
    print(completion)
    completions.append(completion)


def get_best_k_completions(prefix: str, word_dict: dict, sentence_dict: dict) -> list[AutoCompleteData]:
    user_sentence = re.sub(' +', ' ', str.lower(prefix.translate(str.maketrans('', '', string.punctuation))))
    user_words = user_sentence.split(' ')
    completions = []
    words_not_found = []

    intersecting_sentences = get_candidate_sentences(user_words, words_not_found, word_dict)
    if len(words_not_found) <= 1:
        for sentence_id in intersecting_sentences:
            sentence = re.sub(' +', ' ', str.lower(
                sentence_dict[sentence_id][0].translate(str.maketrans('', '', string.punctuation))))
            score_sentences(user_sentence, sentence_id, completions, words_not_found,
                            sentence, user_words, sentence_dict)
    return completions


if __name__ == '__main__':
    word_dict, sentence_dict = Offline.offline_function()

    user_input = str(input("Enter a sentence, please: "))
    get_best_k_completions(user_input, word_dict, sentence_dict)
