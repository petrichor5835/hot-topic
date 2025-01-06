from flask import Flask, jsonify
from flask_cors import CORS
import logging
import time
from spider.weibo import get_weibo_hot_news
from spider.zhihu import get_zhihu_hot_list
from spider.bilibili import get_bilibili_hot_list
from spider.juejin import get_juejin_hot_list
from spider.shaoshupai import get_shaoshupai_hot_list
from spider.douban import get_douban_hot_movies
from spider.maoyan import get_maoyan_movies
from spider.csdn import get_csdn_hot_list
from spider.hgithub import get_hgithub_hot_list
from spider.w2pojie import get_52pojie_hot_list

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
    'bilibili': [],
    'douban': [],
    'maoyan': [],
    'csdn': [],
    'hgithub': [],
    '52pojie': []
}

def fetch_weibo_hot():
    # 这里添加微博热搜爬虫逻辑
    hot_topics = get_weibo_hot_news()   
    return hot_topics


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

def fetch_douban_hot():
    # 这里添加豆瓣热榜爬虫逻辑
    hot_list = get_douban_hot_movies()
    return hot_list

def fetch_maoyan_hot():
    # 这里添加猫眼热榜爬虫逻辑
    hot_list = get_maoyan_movies()
    return hot_list

def fetch_csdn_hot():
    # 这里添加CSDN热榜爬虫逻辑
    hot_list = get_csdn_hot_list()
    return hot_list

def fetch_hgithub_hot():
    # 这里添加HelloGithub热榜爬虫逻辑
    hot_list = get_hgithub_hot_list()
    return hot_list

def fetch_52pojie_hot():
    # 这里添加52破解热榜爬虫逻辑
    hot_list = get_52pojie_hot_list()
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
    elif platform == 'douban':
        news_data[platform] = fetch_douban_hot()
    elif platform == 'maoyan':
        news_data[platform] = fetch_maoyan_hot()
    elif platform == 'csdn':
        news_data[platform] = fetch_csdn_hot()
    elif platform == 'hgithub':
        news_data[platform] = fetch_hgithub_hot()
    elif platform == '52pojie':
        news_data[platform] = fetch_52pojie_hot()
    return jsonify({
        'data': news_data[platform],
        'updateTime': int(time.time())
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True) 