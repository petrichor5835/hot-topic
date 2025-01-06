import requests
from bs4 import BeautifulSoup

def get_douban_hot_movies():
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
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    try:
        response = requests.get('https://movie.douban.com/chart', headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 找到所有电影条目
        movies = soup.select('.item')
        result = []

        for movie in movies:
            # 获取标题
            title = movie.select_one('.pl2 a').text.strip().split('\n')[0]
            
            # 获取链接
            link = movie.select_one('.pl2 a')['href']
            
            # 获取评分 (如果有的话)
            rating = movie.select_one('.rating_nums')
            rating = rating.text if rating else '暂无评分'

            result.append({
                'title': title,
                'link': link,
                'rating': rating
            })

        return result
        
    except Exception as e:
        print(f"获取豆瓣热门电影失败: {str(e)}")
        return []

if __name__ == '__main__':
    print(get_douban_hot_movies())
