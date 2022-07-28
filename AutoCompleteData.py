class AutoCompleteData:
    def __init__(self, completed_sentence, source_text, offset, score):
        self.completed_sentence = completed_sentence
        self.source_text = source_text
        self.offset = offset
        self.score = score

    def my_function(self):
        print(self.completed_sentence, self.source_text, self.offset, self.score)

    def __str__(self):
        return f"sentence: {self.completed_sentence}, source: {self.source_text}," \
               f"offset: {self.offset}, score: {self.score}"
