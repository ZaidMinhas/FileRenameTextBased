import os
import re


class Rename:
    def __init__(self):
        #Original file path
        self.path = ""
        #File names with extension
        self.full_file_names = []
        #file names without extension
        self.file_names = []
        #file extension
        self.ext = ""
        #New file name with extension
        self.new_full_file_names = []

    def SelectFiles(self, path):
        self.path = path + "\\"
        #List all the files in folder
        files = os.listdir(self.path)

        # Regex to split file name and extension
        fileRE = re.compile(r"(.+)\.(.+)$")

        # initialize file name list and find extension
        fileList = [fileRE.findall(file)[0] for file in files]
        self.file_names , file_extensions = zip(*fileList)

        #Check if there are multiple extensions
        self.ext = list(set(file_extensions))
        if len(self.ext) > 1:
            raise TooManyExtensions(self.ext)

        #Set extension and full file names
        self.ext = self.ext[0]
        self.full_file_names = [f"{i}.{self.ext}" for i in self.file_names]

    def ReplaceText(self, find, replace):
        for file in self.file_names:
            new_file = file.replace(find, replace)
            self.new_full_file_names.append(f"{new_file}.{self.ext}")

    def AddText(self, text, placement):
        for file in self.file_names:
            new_file = ""
            if (placement):
                new_file = text + file
            else:
                new_file =  file + text
            self.new_full_file_names.append(f"{new_file}.{self.ext}")


    def FormatText(self, text, number):

        for file in self.file_names:
            new_file = text + str(number)
            number += 1
            self.new_full_file_names.append(f"{new_file}.{self.ext}")

    def ChangeExt(self, new_ext):
        for file in self.file_names:
            self.new_full_file_names.append(f"{file}.{new_ext}")

    def Preview(self):
        for i in range(len(self.file_names)):
            print(f"{self.full_file_names[i]}  => {self.new_full_file_names[i]}")

    def Commit(self):
        if (len(set(self.new_full_file_names)) < len(self.new_full_file_names)):
            raise DuplicationError

        for i in range(len(self.file_names)):
            os.rename(self.path + self.full_file_names[i], self.path + self.new_full_file_names[i])

    def Revert(self):
        for i in range(len(self.file_names)):
            os.rename(self.path + self.new_full_file_names[i], self.path + self.full_file_names[i])


class TooManyExtensions(Exception):
    def __init__(self, ext):
        self.ext = ext
        super().__init__("Too many extensions found: ", self.ext)

class DuplicationError(Exception):
    def __init__(self):
        super().__init__("More than one file share the same new name")