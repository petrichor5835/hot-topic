import requests
import time

def get_shaoshupai_hot_list():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://sspai.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'limit': '15',
        'offset': '0',
        'created_at': str(int(time.time())),
        'tag': '热门文章',
        'released': 'false',
    }

    response = requests.get('https://sspai.com/api/v1/article/tag/page/get', params=params, headers=headers)
    lists = response.json()['data']
    hot_list = []
    for item in lists:
        hot_list.append({
            'title': item['title'],
            'link': f'https://sspai.com/post/{item["id"]}'
        })
    return hot_list
