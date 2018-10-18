import machine, math

def get_temp(_pin):
    # Inputs ADC Value from Thermistor and outputs temperature in Celsius
    raw_ADC = machine.ADC(_pin).read()

    # Assuming a 10k Thermistor.  Calculation is actually: resistance = (1024/ADC)
    resistance=((10240000/raw_ADC) - 10000)

    #   *****************************************************************
    #   * Utilizes the Steinhart-Hart Thermistor Equation:				*
    #   *    temperature in Kelvin = 1 / {A + B[ln(R)] + C[ln(R)]^3}	*
    #   *    where A = 0.001129148, B = 0.000234125 and C = 8.76741E-08	*
    #   *****************************************************************
    temp = math.log(resistance)
    temp = 1 / (0.001129148 + (0.000234125 * temp) + (0.0000000876741 * temp * temp * temp))
    temp = temp - 273.15;  # Convert Kelvin to Celsius

    # Uncomment this line for the function to return Fahrenheit instead.
    # temp = (temp * 9.0)/ 5.0 + 32.0 # Convert to Fahrenheit

    return temp  # Return the temperature