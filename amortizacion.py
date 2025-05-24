import pandas as pd

def pedir_float(mensaje, minimo=0, maximo=None):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
            elif maximo is not None and valor > maximo:
                print(f"El valor debe ser menor o igual a {maximo}.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

def pedir_entero(mensaje, minimo=1):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo:
                print(f"El valor debe ser un número entero mayor o igual a {minimo}.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def amortizacion():
    print("=== Calculadora de Tabla de Amortización ===\n")
    monto = pedir_float("Ingrese el monto del préstamo: ", minimo=0.01)
    tasa = pedir_float("Ingrese la tasa mensual en % (por ejemplo, 2 para 2%): ", minimo=0)
    tasa_mensual = tasa / 100
    n = pedir_entero("Ingrese la cantidad de periodos en meses: ", minimo=1)

    pago_periodico = monto * tasa_mensual / (1 - (1 + tasa_mensual) ** -n)

    tabla_amortizacion = []
    capital_insoluto = monto

    for i in range(1, n + 1):
        intereses = capital_insoluto * tasa_mensual

        if i == n:
            amortizacion_tabla = capital_insoluto
            pago_periodico = intereses + amortizacion_tabla
            capital_insoluto = 0
        else:
            amortizacion_tabla = pago_periodico - intereses
            capital_insoluto -= amortizacion_tabla
            if capital_insoluto < 0:
                capital_insoluto = 0

        tabla_amortizacion.append({
            "Periodo": i,
            "Capital Insoluto": round(monto, 2),
            "Intereses": round(intereses, 2),
            "Pago Periódico": round(pago_periodico, 2),
            "Amortización": round(amortizacion_tabla, 2)
        })

        monto -= amortizacion_tabla

    tabla_final = pd.DataFrame(tabla_amortizacion, columns=[
        "Periodo", "Capital Insoluto", "Intereses", "Pago Periódico", "Amortización"
    ])

    print("\nTabla de amortización\n")
    print(tabla_final)

    tabla_final.to_excel("tabla_amortizacion.xlsx", index=False)
    print("\n✅ La tabla fue guardada como 'tabla_amortizacion.xlsx'.")

amortizacion()

















































    