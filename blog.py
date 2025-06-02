import urllib.request
import json

# 네이버 API 인증 정보 입력
CLIENT_ID = "여기에_클라이언트_ID_입력"
CLIENT_SECRET = "여기에_클라이언트_시크릿_입력"

def naver_search(query, search_type="blog"):
    """
    네이버 검색 API 호출 함수
    :param query: 검색어 문자열
    :param search_type: 검색 타입(blog, news, book 등)
    :return: 검색 결과 리스트 (딕셔너리 형태)
    """
    encoded_query = urllib.parse.quote(query)
    url = f"https://openapi.naver.com/v1/search/{search_type}?query={encoded_query}"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", CLIENT_ID)
    request.add_header("X-Naver-Client-Secret", CLIENT_SECRET)

    try:
        response = urllib.request.urlopen(request)
        rescode = response.getcode()

        if rescode == 200:
            response_body = response.read()
            data = json.loads(response_body.decode('utf-8'))

            results = []
            for item in data.get('items', []):
                result = {
                    "title": item.get("title", ""),
                    "link": item.get("link", ""),
                    "description": item.get("description", ""),
                    "bloggername": item.get("bloggername", ""),
                    "postdate": item.get("postdate", "")
                }
                results.append(result)

            return results
        else:
            print(f"Error Code: {rescode}")
            return []
    except Exception as e:
        print(f"Exception occurred: {e}")
        return []

if __name__ == "__main__":
    search_word = "네이버"
    
    print("[블로그 검색 결과]")
    blog_results = naver_search(search_word, search_type="blog")
    for res in blog_results:
        print(f"제목: {res['title']}")
        print(f"링크: {res['link']}")
        print("-" * 40)

    print("\n[뉴스 검색 결과]")
    news_results = naver_search(search_word, search_type="news")
    for res in news_results:
        print(f"제목: {res['title']}")
        print(f"링크: {res['link']}")
        print("-" * 40)
