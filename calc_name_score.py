import os


def read_data_from(filename):

    with open(os.path.join(os.getcwd(), 'input_file', filename)) as f:
        contexts = f.read()

    return [name.replace('"', '') for name in sorted(contexts.split(','))]


def calc_name_score(filename):

    contexts = read_data_from(filename)

    if len(contexts) != len(set(contexts)):
        raise Exception('name is duplicated')

    unicode_basic = ord('A') - 1
    total_name_score = 0

    for idx, name in enumerate(contexts):
        for char in name:
            if ord('A') <= ord(char) <= ord('Z'):
                total_name_score += (ord(char) - unicode_basic) * (idx + 1)
            else:
                raise Exception('context format of file is wrong')

    return total_name_score


if __name__ == '__main__':
    calc_name_score('contexts.txt')
    # calc_name_score('duplicated_string.txt')
    # calc_name_score('wrong_format_with_new_line.txt')
