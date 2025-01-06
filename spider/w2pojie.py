import requests
from bs4 import BeautifulSoup

def get_52pojie_hot_list():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://www.52pojie.cn/forum.php?mod=guide&view=hot',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'mod': 'guide',
        'view': 'digest',
    }

    try:
        response = requests.get('https://www.52pojie.cn/forum.php', params=params, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        result = []
        
        # 找到所有帖子的标题链接
        for thread in soup.find_all('a', class_='xst'):
            title = thread.text.strip()
            link = thread.get('href')
            if title and link:
                result.append({
                    'title': title,
                    'link': 'https://www.52pojie.cn/' + link
                })
        
        return result[:15]
    except Exception as e:
        print(f"获取吾爱破解热榜失败: {str(e)}")
        return []