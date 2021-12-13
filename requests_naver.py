import urllib
import urllib.parse, urllib.request
import json

def requests_naver(enc_text, type="webkr"):
    encText = urllib.parse.quote(enc_text)
    url = f"https://openapi.naver.com/v1/search/{type}?query=" + encText

    client_id = "aBtzUhN3jBckA0jDPVbV"
    client_secret = "ZBR7EN05g_"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)

    rescode = response.getcode()
    if rescode==200:
        response_body = response.read()
        return json.loads(response_body.decode('utf-8'))['items']
    else:
        return "Error Code:" + rescode


if __name__ == '__main__':
    results = requests_naver("naver")
    for result in results:
        print(result['title'])
        print(result['link'])
        print(result['description'])
