number_of_month = int(input())

number_of_month = number_of_month // 3;

all_rating = {
    1: 'зима',
    2: 'весна',
    3: 'лето',
    4: 'зима'
}

# a=input('a= ')

if number_of_month in all_rating:
    print(all_rating[number_of_month])
else:
    print('ошибка')
