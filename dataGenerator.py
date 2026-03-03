import random
from medical_entities import Patient, Diagnosis, Treatment, TreatmentOutcome
import medical_entities

names = [f"Пациент_{i}" for i in range(1, 1001)]
symptomsPool = ["температура", "кашель", "слабость", "головная боль", "насморк",
                 "зуд", "высыпания", "отек", "слезотечение", "потеря сознания",
                 "тошнота", "рвота", "звон в ушах", "амнезия", "головокружение",
                 "нарушение координации, речи", "асимметрия лица", "одышка", "боль в грудной клетке"]
sexes = ["male", "female", "unknown"]
resultsPool = ["recovered", "improved", "no_change", "worsened", "deceased"]


def generate_patient_records(count):
    predictor = DiagnosisPredictor()

    for i in range(count):
        try:
            name = random.choice(names)
            age = random.randint(5, 100)
            sex = random.choice(sexes)
            countSymptoms = random.randint(1, 5)
            symptoms = random.sample(symptoms_pool, countSymptoms)

            patient = Patient(name, age, symptoms, sex=sex)

            diagnosis, treatment = predictor.predict_and_prescribe(patient)

            base_duration = random.randint(3, 30)
            side_effects = random.sample(["головная боль", "тошнота", "сонливость", "бессонница"], random.randint(0, 2))
            result_prob = random.random()
            if result_prob < 0.6:
                result = "recovered"
            elif result_prob < 0.8:
                result = "improved"
            elif result_prob < 0.9:
                result = "no_change"
            else:
                result = "worsened"

            outcome = TreatmentOutcome(result, base_duration, side_effects)
            patient.outcome = outcome

            yield patient

        except Exception as e:
            print(f"Ошибка генерации записи {i}: {e}")
            continue
