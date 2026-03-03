# data_generator.py
import random

# Списки для генерации
names = [f"Пациент_{i}" for i in range(1, 1001)] # 1000 уникальных имен
symptoms_pool = ["температура", "кашель", "слабость", "головная боль", "насморк",
                 "зуд", "высыпания", "отек", "слезотечение", "потеря сознания",
                 "тошнота", "рвота", "звон в ушах", "амнезия", "головокружение",
                 "нарушение координации, речи", "асимметрия лица", "одышка", "боль в грудной клетке"]
sexes = ["male", "female", "unknown"]
results_pool = ["recovered", "improved", "no_change", "worsened", "deceased"]

def generate_patient_records(count, predictor):
    """Генератор, создающий полные записи пациентов."""
    for i in range(count):
        try:
            name = random.choice(names)
            age = random.randint(5, 100)
            sex = random.choice(sexes)
            countSymptoms = random.randint(1, 5)
            symptoms = random.sample(symptoms_pool, countSymptoms)

            # Создаем пациента
            patient = Patient(name, age, symptoms, sex=sex)

            # Прогнозируем диагноз и лечение
            # predictor передается как аргумент, чтобы не создавать его каждый раз
            predictor.predictAndPrescribe(patient)

            # Симулируем результат лечения
            # Это упрощенная логика, можно сделать сложнее
            base_duration = random.randint(3, 30)
            side_effects = random.sample(["головная боль", "тошнота", "сонливость", "бессонница"], random.randint(0, 2))
            # Результат может зависеть от диагноза, лечения, возраста (для простоты - рандом)
            result_prob = random.random()
            if result_prob < 0.6:
                result = "recovered"
            elif result_prob < 0.8:
                result = "improved"
            elif result_prob < 0.9:
                result = "no_change"
            else:
                result = "worsened" # или "deceased" с меньшей вероятностью

            outcome = TreatmentOutcome(result, base_duration, side_effects)
            patient.outcome = outcome

            yield patient

        except Exception as e:
            # Обработка ошибки в генераторе
            print(f"Ошибка генерации записи {i}: {e}")
            # В реальной системе можно было бы логировать в файл
            continue # Пропускаем ошибочную запись
