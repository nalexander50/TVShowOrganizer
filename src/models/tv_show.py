import os

class TVShow:

    show_name = ''
    folder_path = ''

    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.show_name = os.path.basename(folder_path)

    def __str__(self):
        return f'{self.show_name}'

    def __repr__(self):
        return self.__str__()