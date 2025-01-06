import requests
from bs4 import BeautifulSoup
import json

def get_zhihu_hot_list():
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://www.google.com/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }
    
    try:
        response = requests.get('https://www.zhihu.com/billboard', headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        script = soup.find('script', id='js-initialData')
        
        if not script:
            return []
            
        json_data = json.loads(script.string)
        hot_list = json_data['initialState']['topstory']['hotList']
        
        result = []
        for item in hot_list:
            target = item['target']
            title = target['titleArea']['text']
            card_id = item.get('cardId', '')
            id = card_id.split('_')[1] if card_id else ''
            
            result.append({
                'title': title,
                'link': f'https://www.zhihu.com/question/{id}'
            })
        #返回前15个
        return result[:15]
        
    except Exception as e:
        print(f"获取知乎热榜失败: {str(e)}")
        return []

