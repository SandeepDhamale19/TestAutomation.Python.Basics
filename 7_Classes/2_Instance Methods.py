from Custom_Functions import ClassHelpers

fun_flight = ClassHelpers.Flight()
flight_number = fun_flight.number()
print("\t" + str(flight_number))

print("\n\t1. Initialisation method: __init__()")
fun_flight = ClassHelpers.Flight_Initialisation_Method_Class("SN060")
flight_number = fun_flight.get_flight_number()
print("\tFlight number: " + str(flight_number))

print("\n\t2. Calss Invariants:")
#fun_flight = ClassHelpers.Flight_Class_Variants("060") # ValueError: No Airline code in '060
#fun_flight = ClassHelpers.Flight_Class_Variants("sn060") # ValueError: Invalid Airline code 'sn060'
#fun_flight = ClassHelpers.Flight_Class_Variants("SN10000") # ValueError: Invalid Airline code 'sn060'
flight_number = fun_flight.get_flight_number()
print("\tFlight number: " + str(flight_number))


print("\nGet registration plan: ")
my_flight = ClassHelpers.Flight_Class_Multiple_Init("AI-814","Airbus 319", num_rows=22, num_seat_per_row=6)
my_flight_registration = my_flight.fun_registration()
my_flight_model = my_flight.fun_model()
my_flight_seat_no = my_flight.fun_seating_plan()
print("\tMy flight registration: " + str(my_flight_registration))
print("\tMy flight model: " + str(my_flight_model))
print("\tMy flight seat no: " + str(my_flight_seat_no))

print("\nClass collaboration: ")
my_flight_model = ClassHelpers.base_flight_class_collboration("BA345", ClassHelpers.Flight_Class_Multiple_Init("AI-814","Airbus 319", num_rows=22, num_seat_per_row=6))
print("\t My flight model: " + str(my_flight_model.flight_model()))







