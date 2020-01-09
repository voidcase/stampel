# Stampel

A very simple utility to run many variations of a command.

## Usage

Instead of something like

```
git add foo.py; git commit -m "fooified the fooing"
git add bar.py; git commit -m "barified the baring"
```

You can do

```
stampel 'git add {}.py; git commit -m "{}"'
> foo, fooified the fooing
> bar, barified the baring
```

That's it. It's very small so just read the code if you want to know more.
