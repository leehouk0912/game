import mod1

#두 숫자를 입력받게 만들고
#메뉴 1.더하기 2.빼기
#1을 누르면 두 수의 더한 결과값
#2를 누르면 두 수를 뺀 결과값
#출력시키기.

print('두개의 숫자를 넣으시고 번호를 선택하세요')
num1 = int(input('num1 : '))
num2 = int(input('num2 : '))
print('1.더하기 2.뺴기')
number = input('선택 : ')
if number == '1':
    result = mod1.add(num1,num2)
    print(result)
elif number == '2':
    result = mod1.sub(num1,num2)
    print(result)