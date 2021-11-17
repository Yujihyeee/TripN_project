def CensusProject():
    birth = 86400//17
    death = 86400//12
    arr = 86400//87
    det = 86400//231
    year = input(f'년 수를 입력하세요')
    a = 51761891
    r = int(year) * (birth + arr - death - det) + a
    print(f'{year}년 후의 인구는 {r} 입니다.')

def Currency():
    money = int(input('금액을 입력하세요'))
    count = 0
    money_type = [10000,5000,1000,500,100,50,10,1]
    for i in money_type:
        count += money // i
        money = money % i
    print(f'{money} 은 만원 {money//10000}장, 오천원 {money//5000}장, 천원 {money//1000}장, 오박원 {money//500}개, 백원 {money//100}개, 십원 {money//1}개 입니다.')

def Equation():
    pass


if __name__ == '__main__':
    # CensusProject()
    Currency()
    # Equation()