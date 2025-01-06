import requests
import json
from urllib.parse import quote

def get_xsrf_token():
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9', 
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate', 
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    session = requests.Session()  # 使用session来保持cookie

    # 第一次请求，获取访客系统的cookie
    response = session.get('https://weibo.com/hot/news', headers=headers)
    return session.cookies.get('XSRF-TOKEN')

def get_sub():

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://passport.weibo.com/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    params = {
        'a': 'crossdomain',
        's': '_2AkMQMj9df8NxqwFRmf4dzWrgZY1-yw7EieKmbs6GJRMxHRl-yT8XqmpdtRB6O7IRsmJ6NtWQHdDS7hS_PXkIBzjQHK8d',
        'sp': '0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWAiCSNwS_pd-2-5ubPok7q',
        'from': 'weibo',
        '_rand': '0.1188860583023208',
        'entry': 'miniblog',
        'url': 'https://weibo.com/hot/news',
    }
    session = requests.Session()
    response = session.get('https://login.sina.com.cn/visitor/visitor', params=params, headers=headers)
    SUB = session.cookies.get('SUB')
    SUBP = session.cookies.get('SUBP')
    return SUB, SUBP

def get_wbpass(xsrf_token, SUB, SUBP):
    cookies = {
        'SUB': SUB,
        'SUBP': SUBP,
        'XSRF-TOKEN': xsrf_token,
    }
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://passport.weibo.com/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }
    session = requests.Session()
    response = session.get('https://weibo.com/hot/news', cookies=cookies, headers=headers)
    return session.cookies.get('WBPSESS')

def get_news(cookies):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'client-version': 'v2.47.15', 
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://weibo.com/hot/news',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'server-version': 'v2024.12.27.1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': cookies.get('XSRF-TOKEN'),
    }

    response = requests.get('https://weibo.com/ajax/statuses/news', cookies=cookies, headers=headers)
    return response.text

def get_weibo_hot_news():
    """
    获取微博热搜新闻数据的主方法
    Args:
        limit: 需要返回的热搜话题数量，默认15条
    Returns:
        list: 包含热搜话题的列表
    """
    # 获取必要的认证token和cookie
    xsrf_token = get_xsrf_token()
    SUB, SUBP = get_sub()
    wbpass = get_wbpass(xsrf_token, SUB, SUBP)
    
    # 组装cookies
    cookies = {
        'XSRF-TOKEN': xsrf_token,
        'SUB': SUB,
        'SUBP': SUBP,
        'WBPSESS': wbpass,
    }
    
    # 获取新闻数据并解析
    response_data = json.loads(get_news(cookies))
    result = []
    for item in response_data['data']['band_list']:
        title = item['topic']
        link = f'https://s.weibo.com/weibo?q=%23{quote(title)}%23'
        result.append({
            'title': title,
            'link': link
        })
    return result

if __name__ == '__main__':
    get_weibo_hot_news()




