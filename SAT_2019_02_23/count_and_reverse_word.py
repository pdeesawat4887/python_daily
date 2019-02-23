class Sentence:

    def __init__(self):
        self.option = int(input("Enter option 1[file] or 2[typing]: "))
        self.statements = {
            1:self.read_file,
            2:self.read_typing,
        }
        self.work(self.statements[self.option]())

    def read_file(self):
        file_name = input("Enter your path and file name: ")
        file_handle = open(file_name, 'r')
        temp_str = ""
        while True:
            line = file_handle.readline()
            if not line:
                break
            temp_str += line
        file_handle.close()
        return temp_str

    def read_typing(self):
        return input("Enter your sentence: ")

    def work(self, input_str):
        self.convert_to_list(input_str)
        self.count_word()
        self.reverse_sentence()

    def convert_to_list(self, input_str):
        self.string = input_str.split(" ")

    def count_word(self):
        self.word_count = set(self.string).__len__()
        print("Number of words in your sentence is {count}.".format(count=self.word_count))

    def reverse_sentence(self):
        temporary = " ".join(self.string[::-1])
        print("Reversed sentence is : {reverse}".format(reverse=temporary))


sentence = Sentence()
