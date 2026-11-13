x = "hello"
weather_type = "sunny"
temp_high = 70
temp_low = 50
probability_of_rain = 0.2
print(
    f"The weather today is {weather_type} with a high of {temp_high}°F and a low of {temp_low}°F. There is a {probability_of_rain * 100}% chance of rain."
)
# if the temperature is above 80 degrees, print a message saying it's going to be a hot day. Otherwise, print a message saying the temperature is moderate.
if temp_high > 80:
    print("It's going to be a hot day! Stay hydrated.")
    if temp_high > 90:
        print("It's going to be a very hot day! Stay indoors if possible.")
elif temp_high < 60:
    print("It's going to be a cold day! Dress warmly.")
elif temp_high < 70:
    print("It's going to be a cool day! You might want to bring a light jacket.")
else:
    print("The temperature is moderate today. Enjoy your day!")

if probability_of_rain > 0.5:
    print("There's a high chance of rain today. Don't forget your umbrella!")
