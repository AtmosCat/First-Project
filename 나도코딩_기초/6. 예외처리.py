# try : 
#     print("나누기 전용 계산기")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요")))
#     nums.append(int(input("두 번째 숫자를 입력하세요")))
#     # nums.append(nums[0] / nums[1])
#     print("{} / {} = {}".format(nums[0], nums[1], nums[2]))
# except ValueError:               # 숫자가 아닌 문자열로 나누는 값을 입력한 경우 -> 발생한 에러 중 except에 해당하는 ValueError가 있는 경우 밑의 명령을 수행하고 다시 실행함
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:    # 0으로 나누는 경우 / 에러 내용을 문장으로 그대로 출력
#     print(err)
# # except:  # 나머지 모든 에러에 대한 메시지 출력
# #     print("알 수 없는 오류가 발생했습니다.")
# except Exception as err:
#     print("알 수 없는 오류가 발생했습니다.")
#     print(err)   # 각 오류의 오류 메시지 출력


# # 에러 발생시키기 & # 사용자 정의 예외처리 : 에러 정의하기

# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
    
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기")
#     num1 = int(input("첫 번째 숫자를 입력하세요:"))
#     num2 = int(input("두 번째 숫자를 입력하세요:"))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {}, {}".format(num1, num2))   # 에러 만들기
#     print("{} / {} = {}".format(num1 ,num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
# except BigNumberError as err:
#     print("에러! 한 자리 숫자만 입력 가능합니다")
#     print(err)
# # finally 정상 구문이든 에러 구문이든 무조건 실행되는 구문
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")


# 퀴즈
# 동네에 항상 대기 손님이 있는 치킨집이 있다. 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 만들었다. 
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오
# 조건 1 : 1보다 작거나 숫자가 아닌 입력값이 들어오는 경우 ValueError로 처리
# 조건 2 : 대기 손님이 주문할 수 있는 치킨은 최대 10마리로 한정. 치킨 소진 시 사용자 정의 에러(SoldOutError)를 발생시키고 프로그램 종료 / 출력 메시지 : "재고가 소진되었습니다"

chicken = 10
waiting = 1 # 홀 만석, 대기 1부터 시작

class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    
    while True:
        print("남은 치킨 : {}".format(chicken))
        order = int(input("치킨 몇 마리를 주문하시겠습니까? :"))
        if order < 1:
            raise ValueError
        if order > chicken : 
            print("재료가 부족합니다")
        else:
            print("[대기번호 {}] {}마리 주문이 완료되었습니다".format(waiting, order))
            waiting += 1
            chicken -= order
        if chicken <= 0 :
            raise SoldOutError("남은 닭 : {}마리".format(chicken))
            break

except ValueError:
    print("잘못된 값을 입력하였습니다.")

except SoldOutError as err:
    print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
    print(err)

except Exception as errr:
    print("알 수 없는 에러가 발생하였습니다.")
    print(errr)









