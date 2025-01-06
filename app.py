from flask import Flask, jsonify
from flask_cors import CORS
import logging
import time
from weibo import get_weibo_hot_news
from zhihu import get_zhihu_hot_list
from bilibili import get_bilibili_hot_list
from juejin import get_juejin_hot_list
from shaoshupai import get_shaoshupai_hot_list
app = Flask(__name__)
CORS(app)  # 启用跨域请求

# 配置日志
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 模拟数据存储
news_data = {
    'weibo': [],
    'zhihu': [],
    'toutiao': [],
    'bilibili': []
}

def fetch_weibo_hot():
    # 这里添加微博热搜爬虫逻辑
    hot_topics = get_weibo_hot_news()
    # 将hot_topics转换为列表
    hot_topics_list = [{"title": topic['topic'], "rank": i} for i, topic in enumerate(hot_topics, 1)]
    return hot_topics_list


def fetch_zhihu_hot():
    # 这里添加知乎热榜爬虫逻辑
    hot_list = get_zhihu_hot_list()
    return hot_list

def fetch_bilibili_hot():
    # 这里添加B站热榜爬虫逻辑
    hot_list = get_bilibili_hot_list()
    return hot_list

def fetch_juejin_hot():
    # 这里添加掘金热榜爬虫逻辑
    hot_list = get_juejin_hot_list()
    return hot_list

def fetch_shaoshupai_hot():
    # 这里添加少少派热榜爬虫逻辑
    hot_list = get_shaoshupai_hot_list()
    return hot_list

@app.route('/api/<platform>/hot-news')
def get_hot_news(platform):
    if platform == 'weibo':
        news_data[platform] = fetch_weibo_hot()
    elif platform == 'zhihu':
        news_data[platform] = fetch_zhihu_hot()
    elif platform == 'bilibili':
        news_data[platform] = fetch_bilibili_hot()
    elif platform == 'juejin':
        news_data[platform] = fetch_juejin_hot()
    elif platform == 'shaoshupai':
        news_data[platform] = fetch_shaoshupai_hot()
    return jsonify({
        'data': news_data[platform],
        'updateTime': int(time.time())
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 