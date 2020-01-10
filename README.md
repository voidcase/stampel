# Stampel

A very simple utility to run many variations of a command.

## Usage

Instead of something like

```
git add src/database.py; git commit -m "fixed duplication bug [162]"
git add src/ui.py res/loading.gif; git commit -m "added pretty loading animation"
```

You can do

```
stampel 'git add {}.py; git commit -m "{}"'
> src/database.py, fixed duplication bug [162]
> src/ui.py res/graphic.gif, added pretty loading animation
```

That's it. It's very small so just read the code if you want to know more.
