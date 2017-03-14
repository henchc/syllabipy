# syllabipy
Collection of syllabification algorithms designed to be universal, aimed at low-resource languages without look-up techniques. No dependencies.

LegaliPy and SonoriPy have been incorporated into the [Talisman](https://github.com/Yomguithereal/talisman) NLP library for JavaScript.

## installation

syllabipy can be installed with `pip`:

~~~
$ pip install syllabipy
~~~

### LegaliPy

To get legal onsets for variable `text`:

~~~
>>> from legalipy import getOnsets
>>> getOnsets(text)
~~~

To syllabify a word:

~~~
>>> from legalipy import LegaliPy
>>> LegaliPy(word, getOnsets(text))
~~~

Command line usage to syllabify a text file:

~~~
$ python legalipy.py text.txt
~~~

### SonoriPy

To syllabify a word:

~~~
>>> from sonoripy import SonoriPy
>>> SonoriPy("justification")
['jus', 'ti', 'fi', 'ca', 'tion']
~~~

Command line usage to syllabify a text file:

~~~
$ python sonoripy.py text.txt
~~~