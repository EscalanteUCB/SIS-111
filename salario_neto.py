'''
Calcular el salario neto de un empleado.
    Datos de entrada:
      - Salario bruto
      - Porcentaje de IVA (ej. 13)
      - Porcentaje de IT (ej. 3)
    Fórmula:
      Salario neto = Salario bruto - [(Salario bruto * % IVA) + (Salario bruto * % IT)]
'''
def calcular_salario_neto():
    # 1. Ingresar salario bruto y porcentajes
    salario_bruto = float(input("Ingrese el salario bruto: "))
    # Impuesto al valor agregado
    iva_porcentaje = 13 
    # Impuesto a la transferencia
    it_porcentaje = 3 

    # 2. Calcular las deducciones
    deduccion_iva = (salario_bruto * (iva_porcentaje / 100))
    deduccion_it = (salario_bruto * (it_porcentaje / 100))
    deducciones = deduccion_iva + deduccion_it

    # 3. Restar las deducciones al salario bruto
    salario_neto = salario_bruto - deducciones

    # 4. Mostrar salario neto
    print(f"Salario Bruto: {salario_bruto}")
    print(f"Total Deducciones (IVA): {deduccion_iva}")
    print(f"Total Deducciones (IT): {deduccion_it}")
    print(f"Total Deducciones (IVA + IT): {deducciones}")
    print(f"Salario Neto: {salario_neto}")


# Ejecución de la función 
calcular_salario_neto()


