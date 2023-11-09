class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, training_type, duration, distance, speed, calories):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        message = (f'Тип тренировки: {self.training_type}; '
                  f'Длительность: {self.duration:.3f} ч.; '
                  f'Дистанция: {self.distance:.3f} км; '
                  f'Ср. скорость: {self.speed:.3f} км/ч; '
                  f'Потрачено ккал: {self.calories:.3f}.')
        return message

class Training:
    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000
    minutes_in_hour: int = 60
    """Базовый класс тренировки."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        #action * LEN_STEP / M_IN_KM
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения км/м."""
        #преодолённая_дистанция_за_тренировку / время_тренировки
        return self.get_distance() / self.duration * self.minutes_in_hour

    def get_spend_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        info = InfoMessage()
        return info.get_message()
        

class Running(Training):
    """Тренировка: бег."""
    CALORIES_MEAN_SPEED_MULTIPLIER: int = 18
    CALORIES_MEAN_SPEED_SHIFT: float = 1.79
    def get_spend_calories(self) -> float:
    #(18 * средняя_скорость + 1.79) * вес_спортсмена 
    # / M_IN_KM * время_тренировки_в_минутах
        return ((self.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_mean_speed() 
                 + self.CALORIES_MEAN_SPEED_SHIFT) 
                 * self.weight / self.M_IN_KM * self.minutes_in_hour)


class SportsWalking(Training):
    K_1: float = 0.035
    K_2: float = 0.029
    K_3_speed_meters: float = 0.278
    K_4_duration_centimeter: int = 100
    """Тренировка: спортивная ходьба."""
    def __init__(self, action: int, 
                 duration: float, 
                 weight: float,
                 height: int,) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spend_calories(self) -> float:
        #(0.035 * вес + (средняя_скорость_в_метрах_в_секунду**2 / рост_в_метрах)
        #* 0.029 * вес) * время_тренировки_в_минутах
        return ((self.K_1 * self.weight 
                 + ((self.get_mean_speed() * self.K_3_speed_meters)** 2 
                 / (self.height * self.K_4_duration_centimeter)) 
                 * self.K_2 * self.weight) * self.minutes_in_hour)


class Swimming(Training):
    K_4: float = 1.1
    K_5: int = 2
    LEN_STEP: float = 1.38
    """Тренировка: плавание."""
    def __init__(self, action: int, duration: float, weight: float,
                 length_pool: int, count_pool: int,) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        #длина_бассейна * count_pool / M_IN_KM / время_тренировки
        return (self.length_pool * self.count_pool 
                / self.M_IN_KM / self.minutes_in_hour)
    
    def get_spent_calories(self) -> float:
        #(средняя_скорость + 1.1) * 2 * вес * время_тренировки
        return ((self.get_mean_speed() + self.K_4) * self.K_5 
                * self.weight * self.minutes_in_hour)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    packages_true = {}
    if workout_type == 'RUN':
        packages_true[workout_type] = Running
        run = Running(data)
        return run
    if workout_type == 'WLK':
        packages_true[workout_type] = SportsWalking
        wlk = SportsWalking(data)
        return wlk
    if workout_type == 'SWM':
        packages_true[workout_type] = Swimming
        swm = Swimming(data)
        return swm

def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    return info

if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
