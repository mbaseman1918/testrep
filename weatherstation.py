import requests

package_q = {'APPID':'28b6ba4bbbfb82760251aca5b843ff94', 'q':'Portland', 'units': 'imperial'}
package_zip = {'APPID':'28b6ba4bbbfb82760251aca5b843ff94', 'zip':'97068', 'units': 'imperial'}
answer_info = {}
def weatherapp():
    temp = input("Would you like your information in metric or imperial units? ")
    while temp.lower() not in ["metric", "imperial"]:
        temp = input("Would you like your information in metric or imperial units? ")
    if temp.lower() == "metric":
        package_q["units"] = "metric"
        package_zip["units"] = "metric"
        answer_info["units"] = "C"
    if temp.lower() == "imperial":
        package_q["units"] = "imperial"
        package_zip["units"] = "imperial"
        answer_info["units"] = "F"
    user = input("Would you like to look up your location by zip code or city name? ")
    while user.lower() not in ["zip code", "city name"]:
        user = input("Would you like to look up your location by zip code or city name? ")
    if user.lower() == "zip code":
        package_zip["zip"] = input("What is the zip? ")
        answer_info["location"] = package_zip["zip"]
        r = requests.get('http://api.openweathermap.org/data/2.5/weather', params = package_zip)
    if user.lower() == "city name":
        package_q["q"] = input("What is the city name? ")
        answer_info["location"] = package_q["q"]
        r = requests.get('http://api.openweathermap.org/data/2.5/weather', params = package_q)
    return "The temperature in {} is {} {}.".format(answer_info["location"], r.json()["main"]["temp"], answer_info["units"])

print(weatherapp())
