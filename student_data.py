import pandas as pd

class StudentData():
    def __init__(self, data_array):
        self.data = self.convert_to_frame(self.convert_data(data_array))

    def convert_data(self, data_array):
        result = []
        gender_dict = {'М': 0,'Ж': 1}
        job_act_dict = {'Есть': 1, 'Нет': 0}
        career_dict = {
            "Бухгалтер": 0,
            "Художник": 1,
            "Банкир": 2,
            "Владелец бизнеса": 3,
            "Инженер-строитель": 4,
            "Дизайнер": 5,
            "Доктор": 6,
            "Разработчик игр": 7,
            "Гос служащий": 8,
            "Юрист": 9,
            "Застройщик": 10,
            "Учёный": 11,
            "Инженер ПО": 12,
            "Инвестор": 13,
            "Преподаватель": 14,
            "Неизвестно": 15,
            "Писатель":16
        }

        #gender, part_time_job, absence_days, activities, hours, career - correct order
        #gender, hours, career, part_time_job, activities, absence_days - app order
        result.append(gender_dict[data_array[0]])
        result.append(job_act_dict[data_array[3]])
        result.append(int(data_array[5]))
        result.append(job_act_dict[data_array[4]])
        result.append(int(data_array[1]))
        result.append(career_dict[data_array[2]])
        return result
    
    def convert_to_frame(self, data_array):
        return pd.DataFrame([data_array], columns=['gender', 'part_time_job', 'absence_days', 'extracurricular_activities',
                                                 'weekly_self_study_hours', 'career_aspiration'])

