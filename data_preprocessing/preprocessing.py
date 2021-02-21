import re
class PreProcessing:
    def __init__(self,data):
        self.data=data
    def remove_new_line(self):
        self.data=self.data.replace('\n',' ')
        return self
    def remove_punctuation(self):
        self.data=re.sub('[^A-Za-z]+', ' ',self.data)
        return self
    def remove_multiple_space(self):
        self.data = re.sub(' +', ' ', self.data)
        return self

