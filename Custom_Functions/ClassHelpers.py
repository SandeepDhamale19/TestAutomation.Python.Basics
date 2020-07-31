class Flight:
    def number(self):
        return "SN060"


class Flight_Initialisation_Method_Class:
    def __init__(self, number):
        """
        This is initializer, not a constructor.
        Initializer should not return anything.
        self is similar to this in Java/ C#
        :param number:
        """
        self._number = number

    def get_flight_number(self):
        return self._number


class Flight_Class_Variants:
    def __init__(self, number):
        # 1st Two characters should not be numbers
        if not number[:2].isalpha():
            raise ValueError(f"No Airline code in '{number}'")
        # 1st Two characters should be uppercase
        if not number[:2].isupper():
            raise ValueError(f"Invalid Airline code '{number}'")
        # Airline code should be digits except 1st two characters and should be <9999
        if not number[2:].isdigit() or int(number[2:])>=9999:
            raise ValueError(f"Invalid route code '{number}'")
        self._number = number

    def get_flight_number(self):
        return self._number

class Flight_Class_Multiple_Init:
    def __init__(self, registration, model, num_rows, num_seat_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seat_per_row = num_seat_per_row

    def fun_registration(self):
        return self._registration

    def fun_model(self):
        return self._model

    def fun_seating_plan(self):
        seat_num = range(1, self._num_rows+1)
        seat_character = "ABCDEFGHJK"[:self._num_seat_per_row] #Seat number does not include I to avoid confusion with 1
        return seat_num, seat_character

# Reusing classes and their methods: Collaboration
class base_flight_class_collboration:
    def __init__(self, number, Flight_Class_Multiple_Init):
        self._number = number
        self._aircraft = Flight_Class_Multiple_Init

    def flight_model(self):
        return self._aircraft.fun_model()

#Seat booking System
class Flight:
    def __init__(self, number, aircraft):
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.fun_seating_plan()