def census_project():
    birth = 86400 // 17
    death = 86400 // 12
    arr = 86400 // 87
    det = 86400 // 231
    print(birth , arr , death , det)
    year = int(input(f'년 수를 입력하세요'))
    a = 51761891
    r = a + (birth + arr - death - det) * year
    print(f'{year}년 후의 인구는 {r} 입니다.')


def currency():
    money = int(input('금액을 입력하세요'))
    m = money // 10000
    o = (money % 10000) // 5000
    c = (money % 5000) // 1000
    ob = (money % 1000) // 500
    b = (money % 500) // 100
    s = (money % 100) // 10
    i = (money % 10) // 1
    print(f'입력하신 금액 {money}원은 만원 {m}장, '
          f'오천원 {o}장, '
          f'천원 {c}장, '
          f'오백원 {ob}개, '
          f'백원 {b}개, '
          f'십원 {s}개,'
          f'일원 {i}개 입니다.')


def equation():
    while True:
        a = float(input('a의 값을 입력하세요:'))
        b = float(input('b의 값을 입력하세요:'))
        c = float(input('c의 값을 입력하세요:'))
        D = b * b - 4 * a * c
        if D > 0:
            r = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
            r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
            print(f'실수 해는 {r} 와/과 {r2} 입니다.')
        elif D == 0:
            x = -b / (2 * a)
            print(f'실수 해는 {x} 입니다.')
        elif D < 0:
            print("이 방정식의 실수 해는 존재하지 않습니다.")


if __name__ == '__main__':
    equation()

