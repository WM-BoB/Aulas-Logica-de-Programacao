class Car:
    """Represents a car with a model name and manufacturing year.

    Attributes:
        model (str): The model name of the car.
        year (int): The year the car was manufactured.
    """

    def __init__(self, model, year):
        """Initializes a Car instance.

        Args:
            model (str): The model name of the car.
            year (int): The year the car was manufactured.
        """
        self.model = model
        self.year = year

    def __str__(self):
        """Returns a readable string representation of the car.

        Returns:
            str: The car formatted as "<year> - <model>", e.g. "2020 - Civic".
        """
        return f"{self.year} - {self.model}"

    def get_model(self):
        """Returns the model name of the car.

        Returns:
            str: The car's model name.
        """
        return self.model

    def get_year(self):
        """Returns the manufacturing year of the car.

        Returns:
            int: The year the car was manufactured.
        """
        return self.year
