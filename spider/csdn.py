import requests

def get_csdn_hot_list():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://www.csdn.net/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'page': '0',
        'pageSize': '25',
        'type': '',
    }

    try:
        response = requests.get('https://blog.csdn.net/phoenix/web/blog/hot-rank', params=params, headers=headers)
        items = response.json()['data']

        result = []
        for item in items:
            result.append({
                'title': item['articleTitle'],
                'link': item['articleDetailUrl'],
            })
        
        return result[:15]
    except Exception as e:
        print(f"获取CSDN热榜失败: {str(e)}")
        return []
