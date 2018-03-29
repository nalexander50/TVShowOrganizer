import os
import argparse

from models.tv_show import TVShow
from models.season import Season
from models.episode import Episode

PREFERRED_VIDEO_EXTENSION = '.mkv'

VIDEO_EXTENSIONS = [
    '.avi', '.mkv', '.mov', '.mp4', '.wmv'
]

def main():

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('path', help='Path to the folder containing all TV Show files')
    arg_parser.add_argument('--whatIf', help='Display changes that would be made. Does not modify any files.', action='store_false')

    args = arg_parser.parse_args()

    tv_show_path = args.path
    should_modify = args.whatIf

    tv_show = TVShow(tv_show_path)
    print(tv_show)

    process_seasons(tv_show, should_modify)

    if should_modify:
        print('[DONE]')
    else:
        print('Done')

def process_seasons(tv_show, should_modify):
    count = 0
    for entry in sorted(os.listdir(tv_show.folder_path)):
        entry_path = os.path.join(tv_show.folder_path, entry)
        if os.path.isdir(entry_path):
            count += 1

            season = Season(entry_path, tv_show, count)
            print(f'\t{season} | {season.rename(should_modify)}')

            process_episodes(season, should_modify)
        else:
            if should_modify:
                os.remove(entry_path)
                print(f'\t[DELETED] {entry_path}')
            else:
                print(f'\tDelete {entry_path}')

def process_episodes(season, should_modify):
    count = 0
    for entry in sorted(os.listdir(season.folder_path)):
        _, extension = os.path.splitext(entry)
        entry_path = os.path.join(season.folder_path, entry)

        if extension in VIDEO_EXTENSIONS:
            count += 1

            episode = Episode(entry_path, season, count, extension)
            print(f'\t\t{episode} | {episode.rename(should_modify)}')

            if extension != PREFERRED_VIDEO_EXTENSION:
                print(f'\t\t\t{episode.encode(PREFERRED_VIDEO_EXTENSION, should_modify)}')

        else:
            if should_modify:
                os.remove(entry_path)
                print(f'\t\t[DELETED] {entry_path}')
            else:
                print(f'\t\tDelete {entry_path}')

if __name__ == '__main__':
    main()