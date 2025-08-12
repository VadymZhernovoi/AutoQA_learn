class SimpleMath:
    """Класс с простыми математическими операциями."""

    def square(self, x):
        """Возвращает квадрат числа."""
        if not isinstance(x, int | float):
            return "Error! Invalid data format"
        return x * x

    def cube(self, x):
        """Возвращает куб числа."""
        if not isinstance(x, int | float):
            return "Error! Invalid data format"
        return x * x * x