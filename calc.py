def calculator():
    try:
        # 숫자 입력받기
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: "))
        
        # 연산 선택 입력받기
        print("원하는 연산을 선택하세요:")
        print("1. 덧셈 (+)")
        print("2. 뺄셈 (-)")
        print("3. 곱셈 (*)")
        print("4. 나눗셈 (/)")
        operation = input("연산을 입력하세요 (+, -, *, /): ")
        
        # 사칙연산 수행
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "undefined (0으로 나눌 수 없습니다)"
        else:
            print("잘못된 연산자를 입력했습니다.")
            return

        # 결과 출력
        print(f"결과: {result}")
        
    except ValueError:
        print("숫자를 정확히 입력하세요.")

# 계산기 함수 호출
calculator()