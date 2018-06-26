# mi, km, ft, m, in, gal, L, all metric prefixes of meters
def distanceconv():
    input_unit_dict = {"mi":1609.34 , "ft":0.3048, "in":0.0254,"Em":10**18, "Pm":10**15,"Tm":10**12, "Gm":10**9, "Mm":10**6,
    "km": 1000, "hm":100, "dam":10, "m":1, "dm":0.1, "cm":0.01, "mm":0.001, "um":10**-6, "nm":10**-9, "pm":10**-12, "fm":10**-15, "am":10**-18}
    ouput_unit_dict = {"mi":0.000321371, "ft":3.28084, "in":39.3701, "Em":10**-18, "Pm":10**-15, "Tm":10**-12, "Gm":10**-9,
    "Mm":10**-6, "km":.001, "hm":.01, "dam":.1, "m":1, "dm":10, "cm":100, "mm":1000, "um":10**6, "nm":10**9, "pm":10**12, "fm":10**15, "am":10**18}
    distance = float(input("Enter a distance: "))
    input_units = input("Enter units: ")
    while input_units not in ["mi", "ft", "in", "Em", "Pm", "Tm", "Gm", "Mm", "km", "hm", "dam", "m", "dm", "cm", "mm", "um", "nm", "pm", "fm", "am"]:
        input_units = input("Enter units: ")
    output_units = input("Enter target units: ")
    while output_units not in ["mi", "ft", "in", "Em", "Pm", "Tm", "Gm", "Mm", "km", "hm", "dam", "m", "dm", "cm", "mm", "um", "nm", "pm", "fm", "am"]:
        output_units = input("Enter target units: ")
    distance = (distance * input_unit_dict[input_units]) * ouput_unit_dict[output_units]
    return str(distance) + " " + output_units
print(distanceconv())
