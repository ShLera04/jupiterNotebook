def log_fun(function):
    def wrapper(*args, **kwargs):
        print(f"[log] Вызвана функция '{function.__name__}' с аргументами {args}, {kwargs}.")
        result = function(*args, **kwargs)
        print(f"[log] Функция '{function.__name__}' завершила свое выполнение.")
        return result
    return wrapper

@log_fun
def countPatientsByDiagnosis(patient, diagnosis):
    #Данная функция подсчитывает количество пациентов, которым уже был поставлен определенный диагноз.
    #Она принимает два параметра: список объектов Patient, строку с названием диагноза.
    #Возвращает количество пациентов с указанным диагнозом.
    return sum(1 for p in patient if p.diagnosis == diagnosis)