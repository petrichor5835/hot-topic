import requests

def get_maoyan_movies():
    # 使用移动端API接口
    url = "https://i.maoyan.com/api/mmdb/movie/v3/list/hot.json"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
        'Accept': 'application/json',
        'Referer': 'https://i.maoyan.com/'
    }
    
    params = {
        'ct': '浙江',
        'ci': 30,
        'channelId': 4
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        
        movies = []
        for item in data.get('data', {}).get('hot', []):
            movie = {
                'title': item.get('nm', ''),
                'link': f"https://www.maoyan.com/films/{item.get('id')}",
                'rating': item.get('sc', '暂无评分')
            }
            movies.append(movie)
            
        return movies
        
    except Exception as e:
        print(f"获取猫眼热门电影失败: {str(e)}")
        return []

if __name__ == "__main__":
    movies = get_maoyan_movies()
    for movie in movies:
        print(f"电影: {movie['title']}")
        print(f"链接: {movie['link']}")
        print(f"评分: {movie['rating']}")
        print("-" * 50)
