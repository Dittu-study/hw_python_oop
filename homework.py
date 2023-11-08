class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, training_type, duration, distance, speed, calories):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        return ('Тип тренировки: {self.training_type}; Длительность: {self.duration} ч.; '
                'Дистанция: {self.distance} км; Ср. скорость: {self.speed} км/ч; '
                'Потрачено ккал: {self.calories}.')

class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.LEN_STEP: list[float] = [0.65, 1.38]
        self.M_IN_KM: int = 1000

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        #action * LEN_STEP / M_IN_KM
        return self.action * self.LEN_STEP[0] / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        #преодолённая_дистанция_за_тренировку / время_тренировки
        self.minutes_in_hour: int = 60 * self.duration
        return self.get_distance() / (self.duration * self.minutes_in_hour)

    def get_spend_calories(self) -> float:
        """Получить количество затраченных калорий."""
        self.CALORIES_MEAN_SPEED_MULTIPLIER: int = 18
        self.CALORIES_MEAN_SPEED_SHIFT: float = 1.79

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        info = InfoMessage()
        return info
        

class Running(Training):
    """Тренировка: бег."""
    def get_spend_calories(self) -> float:
    #(18 * средняя_скорость + 1.79) * вес_спортсмена / M_IN_KM * время_тренировки_в_минутах
        return ((self.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_mean_speed() + self.CALORIES_MEAN_SPEED_SHIFT)
                * self.weight / self.M_IN_KM * self.minutes_in_hour)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def get_spend_calories(self, height: int) -> float:
        self.heigh = height
        self.K_1 = 0.035
        self.K_2 = 0.029
        #((0.035 * вес + (средняя_скорость_в_метрах_в_секунду**2 / рост_в_метрах)
        #* 0.029 * вес) * время_тренировки_в_минутах)
        return (self.K_1 * self.weight + (self.get_mean_speed**2 / self.heigh) * self.K_2 * self.weight) * self.minutes_in_hour


class Swimming(Training):
    """Тренировка: плавание."""
    def get_distance(self) -> float:
        #action * LEN_STEP / M_IN_KM
        return self.action * self.LEN_STEP[1] / self.M_IN_KM

    def get_mean_speed(self, length_pool: int, count_pool: int) -> float:
        #длина_бассейна * count_pool / M_IN_KM / время_тренировки
        self.length_pool = length_pool
        self.count_pool = count_pool
        return self.length_pool * self.count_pool / self.M_IN_KM / self.minutes_in_hour
    
    def get_spent_calories(self) -> float:
        self.K_3 = 1.1
        self.K_4 = 2
        #(средняя_скорость + 1.1) * 2 * вес * время_тренировки
        return (self.get_mean_speed() + self.K_3) * self.K_4 * self.weight * self.minutes_in_hour


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    packages_true = {}
    if workout_type == 'WLK':
        packages_true[workout_type] = data
        wlk = SportsWalking
        return wlk
    if workout_type == 'RUN':
        packages_true[workout_type] = data
        run = Running
        return run
    if workout_type == 'SWM':
        packages_true[workout_type] = data
        swm = Swimming
        return swm

def main(training: Training) -> None:
    """Главная функция."""
    def show_training_info() -> str:
        print(InfoMessage.get_message)

if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
