"""
ПРОГРАМА ВІЗУАЛІЗАЦІЇ ТРИВИМІРНИХ ДАНИХ З CSV ФАЙЛІВ
Використання бібліотеки Plotly для створення інтерактивних графіків

Автор: Студент
Дата: 07.01.2026
Варіант: Візуалізація тривимірних даних з .csv файлів
"""

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
import os
import sys


class DataVisualizer3D:
    """
    Клас для завантаження, обробки та візуалізації тривимірних даних
    """
    
    def __init__(self):
        """Ініціалізація візуалізатора"""
        self.data = None
        self.filename = None
        
    def load_csv_data(self, filename):
        """
        Завантаження даних з CSV файлу
        
        Параметри:
            filename (str): Шлях до CSV файлу
            
        Повертає:
            bool: True якщо завантаження успішне, False інакше
        """
        try:
            if not os.path.exists(filename):
                raise FileNotFoundError(f"Файл '{filename}' не знайдено")
            
            # Спроба завантажити з різними роздільниками
            try:
                self.data = pd.read_csv(filename, encoding='utf-8')
            except:
                try:
                    self.data = pd.read_csv(filename, encoding='cp1251', sep=';')
                except:
                    self.data = pd.read_csv(filename, encoding='latin1')
            
            self.filename = filename
            print(f"  Дані успішно завантажено з файлу: {filename}")
            print(f"  Розмір даних: {self.data.shape[0]} рядків × {self.data.shape[1]} стовпців")
            return True
            
        except FileNotFoundError as e:
            print(f"  Помилка: {e}")
            return False
        except Exception as e:
            print(f"  Помилка при завантаженні файлу: {e}")
            return False
    
    def validate_data(self):
        """
        Перевірка та валідація даних
        
        Повертає:
            bool: True якщо дані валідні, False інакше
        """
        try:
            if self.data is None:
                raise ValueError("Дані не завантажено")
            
            if self.data.shape[1] < 3:
                raise ValueError("Файл повинен містити мінімум 3 стовпці для 3D візуалізації")
            
            # Перевірка на наявність числових стовпців
            numeric_cols = self.data.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) < 3:
                raise ValueError("Недостатньо числових стовпців для 3D візуалізації")
            
            # Обробка пропущених значень
            missing_count = self.data.isnull().sum().sum()
            if missing_count > 0:
                print(f"⚠ Знайдено {missing_count} пропущених значень")
                choice = input("Видалити рядки з пропущеними значеннями? (y/n): ").lower()
                if choice == 'y':
                    self.data = self.data.dropna()
                    print(f"  Видалено рядки з пропущеними значеннями")
            
            print("  Дані пройшли валідацію")
            return True
            
        except Exception as e:
            print(f"  Помилка валідації: {e}")
            return False
    
    def show_data_info(self):
        """Відображення інформації про дані"""
        if self.data is None:
            print("  Дані не завантажено")
            return
        
        print("\n" + "="*70)
        print("ІНФОРМАЦІЯ ПРО ЗАВАНТАЖЕНІ ДАНІ")
        print("="*70)
        print(f"\nНазва файлу: {self.filename}")
        print(f"Розмір: {self.data.shape[0]} рядків × {self.data.shape[1]} стовпців")
        print(f"\nСтовпці:")
        for i, col in enumerate(self.data.columns, 1):
            dtype = self.data[col].dtype
            print(f"  {i}. {col} ({dtype})")
        
        print(f"\nПерші 5 рядків:")
        print(self.data.head())
        
        print(f"\nСтатистичні показники:")
        print(self.data.describe())
        print("="*70 + "\n")
    
    def select_columns(self):
        """
        Вибір стовпців для осей X, Y, Z
        
        Повертає:
            tuple: (x_col, y_col, z_col) або None при помилці
        """
        try:
            numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
            
            print("\n" + "="*70)
            print("ВИБІР КООРДИНАТ ДЛЯ ВІЗУАЛІЗАЦІЇ")
            print("="*70)
            print("\nДоступні числові стовпці:")
            for i, col in enumerate(numeric_cols, 1):
                print(f"  {i}. {col}")
            
            print("\nВведіть номери стовпців для осей:")
            x_idx = int(input(f"Вісь X (1-{len(numeric_cols)}): ")) - 1
            y_idx = int(input(f"Вісь Y (1-{len(numeric_cols)}): ")) - 1
            z_idx = int(input(f"Вісь Z (1-{len(numeric_cols)}): ")) - 1
            
            if not all(0 <= idx < len(numeric_cols) for idx in [x_idx, y_idx, z_idx]):
                raise ValueError("Некоректні номери стовпців")
            
            x_col = numeric_cols[x_idx]
            y_col = numeric_cols[y_idx]
            z_col = numeric_cols[z_idx]
            
            print(f"\n  Обрано: X={x_col}, Y={y_col}, Z={z_col}")
            return x_col, y_col, z_col
            
        except (ValueError, IndexError) as e:
            print(f"  Помилка вибору стовпців: {e}")
            return None
    
    def create_3d_scatter(self, x_col, y_col, z_col, color_col=None):
        """
        Створення 3D діаграми розсіювання
        
        Параметри:
            x_col, y_col, z_col (str): Назви стовпців для осей
            color_col (str): Стовпець для кольорування точок
        """
        try:
            print("\n  Створення 3D діаграми розсіювання...")
            
            fig = go.Figure(data=[go.Scatter3d(
                x=self.data[x_col],
                y=self.data[y_col],
                z=self.data[z_col],
                mode='markers',
                marker=dict(
                    size=6,
                    color=self.data[color_col] if color_col else self.data[z_col],
                    colorscale='Viridis',
                    showscale=True,
                    colorbar=dict(title=color_col if color_col else z_col)
                ),
                text=[f"{x_col}: {x}<br>{y_col}: {y}<br>{z_col}: {z}" 
                      for x, y, z in zip(self.data[x_col], 
                                        self.data[y_col], 
                                        self.data[z_col])],
                hovertemplate='%{text}<extra></extra>'
            )])
            
            fig.update_layout(
                title=f'3D Діаграма розсіювання: {x_col}, {y_col}, {z_col}',
                scene=dict(
                    xaxis_title=x_col,
                    yaxis_title=y_col,
                    zaxis_title=z_col
                ),
                width=1000,
                height=800
            )
            
            output_file = 'scatter_3d.html'
            fig.write_html(output_file)
            print(f"  3D діаграма розсіювання збережена: {output_file}")
            fig.show()
            
        except Exception as e:
            print(f"  Помилка створення діаграми: {e}")
    
    def create_3d_surface(self, x_col, y_col, z_col):
        """
        Створення 3D поверхні
        
        Параметри:
            x_col, y_col, z_col (str): Назви стовпців для осей
        """
        try:
            print("\n  Створення 3D поверхні...")
            
            # Підготовка даних для поверхні (створення сітки)
            x_unique = sorted(self.data[x_col].unique())
            y_unique = sorted(self.data[y_col].unique())
            
            # Створення сітки значень
            z_matrix = np.zeros((len(y_unique), len(x_unique)))
            
            for i, y_val in enumerate(y_unique):
                for j, x_val in enumerate(x_unique):
                    mask = (self.data[x_col] == x_val) & (self.data[y_col] == y_val)
                    if mask.any():
                        z_matrix[i, j] = self.data.loc[mask, z_col].mean()
            
            fig = go.Figure(data=[go.Surface(
                x=x_unique,
                y=y_unique,
                z=z_matrix,
                colorscale='Viridis'
            )])
            
            fig.update_layout(
                title=f'3D Поверхня: {z_col} від {x_col} та {y_col}',
                scene=dict(
                    xaxis_title=x_col,
                    yaxis_title=y_col,
                    zaxis_title=z_col
                ),
                width=1000,
                height=800
            )
            
            output_file = 'surface_3d.html'
            fig.write_html(output_file)
            print(f"  3D поверхня збережена: {output_file}")
            fig.show()
            
        except Exception as e:
            print(f"  Помилка створення поверхні: {e}")
    
    def create_3d_line(self, x_col, y_col, z_col):
        """
        Створення 3D лінійного графіка
        
        Параметри:
            x_col, y_col, z_col (str): Назви стовпців для осей
        """
        try:
            print("\n Створення 3D лінійного графіка...")
            
            fig = go.Figure(data=[go.Scatter3d(
                x=self.data[x_col],
                y=self.data[y_col],
                z=self.data[z_col],
                mode='lines+markers',
                marker=dict(size=4, color='red'),
                line=dict(color='blue', width=2)
            )])
            
            fig.update_layout(
                title=f'3D Лінійний графік: {x_col}, {y_col}, {z_col}',
                scene=dict(
                    xaxis_title=x_col,
                    yaxis_title=y_col,
                    zaxis_title=z_col
                ),
                width=1000,
                height=800
            )
            
            output_file = 'line_3d.html'
            fig.write_html(output_file)
            print(f" 3D лінійний графік збережений: {output_file}")
            fig.show()
            
        except Exception as e:
            print(f" Помилка створення графіка: {e}")
    
    def create_combined_visualization(self, x_col, y_col, z_col):
        """
        Створення комбінованої візуалізації
        
        Параметри:
            x_col, y_col, z_col (str): Назви стовпців для осей
        """
        try:
            print("\n Створення комбінованої візуалізації...")
            
            # Створення субплотів
            fig = make_subplots(
                rows=2, cols=2,
                subplot_titles=('3D Розсіювання', '2D Проекція XY', 
                               '2D Проекція XZ', '2D Проекція YZ'),
                specs=[[{'type': 'scatter3d'}, {'type': 'scatter'}],
                       [{'type': 'scatter'}, {'type': 'scatter'}]]
            )
            
            # 3D діаграма
            fig.add_trace(
                go.Scatter3d(
                    x=self.data[x_col],
                    y=self.data[y_col],
                    z=self.data[z_col],
                    mode='markers',
                    marker=dict(size=4, color=self.data[z_col], colorscale='Viridis')
                ),
                row=1, col=1
            )
            
            # Проекція XY
            fig.add_trace(
                go.Scatter(
                    x=self.data[x_col],
                    y=self.data[y_col],
                    mode='markers',
                    marker=dict(size=5, color=self.data[z_col], colorscale='Viridis')
                ),
                row=1, col=2
            )
            
            # Проекція XZ
            fig.add_trace(
                go.Scatter(
                    x=self.data[x_col],
                    y=self.data[z_col],
                    mode='markers',
                    marker=dict(size=5, color=self.data[y_col], colorscale='Viridis')
                ),
                row=2, col=1
            )
            
            # Проекція YZ
            fig.add_trace(
                go.Scatter(
                    x=self.data[y_col],
                    y=self.data[z_col],
                    mode='markers',
                    marker=dict(size=5, color=self.data[x_col], colorscale='Viridis')
                ),
                row=2, col=2
            )
            
            fig.update_layout(
                title_text="Комбінована візуалізація 3D даних",
                height=900,
                width=1200,
                showlegend=False
            )
            
            output_file = 'combined_3d.html'
            fig.write_html(output_file)
            print(f" Комбінована візуалізація збережена: {output_file}")
            fig.show()
            
        except Exception as e:
            print(f" Помилка створення комбінованої візуалізації: {e}")


def print_menu():
    """Відображення головного меню"""
    print("\n" + "="*70)
    print("МЕНЮ ПРОГРАМИ")
    print("="*70)
    print("1. Завантажити дані з CSV файлу")
    print("2. Показати інформацію про дані")
    print("3. Створити 3D діаграму розсіювання")
    print("4. Створити 3D поверхню")
    print("5. Створити 3D лінійний графік")
    print("6. Створити комбіновану візуалізацію")
    print("7. Генерувати тестові дані")
    print("0. Вихід")
    print("="*70)


def generate_sample_data():
    """
    Генерація тестових даних для демонстрації
    """
    try:
        print("\n  Генерація тестових даних...")
        
        # Генерація випадкових 3D даних
        np.random.seed(42)
        n_points = 100
        
        x = np.random.uniform(0, 10, n_points)
        y = np.random.uniform(0, 10, n_points)
        z = np.sin(x) * np.cos(y) + np.random.normal(0, 0.1, n_points)
        
        # Додаткові параметри
        temperature = x * 10 + np.random.normal(0, 5, n_points)
        pressure = y * 2 + np.random.normal(0, 1, n_points)
        
        df = pd.DataFrame({
            'X_coordinate': x,
            'Y_coordinate': y,
            'Z_value': z,
            'Temperature': temperature,
            'Pressure': pressure
        })
        
        filename = 'sample_3d_data.csv'
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f" Тестові дані згенеровано та збережено в файл: {filename}")
        print(f"  Розмір: {len(df)} записів")
        return filename
        
    except Exception as e:
        print(f"  Помилка генерації даних: {e}")
        return None


def main():
    """
    Головна функція програми
    """
    print("="*70)
    print(" "*15 + "ВІЗУАЛІЗАЦІЯ ТРИВИМІРНИХ ДАНИХ")
    print(" "*20 + "Бібліотека: Plotly")
    print("="*70)
    
    visualizer = DataVisualizer3D()
    
    while True:
        try:
            print_menu()
            choice = input("\nВаш вибір: ").strip()
            
            if choice == '0':
                print("\n  Дякуємо за використання програми!")
                sys.exit(0)
            
            elif choice == '1':
                filename = input("\nВведіть шлях до CSV файлу: ").strip()
                if visualizer.load_csv_data(filename):
                    visualizer.validate_data()
            
            elif choice == '2':
                visualizer.show_data_info()
            
            elif choice == '3':
                if visualizer.data is None:
                    print("  Спочатку завантажте дані (пункт 1)")
                    continue
                columns = visualizer.select_columns()
                if columns:
                    x_col, y_col, z_col = columns
                    visualizer.create_3d_scatter(x_col, y_col, z_col)
            
            elif choice == '4':
                if visualizer.data is None:
                    print("  Спочатку завантажте дані (пункт 1)")
                    continue
                columns = visualizer.select_columns()
                if columns:
                    x_col, y_col, z_col = columns
                    visualizer.create_3d_surface(x_col, y_col, z_col)
            
            elif choice == '5':
                if visualizer.data is None:
                    print("  Спочатку завантажте дані (пункт 1)")
                    continue
                columns = visualizer.select_columns()
                if columns:
                    x_col, y_col, z_col = columns
                    visualizer.create_3d_line(x_col, y_col, z_col)
            
            elif choice == '6':
                if visualizer.data is None:
                    print("  Спочатку завантажте дані (пункт 1)")
                    continue
                columns = visualizer.select_columns()
                if columns:
                    x_col, y_col, z_col = columns
                    visualizer.create_combined_visualization(x_col, y_col, z_col)
            
            elif choice == '7':
                filename = generate_sample_data()
                if filename:
                    load_choice = input("\nЗавантажити згенеровані дані? (y/n): ").lower()
                    if load_choice == 'y':
                        visualizer.load_csv_data(filename)
                        visualizer.validate_data()
            
            else:
                print("  Невірний вибір. Спробуйте ще раз.")
        
        except KeyboardInterrupt:
            print("\n\n  Програму перервано користувачем")
            sys.exit(0)
        except Exception as e:
            print(f"\n  Непередбачена помилка: {e}")
            continue


if __name__ == "__main__":
    main()