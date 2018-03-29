import os

class Season:
    
    tv_show = None
    season_number = 0
    folder_path = ''

    def __init__(self, folder_path, tv_show, season_number):
        self.tv_show = tv_show
        self.season_number = season_number
        self.folder_path = folder_path

    def rename(self, should_modify):
        new_name = f'Season {self.season_number:02}'
        new_path = os.path.join(os.path.dirname(self.folder_path), new_name)
        if should_modify:
            os.rename(self.folder_path, new_path)
            self.folder_path = new_path
            return f'[RENAMED] {os.path.basename(self.folder_path)} -> {new_name}'
        else:
            return f'Rename {os.path.basename(self.folder_path)} -> {new_name}'

    def __str__(self):
        return f'Season {self.season_number:02} ({self.tv_show.show_name})'

    def __repr__(self):
        return self.__str__()