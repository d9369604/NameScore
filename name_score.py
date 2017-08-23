def name_score():
    filename = 'name_score.txt'
    with open(filename) as f:
        contexts = f.read()
    contexts = sorted(contexts.split(','))
    contexts = [i.replace('"', '') for i in contexts]

    basic = ord('A')

    for idx, context in enumerate(contexts):
        total_sum = 0
        for i in context:
            total_sum += ord(i) - basic + 1
        total_sum *= idx + 1
        print "{} : {}".format(context, total_sum)


if __name__ == '__main__':
    name_score()
