# sspypl
Simple Stupid Programming Language written on PYthon

# Information
This file has Russian analog: [link](https://github.com/TwoSpikes/sspypl/blob/master/README-rus.md)

# Dependencies
python version: I do not know but my is 3.11.4
shell: bash, fish, csh, sh, zsh or other

# Quick install
## Step 1:
```console
SSPYPL_PATH=~/sspypl
```
You can change this path to any you want

You can add extra slash (/) if you want (or even several slashes)

## Step 2:
```console
set +o histexpand
```
It is nessesary to properly escape shebang symbol

## Step 3A:
```console
echo "#!/bin/env -S python3 $SSPYPL_PATH/main.py" > "${PREFIX}"/bin/sspypl
```

## Step 3B:
If you want to change path dynamicaly, run
```console
echo '#!/bin/env -S python3 $SSPYPL_PATH/main.py' > "${PREFIX}"/bin/sspypl
```
In that case, to set path, do [first step](Step 1) with custom path

## Step 4:
```
chmod -v u+x "${PREFIX}"/bin/sspypl
```

# Interpreter

not implemented yet

# Language

not implemented yet

# [faq](https://github.com/TwoSpikes/sspypl/blob/master/FAQ.md)
