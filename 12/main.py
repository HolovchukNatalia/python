#!/usr/bin/env python3
"""
Лабораторна робота:
Візуалізація тривимірних даних з .csv файлів із використанням бібліотеки Plotly.
Створення інтерактивних графіків і тривимірних діаграм.

Автор: (впишіть своє ПІБ)
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# -----------------------------
# Налаштування та структури даних
# -----------------------------

DEFAULT_OUTPUT_DIR = "outputs"


@dataclass
class ColumnChoice:
    x: str
    y: str
    z: str
    color: Optional[str] = None
    size: Optional[str] = None


# -----------------------------
# Допоміжні функції (ввід/перевірки)
# -----------------------------

def print_header() -> None:
    print("=" * 72)
    print("3D-візуалізація CSV (Plotly) — інтерактивний аналіз даних")
    print("=" * 72)


def ask_path(prompt: str) -> str:
    return input(prompt).strip().strip('"').strip("'")


def ensure_output_dir(path: str = DEFAULT_OUTPUT_DIR) -> Path:
    out = Path(path)
    out.mkdir(parents=True, exist_ok=True)
    return out


def safe_int(prompt: str, allowed: Optional[List[int]] = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            if allowed is not None and value not in allowed:
                print(f"✗ Допустимі значення: {allowed}")
                continue
            return value
        except ValueError:
            print("✗ Введіть ціле число.")


def choose_from_list(prompt: str, options: List[str], allow_empty: bool = False) -> Optional[str]:
    """
    Дозволяє обрати елемент зі списку. Якщо allow_empty=True, порожній ввід -> None.
    """
    while True:
        raw = input(prompt).strip()
        if allow_empty and raw == "":
            return None
        if raw in options:
            return raw
        print("✗ Невірна назва. Доступні варіанти:")
        print(", ".join(options))


# -----------------------------
# Завантаження та підготовка даних (етапи обробки)
# -----------------------------

def load_csv(file_path: str) -> pd.DataFrame:
    """
    Етап 1: імпорт даних.
    Підтримує CSV з розділювачем кома/крапка з комою (автовизначення).
    """
    p = Path(file_path)
    if not p.exists():
        raise FileNotFoundError(f"Файл не знайдено: {p.resolve()}")

    try:
        # engine='python' дозволяє sep=None (автовизначення)
        df = pd.read_csv(p, sep=None, engine="python", encoding="utf-8")
    except UnicodeDecodeError:
        # запасний варіант кодування
        df = pd.read_csv(p, sep=None, engine="python", encoding="cp1251")
    return df


def normalize_numeric_strings(series: pd.Series) -> pd.Series:
    """
    Етап 2: очищення.
    Перетворює рядки виду " 1,23 " -> 1.23, прибирає зайві пробіли.
    Якщо значення не можна перетворити — стане NaN.
    """
    if series.dtype == "object":
        cleaned = (
            series.astype(str)
            .str.strip()
            .str.replace(" ", "", regex=False)
            .str.replace(",", ".", regex=False)
        )
        return pd.to_numeric(cleaned, errors="coerce")
    return pd.to_numeric(series, errors="coerce")


def clean_dataframe(df: pd.DataFrame, numeric_cols: List[str]) -> Tuple[pd.DataFrame, dict]:
    """
    Етап 2: очищення даних.
    - конвертація числових колонок до float
    - видалення рядків з NaN у вибраних числових колонках
    Повертає очищений df та статистику очищення.
    """
    stats = {"rows_before": len(df), "nan_before": {}, "nan_after": {}}

    work = df.copy()

    for col in numeric_cols:
        stats["nan_before"][col] = int(work[col].isna().sum()) if col in work.columns else None
        work[col] = normalize_numeric_strings(work[col])

    # Перевірка NaN після конвертації
    for col in numeric_cols:
        stats["nan_after"][col] = int(work[col].isna().sum())

    # Видаляємо рядки з NaN у ключових числових колонах
    work = work.dropna(subset=numeric_cols).reset_index(drop=True)

    stats["rows_after"] = len(work)
    stats["rows_dropped"] = stats["rows_before"] - stats["rows_after"]
    return work, stats


def compute_basic_stats(df: pd.DataFrame, cols: List[str]) -> pd.DataFrame:
    """
    Етап 3: аналіз/розрахунки — описова статистика.
    """
    return df[cols].describe().T


# -----------------------------
# Візуалізація (Plotly)
# -----------------------------

def make_3d_scatter(df: pd.DataFrame, choice: ColumnChoice, title: str) -> go.Figure:
    """
    3D scatter з можливістю задавати color/size.
    """
    fig = px.scatter_3d(
        df,
        x=choice.x,
        y=choice.y,
        z=choice.z,
        color=choice.color if choice.color else None,
        size=choice.size if choice.size else None,
        title=title,
        opacity=0.85,
    )
    fig.update_layout(margin=dict(l=0, r=0, t=50, b=0))
    return fig


def make_3d_line(df: pd.DataFrame, choice: ColumnChoice, title: str) -> go.Figure:
    """
    3D лінія: дані попередньо сортуємо по X.
    """
    d = df.sort_values(by=choice.x).reset_index(drop=True)
    trace = go.Scatter3d(
        x=d[choice.x],
        y=d[choice.y],
        z=d[choice.z],
        mode="lines+markers",
    )
    fig = go.Figure(data=[trace])
    fig.update_layout(title=title, margin=dict(l=0, r=0, t=50, b=0))
    return fig


def make_3d_surface_if_grid(df: pd.DataFrame, choice: ColumnChoice, title: str) -> go.Figure:
    """
    3D surface: потребує сітки (X, Y) -> Z.
    Якщо дані не є сіткою, робимо pivot з агрегацією mean.
    """
    # округлюємо X,Y щоб збільшити шанс утворення сітки
    d = df.copy()
    d["_x_round"] = d[choice.x].round(2)
    d["_y_round"] = d[choice.y].round(2)

    pivot = d.pivot_table(index="_y_round", columns="_x_round", values=choice.z, aggfunc="mean")
    # plotly surface expects z as 2D array
    z = pivot.values
    x = pivot.columns.values
    y = pivot.index.values

    fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)])
    fig.update_layout(title=title, margin=dict(l=0, r=0, t=50, b=0))
    return fig


def save_outputs(
    out_dir: Path,
    df_clean: pd.DataFrame,
    stats_table: pd.DataFrame,
    fig: go.Figure,
    base_name: str = "result",
) -> Tuple[Path, Path, Path]:
    """
    Етап 4: збереження результатів.
    - cleaned CSV
    - статистика TXT
    - інтерактивний графік HTML
    """
    out_dir.mkdir(parents=True, exist_ok=True)

    csv_path = out_dir / f"{base_name}_cleaned.csv"
    txt_path = out_dir / f"{base_name}_stats.txt"
    html_path = out_dir / f"{base_name}_plot.html"

    df_clean.to_csv(csv_path, index=False, encoding="utf-8")

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("Описова статистика (describe):\n\n")
        f.write(stats_table.to_string())
        f.write("\n")

    fig.write_html(str(html_path), include_plotlyjs="cdn")

    return csv_path, txt_path, html_path


# -----------------------------
# Головний сценарій (діалог з користувачем)
# -----------------------------

def run() -> None:
    print_header()
    print("Порада: для тесту використайте файл sample_3d_data.csv (є в папці проєкту).")
    file_path = ask_path("Введіть шлях до CSV файлу: ")

    try:
        df = load_csv(file_path)
    except FileNotFoundError as e:
        print(f"✗ Помилка: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Не вдалося прочитати CSV: {e}")
        sys.exit(1)

    print("\n✓ Файл успішно завантажено.")
    print(f"Рядків: {len(df)}, Колонок: {len(df.columns)}")
    print("Колонки:", ", ".join(df.columns.astype(str).tolist()))

    # Обираємо X,Y,Z
    cols = df.columns.astype(str).tolist()
    print("\nОберіть колонки для 3D-візуалізації (X, Y, Z повинні бути числовими).")
    x = choose_from_list("X колонка: ", cols)
    y = choose_from_list("Y колонка: ", cols)
    z = choose_from_list("Z колонка: ", cols)

    # Опційні колонки
    print("\nОпційно: оберіть колонку для кольору (категорія або число) — Enter щоб пропустити.")
    color = choose_from_list("Color колонка (або Enter): ", cols, allow_empty=True)

    print("Опційно: оберіть колонку для розміру маркера (число) — Enter щоб пропустити.")
    size = choose_from_list("Size колонка (або Enter): ", cols, allow_empty=True)

    choice = ColumnChoice(x=x, y=y, z=z, color=color, size=size)

    # Етап очищення
    try:
        df_clean, clean_stats = clean_dataframe(df, numeric_cols=[choice.x, choice.y, choice.z])
    except KeyError as e:
        print(f"✗ Немає колонки в даних: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Помилка під час очищення: {e}")
        sys.exit(1)

    print("\n✓ Очищення завершено.")
    print(f"Рядків до: {clean_stats['rows_before']}, після: {clean_stats['rows_after']}")
    print(f"Видалено рядків (через NaN/помилки): {clean_stats['rows_dropped']}")

    # Аналіз
    stats_table = compute_basic_stats(df_clean, cols=[choice.x, choice.y, choice.z])
    print("\nОписова статистика (коротко):")
    print(stats_table[["count", "mean", "min", "max"]])

    # Вибір типу графіка
    print("\nОберіть тип 3D-графіка:")
    print("1 — 3D Scatter (точки)")
    print("2 — 3D Line (лінія)")
    print("3 — 3D Surface (поверхня через pivot)")
    plot_type = safe_int("Ваш вибір (1/2/3): ", allowed=[1, 2, 3])

    title = f"3D графік: {choice.x}, {choice.y}, {choice.z}"

    try:
        if plot_type == 1:
            fig = make_3d_scatter(df_clean, choice, title=title)
        elif plot_type == 2:
            fig = make_3d_line(df_clean, choice, title=title)
        else:
            fig = make_3d_surface_if_grid(df_clean, choice, title=title)
    except Exception as e:
        print(f"✗ Помилка побудови графіка: {e}")
        sys.exit(1)

    # Збереження
    out_dir = ensure_output_dir(DEFAULT_OUTPUT_DIR)
    try:
        csv_path, txt_path, html_path = save_outputs(out_dir, df_clean, stats_table, fig, base_name="task2")
    except Exception as e:
        print(f"✗ Помилка збереження результатів: {e}")
        sys.exit(1)

    print("\n✓ Готово! Результати збережено:")
    print(f"- Очищені дані: {csv_path.resolve()}")
    print(f"- Статистика:   {txt_path.resolve()}")
    print(f"- Графік HTML:  {html_path.resolve()}")
    print("\nВідкрийте HTML у браузері — графік інтерактивний (обертання, масштабування, наведення).")


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\nПерервано користувачем.")
        sys.exit(0)
