# Welcome to your coding challenge!

"""
The goal of this coding challenge is to create a simple program that can be
executed from the command line which will call a fake method get_data(),
turn the results into instances of 2 classes you define, and print the results.

Please modify the class definitions and/or create new classes, but don't
modify the main() or get_data() functions (you can edit them to troubleshoot
but they should be unchanged in your submission). Bonus points if you include
a shell script and/or readme describing the creation of your python
environment.

The output should look like this:

R Smith M.D. ID_123 is the doctor for: Mr. Mem Burr
J Brown M.D. PhD ID_234 is the doctor for: Mrs. Pay Shent
"""

import pandas as pd


class Member():

    #def __init__(self, mem_id, name, title):
        #self.id = mem_id
        #self.title = title
        #self.name = name

    def __init__(self, *args):
        self.id = args[0]
        self.title = args[2]
        self.name = args[1]
    
    def __str__(self):
        return self.title + " " + self.name



class Doctor():

    #def __init__(self, doc_id, name, title):
        #self.id = doc_id
        #self.title = title
        #self.name = name

    def __init__(self, *args):
        self.id = args[0]
        self.title = args[2]
        self.name = args[1]
    
    def __str__(self):
        return self.name + " " + self.title + " " + self.id


def get_data():
    docs_and_mems = []
    data = pd.read_csv("fake_data.csv")
    for n, row in data.iterrows():
        mem = Member(row["member_id"], row["member_name"], row["member_title"])
        doc = Doctor(row["doc_id"], row["doc_name"], row["doc_title"])
        docs_and_mems.append((doc, mem))
    return docs_and_mems

if __name__ == "__main__":
    docs_and_mems = get_data()
    for doc, mem in docs_and_mems:
        print(str(doc)+' is the doctor for: '+str(mem))