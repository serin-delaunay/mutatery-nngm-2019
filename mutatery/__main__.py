#!/usr/bin/env python
# encoding: utf-8
"""
Output an example line from a JSON Tracery grammar.
"""
from __future__ import print_function, unicode_literals
import argparse
import json
import random
import tqdm
import itertools as it

import mutatery
from mutatery.modifiers import base_english
import tracery


class Phrase:
    def __init__(self, grammar):
        self.grammar = grammar
        self.make_initial_tree()

    def make_initial_tree(self):
        self.grammar.flatten('#origin#')

    @staticmethod
    def begins_with(prefix, path):
        return path[:len(prefix)] == prefix

    def mutate(self):
        choices = list(self.grammar.choices.keys())
        del_path = random.choice(choices)
        self.grammar.mutated_path = del_path
        self.grammar.mutated_choice = self.grammar.choices[del_path]
        for path in choices:
            if self.begins_with(del_path, path):
                del self.grammar.choices[path]

    def flatten(self):
        return self.grammar.flatten('#origin#')

def capitalise_nicely(s):
    try:
        head, rest = s.split(' ', maxsplit = 1)
        return f"{head.capitalize()} {rest}"
    except ValueError:
        return s.capitalize()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Output an example line from a JSON Tracery grammar.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "grammar", help="Input Tracery grammar file")
    parser.add_argument(
        "out", help="Output story text file")
    parser.add_argument(
        "out_punctuated", help="Output punctuated story text file")
    parser.add_argument(
        "words", type=int, default=50000, nargs="?",
        help="Minimum number of words to generate")
    args = parser.parse_args()

    with open(args.grammar) as data_file:
        rules = json.load(data_file)

    grammar = mutatery.Grammar(rules)
    grammar.add_modifiers(base_english)

    phrases = []
    actual_words = 0
    p = Phrase(grammar)
    pbar = tqdm.tqdm(total=args.words)
    while actual_words < args.words:
        current_phrase = p.flatten()
        actual_words += len(current_phrase.split())
        phrases.append(current_phrase)
        pbar.update(len(current_phrase.split()))
        p.mutate()
    
    lines = '\n'.join([p.capitalize() for p in phrases])
    story_words = ' '.join(phrases).split(' ')
    with open('punctuation_2.json') as data_file:
        rules = json.load(data_file)
    punctuator = tracery.Grammar(rules)
    punctuation = []
    words = 0
    while words != actual_words:
        if words > actual_words:
            index = random.randint(0, len(punctuation) - 1)
            delta = punctuation[index].count('a')
            words -= delta
            del punctuation[index]
        else:
            next_punctuation = punctuator.flatten("#origin#")
            words += next_punctuation.count('a')
            punctuation.append(next_punctuation)
    punctuation = ''.join(punctuation).split('a')
    story_punctuated = ''.join(it.chain.from_iterable(zip(story_words + [''], punctuation[1:])))
    for sep in ['. ', '! ', '? ', '.\n', '!\n', '?\n', '.\n\n', '!\n\n', '?\n\n']:
        sp = story_punctuated.split(sep)
        story_punctuated = sep.join(capitalise_nicely(s) for s in sp)
    
    with open(args.out, 'w') as file:
        file.write(lines)
    with open(args.out_punctuated, 'w') as file:
        file.write(story_punctuated)
# End of file
