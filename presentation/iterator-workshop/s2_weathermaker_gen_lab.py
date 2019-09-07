
import random

def weathermaker(volatility, days):
    '''
    Yield a series of messages giving the day's weather and occasional commentary

    volatility ‑ a float between 0 and 1; the greater this number the greater
                    the likelihood that the weather will change on each given day
    days ‑ number of days for which to generate weather
    '''
    #Always start as if yesterday were sunny
    current_weather = 'sunny'
    #First item is the probability that the weather will stay the same
    #Second item is the probability that the weather will change
    #The higher the volatility the greater the likelihood of change
    weights = 1.0‑volatility, volatility    #For fun track how many sunny days in a row there have been
    sunny_run = 1
    #How many rainy days in a row there have been
    rainy_run = 0
    for day in range(days):
        #Figure out the opposite of the current weather
        other_weather = 'rainy' if current_weather == 'sunny' else 'sunny'
        #Set up to choose the next day's weather. First set up the choices
        choose_from = current_weather, other_weather        #random.choices returns a list of random choices based on the weights
        #By default a list of 1 item, so we grab that first and only item with 0        current_weather = random.choices(choose_from, weights)0        yield 'today it is ' + current_weather
        if current_weather == 'sunny':
            #Check for runs of three or more sunny days
            sunny_run += 1
            rainy_run = 0
            if sunny_run >= 3:
                yield "Uh oh! We're getting thirsty!"
        else:
            #Check for runs of three or more rainy days
            rainy_run += 1
            sunny_run = 0
            if rainy_run >= 3:
                yield "Rain, rain go away!"
    return

#Create a generator object and print its series of messages
for msg in weathermaker(0.2, 10):
    print(msg)