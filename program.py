import os

import collections

SearchResult = collections.namedtuple('SearchResult',
                                      'file, line, text')

def main():
    print_header()

    search_text = get_search_text_from_user()
    if not search_text:
        print("We can't search for nothing !")
        return

    # print('Search Text: {}'.format(search_text))

    search_folder = get_search_folder_from_user()
    if not search_folder:
        print("We need a folder to search through !")
        return

    # print('Search Folder: {}'.format(search_folder))

    matches = search_folders(search_folder, search_text)
    matches_count = 0

    for m in matches:
        matches_count = matches_count + 1
        # print(m)
        # print('------------  MATCH  -------------')
        # print('file: ' + m.file)
        # print('line: {}'.format(m.line))
        # print('match: ' + m.text.strip())
        # print()

    print('Found {:,} matches'.format(matches_count))


def print_header():
    print('--------------------------------')
    print('        File Search App')
    print('--------------------------------')
    print('')


def get_search_folder_from_user():
    folder = input('What folder do you want to search through ? ')
    if not folder or not folder.strip():
        print('No input: ')
        return None

    if not os.path.isdir(folder):
        print('Not directory: ')
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input('What text do you want to search for [single phrases only] ? ')
    return text.lower()


def search_folders(folder, text):
    print('Would search {} folder for {} '.format(folder, text))

    # all_matches = []
    items = os.listdir(folder)

    for item in items:

        print("item: {}".format(item))

        #if item == "pip-10.0.1-py3.7.egg":
        #    return all_matches
        #elif item == "Scripts":
        #    return all_matches
        #else:

        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            yield from search_folders(full_item, text)
            # all_matches.extend(matches)
        else:
            yield from search_item(full_item, text)
            # all_matches.extend(matches)

    # return all_matches


def search_item(filename, search_text):

    # matches = []

    with open(filename, 'r', encoding='utf8') as fin:

        line_num = 0
        for line in fin:
            line_num = line_num + 1
            if line.find(search_text) >= 0:
                m = SearchResult(line=line_num, file=filename, text=line)
                # print("m : {}".format(m))
                # matches.append(m)
                yield m

    # return matches


if __name__ == '__main__':
    main()
