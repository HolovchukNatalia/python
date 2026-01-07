# 3D CSV Visualizer (Plotly) — лабораторна

## Встановлення
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -U pip
pip install pandas plotly
```

## Запуск
```bash
python main.py
```

Для швидкої перевірки використайте `sample_3d_data.csv` (лежить поруч із `main.py`).

## Результати
Після запуску програма створює папку `outputs/`:
- `task2_cleaned.csv` — очищені дані
- `task2_stats.txt` — описова статистика
- `task2_plot.html` — інтерактивний 3D-графік (відкрити в браузері)

## GitHub
1) Створіть публічний репозиторій.
2) Додайте сюди весь вміст папки.
3) Додайте посилання у звіт у розділ «Посилання на код».
