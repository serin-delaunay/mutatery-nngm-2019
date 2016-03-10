# Tracery for Python

This is a (rough) port of [Kate Compton](http://www.galaxykate.com/)'s
wonderful [Tracery](https://github.com/galaxykate/tracery) to Python. The port
is by [Allison Parrish](http://www.decontextualize.com/).

I'm always writing little one-off recursive template/grammar expansion functions
in my Python generative text projects. And I *love* working with Tracery! So I figured:
why not save myself (and potentially others) some time and just make it
possible to use Tracery from within Python? This port is the result!

The port is a fairly literal Python translation of [this
version](https://github.com/galaxykate/tracery/blob/8baa6ec53271ce7526e14b0ae3069a7469c6f035/js/tracery/tracery.js)
of `tracery.js` in the official repository's `tracery2` branch.

## Installation

    pip install -e git+https://github.com/aparrish/pytracery.git#egg=tracery

(I'm working on getting this package on PyPI.)

## Usage

See [Kate Compton's Tracery
tutorial](http://www.crystalcodepalace.com/traceryTut.html) for information
about how Tracery works. In the Python port, you use Python dictionaries
instead of Javascript objects for the rules, but the concept is the same
otherwise.

    import tracery
    from tracery.modifiers import base_english

    rules = {
        'origin': '#hello.capitalize#, #location#!',
        'hello': ['hello', 'greetings', 'howdy', 'hey'],
        'location': ['world', 'solar system', 'galaxy', 'universe']
    }

    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)
    print grammar.flatten("#origin#") # prints, e.g., "Hello, world!"

Any valid Tracery grammar should work in this port. The `base_english`
modifiers in `tracery.modifiers` are a port of the modifiers in the Javascript
package. Many aspects of Tracery are not standardized, so in some edge cases
you may get output that doesn't exactly conform to what you would get if you
used the same grammar with the Javascript version. (e.g., "None" in strings
where in Javascript you might see "undefined")

## Contributing

This port is very fresh but I wanted to put it on Github so it would be easier
to deploy my own bots that use the code. A lot remains to be done: see
`todo.txt` for a (probably incomplete) to-do list. Feel free to submit pull
requests or to open issues in the Github issue tracker.

## License

This port inherits Tracery's original Apache License 2.0.

    Copyright 2016 Allison Parrish
    Based on code by Kate Compton

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

