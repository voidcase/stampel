# Stampy

A very simple utility to run many variations of a command.

## Usage

Instead of

```
git add foo.py; git commit -m "fooified the fooing"
git add bar.py; git commit -m "barified the baring"
```

You can do

```
stam.py 'git add {}.py; git commit -m "{}"'
> foo, fooified the fooing
> bar, barified the baring
```

That's it. It's like 18 lines so just read the code if you want to know more.
