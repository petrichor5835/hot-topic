import requests

def get_juejin_hot_list():
    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9', 
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://juejin.cn',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://juejin.cn/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    params = {
        'category_id': '1',
        'type': 'hot',
        'aid': '2608',
        'uuid': '7441127218145871400',
        'spider': '0',
    }

    try:
        response = requests.get(
            'https://api.juejin.cn/content_api/v1/content/article_rank',
            params=params,
            headers=headers,
        )
        
        data = response.json()['data'][:15]
        result = []
        
        for item in data:
            result.append({
                'title': item['content']['title'],
                'id': item['content']['content_id']
            })
            
        return result
        
    except Exception as e:
        print(f"获取掘金热榜失败: {str(e)}")
        return []
