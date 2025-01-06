import requests
import time

def get_bilibili_hot_list():
    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9', 
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.bilibili.com/v/popular/rank/all/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    params = {
        'rid': '0',
        'type': 'all',
        'web_location': '333.934',
        'w_rid': '3711c872d6b9f8d6b66d739acbf3e723',
        'wts': time.time(),
    }

    try:
        response = requests.get('https://api.bilibili.com/x/web-interface/ranking/v2', params=params, headers=headers)
        items = response.json()['data']['list']

        result = []
        for item in items:
            result.append({
                'title': item['title'],
                'link': item['short_link_v2'],
            })
        
        return result[:15]
    except Exception as e:
        print(f"获取B站热榜失败: {str(e)}")
        return []

