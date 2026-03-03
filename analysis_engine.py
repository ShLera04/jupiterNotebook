# analysis_engine.py
from functools import reduce
from collections import Counter
import operator # Для reduce
import traceback # Для try/except

# --- Вспомогательные функции анализа ---

@log_execution_time # Применяем декоратор
def analyze_treatment_effectiveness(records):
    """
    Анализирует эффективность лечения.
    Возвращает словарь с процентами успешных исходов для каждого лечения.
    """
    print("\n--- Анализ эффективности лечения ---")
    try:
        # Сгруппируем результаты по лечению
        treatment_results = {}
        for patient in records:
            # Используем строковое представление лечения как ключ
            treatment_name = str(patient.treatment)
            outcome_result = patient.outcome.result
            if treatment_name not in treatment_results:
                treatment_results[treatment_name] = []
            treatment_results[treatment_name].append(outcome_result)

        effectiveness = {}
        for treatment, outcomes in treatment_results.items():
            # Подсчитаем успешные исходы ('recovered', 'improved')
            successful = sum(1 for o in outcomes if o in ['recovered', 'improved'])
            total = len(outcomes)
            if total > 0:
                effectiveness[treatment] = round((successful / total) * 100, 2)
            else:
                effectiveness[treatment] = 0 # Избежать деления на 0

        print("Эффективность лечения (%):")
        for treatment, eff in sorted(effectiveness.items(), key=operator.itemgetter(1), reverse=True):
             print(f"  {treatment}: {eff}%")

        return effectiveness

    except ZeroDivisionError:
        print("Ошибка: Деление на ноль при подсчете эффективности.")
        return {}
    except Exception as e:
        print(f"Ошибка при анализе эффективности лечения: {e}")
        traceback.print_exc()
        return {}


@log_execution_time
def identify_risk_factors(records):
    """
    Простой анализ факторов риска.
    Возвращает Counter с симптомами, часто встречающимися при плохом исходе.
    """
    print("\n--- Анализ факторов риска (частые симптомы при плохом исходе) ---")
    try:
        # Найдем пациентов с плохим исходом с помощью filter
        bad_outcome_patients = list(filter(lambda p: p.outcome.result in ['worsened', 'deceased'], records))

        # Подсчитаем симптомы у этих пациентов с помощью map и Counter
        all_risk_symptoms = []
        # Используем map для извлечения списков симптомов
        symptom_lists = map(lambda p: p.symptoms, bad_outcome_patients)
        # Распаковываем списки в один общий список
        for symptom_list in symptom_lists:
            all_risk_symptoms.extend(symptom_list)

        risk_counter = Counter(all_risk_symptoms)
        most_common_risks = risk_counter.most_common(5) # 5 самых частых

        print("Топ-5 симптомов, связанных с плохим исходом:")
        for symptom, count in most_common_risks:
            print(f"  {symptom}: {count} случаев")

        return risk_counter

    except Exception as e:
        print(f"Ошибка при анализе факторов риска: {e}")
        traceback.print_exc()
        return Counter()


@log_execution_time
def analyze_patient_demographics(records):
    """
    Анализирует демографические данные и исходы (например, по возрасту).
    """
    print("\n--- Анализ по возрасту ---")
    try:
        # Сгруппируем по возрастным группам
        age_groups = {"<30": [], "30-50": [], "50-70": [], ">70": []}
        for p in records:
            age = p.age
            if age < 30:
                group = "<30"
            elif 30 <= age < 50:
                group = "30-50"
            elif 50 <= age < 70:
                group = "50-70"
            else:
                group = ">70"
            age_groups[group].append(p)

        age_outcomes = {}
        for group, patients in age_groups.items():
            # Используем map для извлечения результатов лечения
            outcomes_in_group = list(map(lambda p: p.outcome.result, patients))
            outcome_counts = dict(Counter(outcomes_in_group))
            age_outcomes[group] = outcome_counts
            print(f"  Группа {group}: {outcome_counts}")

        return age_outcomes

    except Exception as e:
        print(f"Ошибка при анализе по возрасту: {e}")
        traceback.print_exc()
        return {}

# --- Пример использования reduce ---
@log_execution_time
def calculate_total_treatment_duration(records):
    """
    Использует reduce для суммирования длительности лечения.
    """
    try:
        total_days = reduce(lambda acc, p: acc + p.outcome.duration, records, 0)
        print(f"\n--- Общая длительность лечения по всем пациентам: {total_days} дней ---")
        return total_days
    except Exception as e:
        print(f"Ошибка при подсчете общей длительности: {e}")
        return 0
