def distance_converter():
    distance = float(input("Enter a distance: "))
    input_units = input("Enter units: ")
    while input_units.lower() not in ["mi", "km", "ft", "m"]:
        input_units = input("Enter units: ")
    output_units = input("Enter target units: ")
    while output_units.lower() not in ["mi", "km", "ft", "m"]:
        output_units = input("Enter target units: ")
    if input_units == "mi":
        if output_units == "mi":
            return str(distance) + " " + output_units
        if output_units == "km":
            return str(distance * 1.60934) + " " + output_units
        if output_units == "ft":
            return str(distance * 5280.0) + " " + output_units
        if output_units == "m":
            return str(distance * 1609.34) + " " + output_units
    if input_units == "km":
        if output_units == "mi":
            return str(distance * 0.621371) + " " + output_units
        if output_units == "km":
            return str(distance) + " " + output_units
        if output_units == "ft":
            return str(distance * 3280.84) + " " + output_units
        if output_units == "m":
            return str(distance * 1000) + " " + output_units
    if input_units == "ft":
        if output_units == "mi":
            return str(distance * 0.000189394) + " " + output_units
        if output_units == "km":
            return str(distance * 0.0003048) + " " + output_units
        if output_units == "ft":
            return str(distance) + " " + output_units
        if output_units == "m":
            return str(distance * 0.3048) + " " + output_units
    if input_units == "m":
        if output_units == "mi":
            return str(distance * 0.000621371) + " " + output_units
        if output_units == "km":
            return str(distance * 0.001) + " " + output_units
        if output_units == "ft":
            return str(distance * 3.28084) + " " + output_units
        if output_units == "m":
            return str(distance) + " " + output_units

print(distance_converter())
