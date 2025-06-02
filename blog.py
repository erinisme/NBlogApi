import urllib.request
import json

CLIENT_ID = "여기에_클라이언트_ID_입력"
CLIENT_SECRET = "여기에_클라이언트_시크릿_입력"

def nblog(search):
    return _naver_search(search, "blog")

def nnews(search):
    return _naver_search(search, "news")

def _naver_search(query, search_type):
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

            # 결과 출력
            for i, res in enumerate(results, 1):
                print(f"{i}. 제목: {res['title']}")
                print(f"   링크: {res['link']}")
                print("-" * 40)

            return results
        else:
            print(f"Error Code: {rescode}")
            return []
    except Exception as e:
        print(f"Exception occurred: {e}")
        return []
