def census_project():
    birth = 86400//17
    death = 86400//12
    arr = 86400//87
    det = 86400//231
    year = input(f'년 수를 입력하세요')
    a = 51761891
    r = int(year) * (birth + arr - death - det) + a
    print(f'{year}년 후의 인구는 {r} 입니다.')


def currency():
    money = int(input('금액을 입력하세요'))
    money_type = [10000, 5000, 1000, 500, 100, 50, 10, 1]


    print(f'{n} 은 만원 {m}장, '
          f'오천원 {o}장, '
          f'천원 {c}장, '
          f'오백원 {ob}개, '
          f'백원 {b}개, '
          f'십원 {s}개,'
          f'일원 {i}개 입니다.')


def equation():
    pass


if __name__ == '__main__':
    # census_project()
    currency()
    # equation()