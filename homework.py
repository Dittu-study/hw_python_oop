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

    def get_distance(self, action: int, duration: float, weight: float) -> float:
        """Получить дистанцию в км."""
        #action * LEN_STEP / M_IN_KM
        self.LEN_STEP: list[float] = [0.65, 1.38]
        self.M_IN_KM: int = 1000
        return self.action * self.LEN_STEP[0] / self.M_IN_KM

    def get_mean_speed(self, action: int, duration: float, weight: float) -> float:
        """Получить среднюю скорость движения."""
        #преодолённая_дистанция_за_тренировку / время_тренировки
        self.minutes_in_hour: int = 60
        return self.get_distance() / (self.duration * self.minutes_in_hour)

    def get_spend_calories(self, action: int, duration: float, weight: float) -> float:
        """Получить количество затраченных калорий."""
        self.CALORIES_MEAN_SPEED_MULTIPLIER: int = 18
        self.CALORIES_MEAN_SPEED_SHIFT: float = 1.79

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        InfoMessage.get_message()

class Running(Training):
    """Тренировка: бег."""
    def get_spend_calories(self) -> float:
    #(18 * средняя_скорость + 1.79) * вес_спортсмена / M_IN_KM * время_тренировки_в_минутах
    """Получить количество затраченных калорий."""
        return ((self.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_mean_speed() + self.CALORIES_MEAN_SPEED_SHIFT)
                * self.weight / self.M_IN_KM * self.minutes_in_hour)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def get_spend_calories(self, height: int) -> float:
        self.heigh = height
        #((0.035 * вес + (средняя_скорость_в_метрах_в_секунду**2 / рост_в_метрах)
        #* 0.029 * вес) * время_тренировки_в_минутах)
        """Получить количество затраченных калорий."""



class Swimming(Training):
    """Тренировка: плавание."""
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
