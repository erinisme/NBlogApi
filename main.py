# blog.py 에서 함수 만들어서 모듈 포함시켜서 활용
import blog
print("네이버 맛집 검색")

# 여기에서 메인 프로그램 작성
# 맛집 검색: 여기 맛집 입력 하면 blog 함수로 가서 결과가
print("1. 블로그 검색\n2. 뉴스 검색")
n = input("입력: ")
if n == '1':
    search = input("맛집 검색: ")
    # 결과가 나오는 프로그램 만들기
    blog.nblog(search)
elif n == '2':
    search = input("뉴스 검색: ")
    blog.nnews(search)
else:
    print('잘못입력')