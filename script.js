class NewsCard {
    constructor(platform, icon, container) {
        this.platform = platform;
        this.icon = icon;
        this.data = [];
        this.container = container;
        this.updateInterval = 300000; // 5分钟更新一次
        this.init();
    }

    init() {
        // 创建卡片DOM结构
        this.cardElement = document.createElement('div');
        this.cardElement.className = 'news-card';
        this.cardElement.innerHTML = `
            <div class="card-header">
                <img src="${this.icon}" alt="${this.platform}">
                <h3>${this.getPlatformName()}</h3>
                <span class="refresh-time">刚刚更新</span>
                <button class="refresh-btn" title="刷新">↻</button>
            </div>
            <ul class="news-list">
                <li class="loading">加载中...</li>
            </ul>
        `;
        this.container.appendChild(this.cardElement);
        
        // 添加刷新按钮的点击事件监听
        const refreshBtn = this.cardElement.querySelector('.refresh-btn');
        refreshBtn.addEventListener('click', () => this.fetchData());
        
        // 开始定时获取数据
        this.fetchData();
        setInterval(() => this.fetchData(), this.updateInterval);
    }

    getPlatformName() {
        const names = {
            'weibo': '微博热搜',
            'zhihu': '知乎热榜',
            'bilibili': 'B站热榜',
            'juejin': '掘金热榜',
            'shaoshupai': '少数派热榜',
            'douban': '豆瓣新片榜',
            'maoyan': '猫眼热榜',
            'csdn': 'CSDN热榜',
            'hgithub': 'HelloGithub',
            '52pojie': '吾爱破解'
        };
        return names[this.platform] || this.platform;
    }

    showLoading() {
        const newsList = this.cardElement.querySelector('.news-list');
        // 创建10个骨架项
        const skeletonItems = Array(10).fill(0).map(() => `
            <li class="skeleton-item">
                <div class="skeleton-rank"></div>
                <div class="skeleton-title"></div>
            </li>
        `).join('');
        
        newsList.innerHTML = skeletonItems;
    }

    async fetchData() {
        const newsList = this.cardElement.querySelector('.news-list');
        
        // 添加淡出效果
        newsList.classList.add('fade-out');
        
        // 等待淡出动画完成
        await new Promise(resolve => setTimeout(resolve, 300));
        
        // 显示骨架屏
        this.showLoading();
        newsList.classList.remove('fade-out');
        
        try {
            const response = await fetch(`http://127.0.0.1:5000/api/${this.platform}/hot-news`);
            const result = await response.json();
            this.data = result.data;
            this.updateTime = result.updateTime;
            
            // 添加淡出效果
            newsList.classList.add('fade-out');
            await new Promise(resolve => setTimeout(resolve, 300));
            
            // 渲染新内容
            this.render();
            
            // 添加淡入效果
            newsList.classList.remove('fade-out');
            newsList.classList.add('fade-in');
            
            // 动画结束后移除动画类
            setTimeout(() => {
                newsList.classList.remove('fade-in');
            }, 300);
            
        } catch (error) {
            console.error('获取数据失败:', error);
            this.showError();
        }
    }

    showError() {
        const newsList = this.cardElement.querySelector('.news-list');
        newsList.innerHTML = '<li class="error">获取数据失败，请稍后再试</li>';
        
        // 错误信息也使用淡入效果
        newsList.classList.remove('fade-out');
        newsList.classList.add('fade-in');
        
        setTimeout(() => {
            newsList.classList.remove('fade-in');
        }, 300);
    }


    render() {
        const newsList = this.cardElement.querySelector('.news-list');
        newsList.innerHTML = this.data.map((item, index) => `
            <li class="news-item">
                <span class="rank ${index < 3 ? 'top' : ''}">${index + 1}</span>
                <div class="title-container">
                    <a href="${item.link}" 
                       class="title" 
                       target="_blank">${item.title}</a>
                </div>
                ${item.rating ? `<span class="rating">${item.rating}</span>` : ''}
            </li>
        `).join('');
        
        // 更新时间显示
        const timeElement = this.cardElement.querySelector('.refresh-time');
        timeElement.textContent = this.getUpdateTimeText();
    }

    getUpdateTimeText() {
        const now = Math.floor(Date.now() / 1000);
        const diff = now - this.updateTime;
        if (diff < 60) return '刚刚更新';
        if (diff < 3600) return `${Math.floor(diff / 60)}分钟前更新`;
        return `${Math.floor(diff / 3600)}小时前更新`;
    }
}

// 初始化
document.addEventListener('DOMContentLoaded', () => {
    const container = document.querySelector('.news-grid');
    const platforms = [
        { name: 'weibo', icon: './images/weibo-icon.png' },
        { name: 'zhihu', icon: './images/zhihu-icon.png' },
        { name: 'bilibili', icon: './images/bilibili-icon.png' },
        { name: 'juejin', icon: './images/juejin-icon.png' },
        { name: 'shaoshupai', icon: './images/shaoshupai-icon.png' },
        { name: 'douban', icon: './images/douban-icon.png' },
        { name: 'maoyan', icon: './images/maoyan-icon.png' },
        { name: 'csdn', icon: './images/csdn-icon.png' },
        { name: 'hgithub', icon: './images/hellogithub-icon.png' },
        { name: '52pojie', icon: './images/52pojie-icon.png' }
    ];

    platforms.forEach(platform => {
        new NewsCard(platform.name, platform.icon, container);
    });
}); 