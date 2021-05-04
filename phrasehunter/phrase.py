class Phrase:
    def __init__(self, phrase):
        lower_phrase = phrase.lower()
        split_phrase = lower_phrase.split(" ")

        words_array = []
        for word in split_phrase:
            letters_array = []
            for letter in word:
                letters_array.append(letter)
            words_array.append(letters_array)

        self.phrase = words_array
        display_pha = []
        for word in words_array:
            word_size = len(word)
            current_word = []
            while word_size != 0:
                current_word.append('_')
                word_size -= 1
            display_pha.append(current_word)

        self.displayed_phrase = display_pha

    def display(self):
        phrase_string = ""
        for word in self.displayed_phrase:
            phrase_string = phrase_string + "   " + " ".join(word)
        print(phrase_string)

    def display_answer(self):
        phrase_string = ""
        for word in self.phrase:
            phrase_string = phrase_string + "   " + " ".join(word)
        print(phrase_string)

    def check_letter(self, input_letter):
        for word in self.phrase:
            for letter in word:
                if letter == input_letter:
                    return True
        return False

    def set_letter(self, input_letter):
        word_position = -1
        for word in self.phrase:
            word_position += 1
            letter_position = -1
            for letter in word:
                letter_position += 1
                if letter == input_letter:
                    self.displayed_phrase[word_position][letter_position] = input_letter

    def check_complete(self):
        for word in self.displayed_phrase:
            for letter in word:
                if letter == '_':
                    return False
        return True

    def reset(self):
        display_pha = []
        for word in self.phrase:
            word_size = len(word)
            current_word = []
            while word_size != 0:
                current_word.append('_')
                word_size -= 1
            display_pha.append(current_word)
        self.displayed_phrase = display_pha
