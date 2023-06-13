"""
Created in 2023 by Maruf Ahmed.
this function will take 5 parameters and returns a desired value based on the inputs.
this lib was created for raspberry pi pico. to add functionality like arduino.
this lib works just like arduino's CPP map() function.
"""

def Map(value, in_min, in_max, out_min, out_max):
    # check value and filter it
    if value < in_min:
        value = in_min
    elif value > in_max:
        value = in_max
    calculate = (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    return calculate
