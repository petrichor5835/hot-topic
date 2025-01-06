# 热点聚合 (Hot Topic Aggregator)

一个聚合各大平台热点内容的网页应用，提供实时热点新闻的一站式浏览体验。

## 功能特点

- 实时聚合多个平台的热点内容
- 自动定时更新（默认5分钟）
- 支持手动刷新
- 响应式布局设计
- 美观的卡片式界面
- 骨架屏加载动画
- 平滑的过渡效果

## 支持平台

- 微博热搜
- 知乎热榜
- B站热榜
- 掘金热榜
- 少数派热榜
- 豆瓣新片榜
- 猫眼热榜
- CSDN热榜
- HelloGithub热榜
- 吾爱破解热帖

## 技术栈

### 前端
- HTML5
- CSS3
- JavaScript (原生)

### 后端
- Python
- Flask
- Flask-CORS

## 快速开始

1. 克隆项目
```bash
git clone https://github.com/your-username/hot-topic.git
cd hot-topic
```

2. 安装依赖
```bash
pip install flask flask-cors requests beautifulsoup4
```

3. 运行后端服务
```bash
python app.py
```

4. 在浏览器中打开 `index.html` 即可访问

## 项目结构

```
hot-topic/
├── app.py              # 后端主程序
├── index.html          # 前端页面
├── styles.css          # 样式文件
├── script.js           # 前端逻辑
├── spider/            # 爬虫模块
│   ├── weibo.py
│   ├── zhihu.py
│   └── ...
└── images/           # 图标资源
    ├── flame.png
    ├── weibo-icon.png
    └── ...
```

## 开发说明

- 后端服务默认运行在 `http://127.0.0.1:5000`
- 所有API返回数据格式统一为：
```json
{
    "data": [...],
    "updateTime": 1234567890
}
```

## 注意事项

- 本项目仅供学习交流使用
- 请遵守相关平台的使用规范
- 建议适当调整数据更新频率，避免对目标网站造成压力

## License

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request

