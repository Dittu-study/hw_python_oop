from dataclasses import dataclass, asdict
from typing import ClassVar


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: object
    duration: int
    distance: float
    speed: float
    calories: float
    MESSAGE_TEMPLATE: ClassVar[str] = (
        'Тип тренировки: {training_type}; '
        'Длительность: {duration:.3f} ч.; '
        'Дистанция: {distance:.3f} км; '
        'Ср. скорость: {speed:.3f} км/ч; '
        'Потрачено ккал: {calories:.3f}.'
    )

    def get_message(self) -> str:
        return self.MESSAGE_TEMPLATE.format(**asdict(self))


class Training:
    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000
    min_in_hour: int = 60
    """Базовый класс тренировки."""
    def __init__(self,
                 action: int,
                 duration: int,
                 weight: int
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.duration_in_min: int = self.min_in_hour * self.duration

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения км/ч."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError('class must be redefined')

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.__class__.__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""
    CALORIES_MEAN_SPEED_MULTIPLIER: int = 18
    CALORIES_MEAN_SPEED_SHIFT: float = 1.79

    def get_spent_calories(self) -> float:
        return ((self.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_mean_speed()
                + self.CALORIES_MEAN_SPEED_SHIFT)
                * self.weight / self.M_IN_KM * self.duration_in_min)


class SportsWalking(Training):
    K_1: float = 0.035
    K_2: float = 0.029
    K_3_speed_meters: float = 0.278
    K_4_height_centimeter: int = 100
    """Тренировка: спортивная ходьба."""
    def __init__(self, action: int,
                 duration: int,
                 weight: int,
                 height: int) -> None:
        super().__init__(action, duration, weight)
        self.height = height
        self.height_in_meters = self.height / self.K_4_height_centimeter
        self.speed_m_min = self.get_mean_speed() * self.K_3_speed_meters

    def get_spent_calories(self) -> float:
        return ((self.K_1 * self.weight
                + (self.speed_m_min ** 2
                 / self.height_in_meters) * self.K_2
                * self.weight) * self.duration_in_min)


class Swimming(Training):
    K_4: float = 1.1
    K_5: int = 2
    LEN_STEP: float = 1.38
    """Тренировка: плавание."""
    def __init__(self, action: int, duration: float, weight: float,
                 length_pool: int, count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        return ((self.get_mean_speed() + self.K_4) * self.K_5
                * self.weight * self.duration)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    packages_true: dict = {
        'RUN': Running,
        'WLK': SportsWalking,
        'SWM': Swimming
    }
    if workout_type in packages_true:
        new_arg = packages_true[workout_type]
        return new_arg(*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    return print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
