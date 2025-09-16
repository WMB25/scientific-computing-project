import numpy as np

temperaturas = np.array([2.5, 3.2, 5.1, 6.3, 7.0, 8.1, 10.5, 9.8, 8.5, 7.3,
    6.2, 5.1, 4.5, 3.8, 5.6, 6.7, 7.2, 8.3, 10.1, 9.4,
    8.2, 7.0, 6.3, 5.4, 4.7, 3.9, 5.8, 6.9, 7.4, 8.5,
    10.3, 9.6, 8.4, 7.2, 6.5, 5.6, 4.9, 4.1, 5.9, 7.0,
    7.5, 8.6, 10.4, 9.7, 8.5, 7.3, 6.6, 5.7, 5.0, 4.2,
    6.0, 7.1, 7.6, 8.7, 10.6, 9.9, 8.7, 7.5, 6.8, 5.9,
    5.2, 4.4, 6.1, 7.2, 7.7, 8.8, 10.7, 10.0, 8.8, 7.6,
    6.9, 6.0, 5.3, 4.5, 6.2, 7.3, 7.8, 8.9, 10.8, 10.2,
    9.0, 7.8, 7.1, 6.2, 5.5, 4.7, 6.3, 7.4, 7.9, 9.0,
    10.9, 10.3, 9.1, 7.9, 7.2, 6.3, 5.6, 4.8, 6.4, 7.5])

statiscal_average = np.mean(temperaturas)
median_statistic = np.median(temperaturas)
standard_deviation = np.std(temperaturas)

cold = temperaturas < 5
moderates = (temperaturas >= 5) & (temperaturas <= 15)
hot = temperaturas > 15

days_cold = np.sum(cold)
days_moderates = np.sum(moderates)
days_hot = np.sum(hot)

very_hot_day= np.argmin(temperaturas)
temp_very_hot_day = np.max(temperaturas)
very_cold_day = np.argmax(temperaturas)
temp_very_cold_day = np.min(temperaturas)

print(f"Media de temperatura: {statiscal_average:.2f}C")
print(f"Mediana da temperatura: {median_statistic:.2f}C")
print(f"Desvio de padrões de temperatura: {standard_deviation:.2f}C\n")

print(f"Temperaturas abaixo de 5 graus: {days_cold} dias")
print(f"Temperaturas entre e e 15 garus: {days_moderates} dias")
print(f"Temperaturas Acima de 15 graus: {days_hot} dias\n")

print(f"Dia mais frio: {very_cold_day} -> {temp_very_cold_day}C")
print(f"Dia mais quente: {very_hot_day} -> {temp_very_hot_day}C")
