# Online store

Простой учебный проект интернет‑магазина на Python. Логика магазина находится в папке `src`, есть тесты в папке `tests`.

## Как запустить проект

1. Установите Python 3.10+.
2. Установите зависимости (используется Poetry):

```bash
poetry install
```

3. Запустите проект:

```bash
poetry run python main.py
```

## Как запустить тесты

```bash
poetry run pytest
```

## Отчёт по покрытию тестами

```bash
poetry run coverage run -m pytest
poetry run coverage html
```
