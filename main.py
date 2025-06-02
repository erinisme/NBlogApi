import blog

print("네이버 맛집 검색")

print("1. 블로그 검색\n2. 뉴스 검색")
choice = input("입력: ")

if choice == '1':
    search = input("맛집 검색어 입력: ")
    blog.nblog(search)
elif choice == '2':
    search = input("뉴스 검색어 입력: ")
    blog.nnews(search)
else:
    print("잘못 입력하셨습니다.")
