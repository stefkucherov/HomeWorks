cost = int(input('Введите стоимость телефона: '))
dailysum = int(input('Ежедневные карманные деньги: '))
weeksum = dailysum * 6
days = cost // dailysum
week = cost // weeksum
print(f'Для покупки телефона понадобиться {days} дней или около {week} недель.')
