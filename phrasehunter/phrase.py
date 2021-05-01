class Phrase():
    def __init__(self, phrase):
        self.phrase = phrase
        display_pha = []
        for word in phrase:
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

    def check_letter(self, input_letter):
        for word in self.phrase:
            for letter in word:
                if letter == input_letter:
                    return False
        return True

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


array = (('T', 'h', 'a', 'n', 'o', 's'), ('f', 'i', 'g', 'h', 't', 's'))
phrase = Phrase(array)
phrase.display()
phrase.set_letter('s')
phrase.display()
