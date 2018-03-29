import os
import subprocess

class Episode:

    season = None
    episode_number = 0
    file_path = ''
    file_extension = ''

    def __init__(self, file_path, season, number, extension):
        self.season = season
        self.episode_number = number
        self.file_path = file_path
        self.file_extension = extension

    def rename(self, should_modify):
        new_name = f'{self.season.tv_show.show_name} - s{self.season.season_number:02}e{self.episode_number:02}'
        new_path = f'{os.path.join(os.path.dirname(self.file_path), new_name)}{self.file_extension}'
        if should_modify:
            os.rename(self.file_path, new_path)
            self.file_path = new_path
            return f'[RENAMED] {os.path.basename(self.file_path)} -> {new_name}'
        else:
            return f'Rename {os.path.basename(self.file_path)} -> {new_name}'

    def encode(self, new_extension, should_modify):
        old_file_path = self.file_path

        file_name, _ = os.path.splitext(old_file_path)
        new_file_path = os.path.join(os.path.dirname(old_file_path), f'{file_name}{new_extension}')

        if should_modify:    
            subprocess.run(args=['handbrake', '-i', old_file_path, '--preset', 'H.264 MKV 1080p30', '-o', new_file_path], check=True)
            os.remove(old_file_path)

            self.file_path = new_file_path

            return f'[ENCODED] {new_file_path} [DELETED] {old_file_path}'
        else:
            return f'Encode {new_file_path} Delete {old_file_path}'

    def __str__(self):
        return f'Episode {self.episode_number:02} (s{self.season.season_number:02}) ({self.season.tv_show.show_name})'

    def __repr__(self):
        return self.__str__()