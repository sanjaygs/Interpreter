# Returns the type and text of the token
# type can be NUMBER,ADD,LEFT_PAREN,EOF etc
# text is the data in the token
class Token:

    def __init__(self, text, type):
        self.text = text
        self.type = type

    def toString(self):
        return "Text: " + self.text + " Type: " + self.type
