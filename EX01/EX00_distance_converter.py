VALUES = {
    'pe': 0.3048,
    'jarda': 0.9144,
    'metro': 1
}

def check_value_unit(value_unit):
    value_unit = value_unit.lower().strip().replace('é', 'e')
    if(value_unit.endswith('s')):
        value_unit = value_unit[:-1]
    return value_unit
    
print("Conversor de distancia\n")

value_unit = input("Digite a unidade que será convertida (pé, jarda, metro): ")
value = float(input("Valor: "))
value_unit_to_convert = input("Digite para o que deve ser conveertido (pé, jarda, metro): ")

origin_unit = check_value_unit(value_unit)
destination_unit = check_value_unit(value_unit_to_convert)

if(origin_unit not in VALUES or destination_unit not in VALUES):
    print("Unidade Invalida!\n")
else:
    meters = value * VALUES[origin_unit]
    result = meters / VALUES[destination_unit]

    str_result = f"{result:.4f}".replace('.', ',')
    str_result = str_result.rstrip('0').rstrip(',')
    print(f"Saída: {str_result}")
