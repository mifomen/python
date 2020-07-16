all_rating = {
    '1': 'плохо',
    '2': 'неудовлетворительно',
    '3': 'удовлетворительно',
    '4': 'хорошо',
    '5': 'отлично'
}

a=input('a= ')

if a in all_rating:
    print(all_rating[a])
else:
    print('ошибка')
