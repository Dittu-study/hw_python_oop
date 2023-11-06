class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, training_type, duration, distance, speed, calories):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        return ('Тип тренировки: {training_type}; Длительность: {duration} ч.; '
                'Дистанция: {distance} км; Ср. скорость: {speed} км/ч; '
                'Потрачено ккал: {calories}.')

class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        pass

    def get_distance(self, action: int, duration: float, weight: float) -> float:
        """Получить дистанцию в км."""
        #action * LEN_STEP / M_IN_KM
        self.LEN_STEP: list[float] = [0.65, 1.38]
        self.M_IN_KM: int = 1000
        return action * self.LEN_STEP[0] / self.M_IN_KM

    def get_mean_speed(self, action: int, duration: float, weight: float) -> float:
        """Получить среднюю скорость движения."""
        #преодолённая_дистанция_за_тренировку / время_тренировки
        self.minutes_in_hour: int = 60
        return self.get_distance() / (duration * self.minutes_in_hour)

    def get_spend_calories(self, action: int, duration: float, weight: float) -> float:
        """Получить количество затраченных калорий."""
        self.CALORIES_MEAN_SPEED_MULTIPLIER: int = 18
        self.CALORIES_MEAN_SPEED_SHIFT: float = 1.79

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass

class Running(Training):
    """Тренировка: бег."""
    def get_spend_calories(self) -> float:
    #(18 * средняя_скорость + 1.79) * вес_спортсмена / M_IN_KM * время_тренировки_в_минутах
        return ((self.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_mean_speed() + self.CALORIES_MEAN_SPEED_SHIFT)
                * self.weight / self.M_IN_KM * self.minutes_in_hour)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    pass


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
