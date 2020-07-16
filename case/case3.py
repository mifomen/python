number_of_month = int(input())


all_rating = {
    1..3: 'плохо',
    4..6: 'неудовлетворительно',
    7..9: 'удовлетворительно',
    10..12: 'хорошо'
}

# a=input('a= ')

if number_of_month in all_rating:
    print(all_rating[a])
else:
    print('ошибка')
