def name_score():

    filename = 'name_score.txt'
    with open(filename) as f:
        contexts = f.read()
    contexts = sorted(contexts.split(','))
    contexts = [name.replace('"', '') for name in contexts]

    unicode_basic = ord('A') - 1
    total_name_score = 0

    for idx, name in enumerate(contexts):
        name_score_sum = sum([ord(character) - unicode_basic for character in name]) * (idx + 1)
        total_name_score += name_score_sum

    print(total_name_score)


if __name__ == '__main__':
    name_score()
