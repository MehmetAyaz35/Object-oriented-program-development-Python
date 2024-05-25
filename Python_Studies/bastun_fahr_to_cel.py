def fahr_to_cel(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return int(celsius) 

# def is_temperature_in_range(celsius_temperature):
#     return 82 <= celsius_temperature <= 87

def main():
    while True:
        try: # Programmet ska inte krassar om man skriver in en bokstav eftersom jag lade till en try except error method. 
            
            fahrenheit_input = float(input("Ange temperaturen i Fahrenheit för bastun: "))
            
            celsius_result = fahr_to_cel(fahrenheit_input)

            if celsius_result < 82:
                print("Det är för kallt.")
            elif celsius_result > 87:
                print("Det är för varmt.")
            else:
                print(f"Temperaturen är nu lagom på {celsius_result} grader Celsius. Bastun är redo att bada i.")
                break  # det avslutar loopen när temperaturen är lagom

        except ValueError:
            print("Fel inmatning. Ange en giltig temperatur i Fahrenheit")

if __name__ == "__main__":
    main()
