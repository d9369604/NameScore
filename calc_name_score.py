import os


def read_data_from(filename):

    with open(os.path.join(os.getcwd(), 'input_file', filename)) as f:
        content = f.read()

    return [name.replace('"', '') for name in content.split(',')]


def calc_name_score(content):

    unicode_basic = ord('A') - 1
    total_name_score = 0

    for idx, name in enumerate(sorted(content)):
        name_score_sum = sum([ord(character) - unicode_basic for character in name]) * (idx + 1)
        total_name_score += name_score_sum

    return total_name_score


if __name__ == '__main__':
    contexts = read_data_from('contexts.txt')
    print calc_name_score(contexts)
