# Tracery for Python

[![Build Status](https://travis-ci.org/aparrish/pytracery.svg?branch=master)](https://travis-ci.org/aparrish/pytracery)

This is a (rough) port of [Kate Compton](http://www.galaxykate.com/)'s
wonderful [Tracery](http://tracery.io/) to Python. The port
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
instead of JavaScript objects for the rules, but the concept is the same
otherwise.

```python
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
```

Any valid Tracery grammar should work in this port. The `base_english`
modifiers in `tracery.modifiers` are a port of the modifiers in the JavaScript
package. Many aspects of Tracery are not standardized, so in some edge cases
you may get output that doesn't exactly conform to what you would get if you
used the same grammar with the JavaScript version. (e.g., "None" in strings
where in JavaScript you might see "undefined")

## Command line

You can run the module on a JSON Tracery grammar file on the command line to output example lines:
```
positional arguments:
  json        Input JSON file
  number      Number of lines to generate (default: 1)
```

For example:
```
$ python -m tracery potterpapers.json 
Harry Potter and the Tchebyshev transforms of the first and second kind
```
```
$ python -m tracery potterpapers.json 3
Harry Potter and the Impact of Extremes in Outdoor Temperature and Sunshine Exposure on Birth Weight.
Harry Potter and the Chromatin Remodelling Enzymes SNF2H and SNF2L Position Nucleosomes adjacent to CTCF and Other Transcription Factors.
Harry Potter and the Model Organism Hermissenda crassicornis (Gastropoda: Heterobranchia) Is a Species Complex.
```

## Contributing

This port is very fresh but I wanted to put it on GitHub so it would be easier
to deploy my own bots that use the code. A lot remains to be done: see
`todo.txt` for a (probably incomplete) to-do list. Feel free to submit pull
requests or to open issues in the GitHub issue tracker.

List of contributors:

* Hugo van Kemenade (build process, code clean-up)

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

