import requests

def get_hgithub_hot_list():
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9', 
        'Authorization': 'Bearer null',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://hellogithub.com',
        'Pragma': 'no-cache',
        'Referer': 'https://hellogithub.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'sort_by': 'featured',
        'page': '1',
        'rank_by': 'newest',
        'tid': 'all',
    }

    try:
        response = requests.get('https://api.hellogithub.com/v1/', params=params, headers=headers)
        items = response.json()['data']
        
        result = []
        for item in items:
            result.append({
                'title': item['title'],
                'link': 'https://hellogithub.com/repository/' + item['item_id']
            })
            
        return result[:15]
    except Exception as e:
        print(f"获取HelloGithub热榜失败: {str(e)}")
        return []
