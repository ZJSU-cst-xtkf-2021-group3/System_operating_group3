#年龄段转换
    # 0-13 -> 1
    # 14-17 -> 2
    # 18-25 -> 3
    # 26-35 -> 4
    # 36-45 -> 5
    # 46-56 -> 6
    # >57 -> 7


def ageSwitch(age):
    if age>=0 and age<=13:
        return 1
    if age>=14 and age<=17:
        return 2
    if age>=18 and age<=25:
        return 3
    if age >= 26 and age <= 35:
        return 4
    if age >= 36 and age <= 45:
        return 5
    if age >= 46 and age <= 56:
        return 6
    if age>=57:
        return 7

if __name__=='__main__':
    a=int(input('age: '))
    print(ageSwitch(a))