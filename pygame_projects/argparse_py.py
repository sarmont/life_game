import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--cars', metavar='car', nargs='*',
                    type=int, default=50, help='integer from 0 to 100')

parser.add_argument('--barbie', metavar='barbie', nargs='*',
                    type=int, default=50, help='integer from 0 to 100')

parser.add_argument('--movie', metavar='movie', nargs='*',
                    choices=['melodrama', 'football', 'other'],
                    type=str,
                    default='other',
                    help='shoose - melodrama or football or other')
args = parser.parse_args()
if args.movie == 'other':
    movie = 50
else:
    if args.movie[0] == 'melodrama':
        movie = 0
    elif args.movie[0] == 'football':
        movie = 100

if type(args.barbie) is list:

    if 0 <= int(args.barbie[0]) <= 100:
        barbie = int(args.barbie[0])
    else:
        barbie = 50
else:
    barbie = args.barbie

if type(args.cars) is list:
    if 0 <= int(args.cars[0]) <= 100:
        cars = int(args.cars[0])
    else:
        cars = 50
else:
    cars = args.cars

boy = (100 - barbie + cars + movie) / 3
girl = 100 - boy

print(f"boy: {round(boy)}")
print(f"girl: {round(girl)}")
