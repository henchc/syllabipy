# syllabipy
Collection of syllabification algorithms designed to be universal, aimed at low-resource languages without look-up techniques.

*Note: SonoriPy has been incorporated into [NLTK](https://github.com/nltk/nltk/blob/develop/nltk/tokenize/sonority_sequencing.py) for Python; LegaliPy and SonoriPy have been incorporated into [Talisman](https://github.com/Yomguithereal/talisman) for JavaScript. This repo will not be updated, we recommend you use one of these two libraries.*

## installation

syllabipy can be installed with `pip`:

~~~
$ pip install syllabipy
~~~

### LegaliPy

To get legal onsets for variable `text`:

~~~
>>> from syllabipy.legalipy import getOnsets
>>> getOnsets(text)
~~~

To syllabify a word:

~~~
>>> from syllabipy.legalipy import LegaliPy
>>> LegaliPy(word, getOnsets(text))
~~~

Command line usage to syllabify a text file:

~~~
$ python legalipy.py text.txt
~~~

### SonoriPy

To syllabify a word:

~~~
>>> from syllabipy.sonoripy import SonoriPy
>>> SonoriPy("justification")
['jus', 'ti', 'fi', 'ca', 'tion']
~~~

Command line usage to syllabify a text file:

~~~
$ python sonoripy.py text.txt
~~~

## Development

To get started, create a python virtual environment e.g. with:

~~~
python3 -m venv .venv
source .venv/bin/activate
~~~

Then install development dependencies with:

~~~
pip install -r requirements-dev.txt
~~~

Run the tests with:

~~~
pytest tests.py
~~~
