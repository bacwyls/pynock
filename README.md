pynock
======

An implementation of Nock in Python.

======
======

Forked from jtauber.

added ```parse_noun(s)``` which forms a tree from a string that represents a noun in typical nock syntax (i.e. "[44 [55 66] 77]")

the output of ```parse_noun(s)``` can be run in ```nock(noun)```

in your terminal, you can run
```python nock.py <cell>``` to run nock on that cell using the head as the subject and the tail as the formula


example:
```python nock.py "[70 [8 [1 0] 8 [1 6 [5 [0 7] 4 0 6] [0 6] 9 2 [0 2] [4 0 6] 0 7] 9 2 0 1]]"```

```69```


