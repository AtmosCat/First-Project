class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만 원")

if __name__ == "__main__":           # thailand.py 에서 바로 실행할 경우에 이 구문이 실행
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때에만 직접 실행됨")
    trip_to = ThailandPackage()
    trip_to.detail()
else:                                # 외부.py에서 불러올 때에는 이 구문 실행
    print("Thailand 외부에서 모듈 호출")










