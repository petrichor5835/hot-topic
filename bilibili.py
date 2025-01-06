import requests

def get_bilibili_hot_list():
    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'origin': 'https://www.bilibili.com',
        'referer': 'https://www.bilibili.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    params = {
        'limit': '15',
        'platform': 'web',
        'web_location': '333.1007',
    }

    try:
        response = requests.get(
            'https://api.bilibili.com/x/web-interface/wbi/search/square',
            params=params,
            headers=headers,
        )
        
        data = response.json()
        if data['code'] != 0:
            return []
            
        hot_list = data['data']['trending']['list']
        result = []
        
        for item in hot_list:
            result.append({
                'title': item['keyword'],
                'id': ''  # B站热搜没有直接的视频ID，所以这里留空
            })
            
        return result
        
    except Exception as e:
        print(f"获取B站热搜失败: {str(e)}")
        return []


