''' Sorts the characters in a block of text alphabetically '''
import argparse

def alphabetize(text):
    ''' performs alphabetization '''
    caps = [l.lower() != l for l in text]
    fixed = [(i, l) for (i, l) in enumerate(text) if not l.isalpha()]
    letters = sorted([l for l in text.lower() if l.isalpha()])

    [letters.insert(i, l) for (i, l) in fixed]

    return ''.join(l.upper() if cap else l for (l, cap) in zip(letters, caps))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='alphabetize letters in text')
    parser.add_argument('text', type=str)

    args = parser.parse_args()

    print alphabetize(args.text)
