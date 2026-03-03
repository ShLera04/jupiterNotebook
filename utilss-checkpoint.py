# utils.py
import time
import threading

# --- Декоратор для измерения времени выполнения ---
def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"[LOG] Начало выполнения функции '{func.__name__}'...")
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"[ERROR] Ошибка в функции '{func.__name__}': {e}")
            raise # Переподнимаем исключение
        finally:
            end_time = time.time()
            print(f"[LOG] Функция '{func.__name__}' выполнена за {end_time - start_time:.4f} секунд.\n")
        return result
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

# --- Блокировка для потоков ---
print_lock = threading.Lock()

def thread_safe_print(message):
    """Потокобезопасный принт."""
    with print_lock:
        print(message)

# --- Вспомогательная функция из старого кода (если нужно) ---
def countPatientsByDiagnosis(patients, diagnosis_name):
    """Подсчитывает количество пациентов с указанным диагнозом."""
    count = 0
    for p in patients:
        # Проверяем, является ли диагноз объектом и совпадает ли имя
        if p.diagnosis and hasattr(p.diagnosis, 'name') and p.diagnosis.name == diagnosis_name:
            count += 1
    return count
