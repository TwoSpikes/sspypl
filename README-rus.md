# sspypl
Simple Stupid Programming Language written on PYthon

# Зависимости
версия python: хз но у меня 3.11.4\
командная строка: bash, fish, csh, sh, zsh илм другая

# Быстрая установка
## Шаг 1:
```console
SSPYPL_PATH=~/sspypl
```
Можете изменить путь на любой который захотите

You can add extra slash (/) if you want (or even several slashes)

## Шаг 2:
```console
set +o histexpand
```
Это необходимо для правильного экранирования шебанга

## Шаг 3A:
```console
echo "#!/bin/env -S python3 $SSPYPL_PATH/main.py" > "${PREFIX}"/bin/sspypl
```

## Шаг 3B:
Если хотите динамически изменять путь к файлу `main.py` после установки:
```console
echo '#!/bin/env -S python3 $SSPYPL_PATH/main.py' > "${PREFIX}"/bin/sspypl
```
Тогда после шага 3B Вам, чтобы изменить путь, потребуется перевыполнить [Шаг 1](Шаг 1) с модифицированным путём к файлу `main.py`

## Шаг 4:
```
chmod -v u+x "${PREFIX}"/bin/sspypl
```

# Туториал по интерпретатору (его аргументами командной строки)

not implemented yet

# Туториал по языку

not implemented yet

# [faq](https://github.com/TwoSpikes/sspypl/blob/master/FAQ.md)
