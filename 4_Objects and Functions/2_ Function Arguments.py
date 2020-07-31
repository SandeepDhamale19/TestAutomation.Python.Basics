from Custom_Functions import DateTimeHelpers
import time
print("1. Default Arguments.")


def banner(message, border='_'):
    print("\t" + border * len(message))
    print("\t" + message)
    print("\t" + border * len(message))


print("\tInvoke function with default argument")
banner("Sandeep Dhamale")

print("\n\tInvoke function with function argument")
banner("Sandeep Dhamale", "*")

print("\n\tNote1: arguments with no assigned name are called as Positional arguments and must kept at beginning.")
print("\tPositional arguments are matched by their position in argument list.")
print("\te.g. banner('Sandeep Dhamale', border='*') - Here 'Sandeep Dhamale' is Positional argument.")
print("\n\tNote2: arguments with assigned are called as keyword arguments.")
print("\tKeyword arguments are matched by assigned name. They can be placed in any order after positional arguments.")
print("\te.g. banner('Sandeep Dhamale', border='*') - Here '*' is Keyword argument with assigned name border.")
print("\te.g. banner(message ='Sandeep Dhamale', border='*') - Here both 'Sandeep Dhamale' and *' are Keyword "
      "arguments as both have assigned name border.")
print("\tbanner(message ='Sandeep Dhamale', border='*') is same as banner(border='*', message ='Sandeep Dhamale')")

print("\n3. Issues with using mutable arguments as default argumets.")

print("\tCurrent Time: " + str(DateTimeHelpers.show_time_mutable_arguments()))
time.sleep(2)
print("\tTime after 2 seconds : " + str(DateTimeHelpers.show_time_mutable_arguments()) + ". :O this is same as time earlier 2 seconds!")
time.sleep(2)
print("\n\tAlways use immutable arguments.")
print("\tTime again after 2 seconds : " + str(DateTimeHelpers.show_time_immutable_arguments() + ". We have a new time!"))
