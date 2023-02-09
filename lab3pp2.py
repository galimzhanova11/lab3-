class myclass:
    def __init__(self):
        self.string1=""
    def get_str(self):
        self.string1=input()
    def print_str(self):
        print (self.string1.upper())
        
string1=myclass()
string1.get_str()
string1.print_str()