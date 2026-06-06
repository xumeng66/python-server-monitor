# 服务器监控面板

一个用 Python Flask 编写的轻量级服务器实时监控 Web 面板。

## 功能
- 实时显示 CPU 使用率
- 显示内存使用量（已用 / 总量）
- 显示系统运行时间

## 技术栈
- Python 3
- Flask（Web 框架）
- psutil（系统信息采集）
- Jinja2（模板渲染）

## 快速启动

# 安装依赖
pip install -r requirements.txt

# 运行应用
python app.py

浏览器访问 http://127.0.0.1:5000 即可查看监控面板。

## 项目结构
python-server-monitor/
├── app.py              # Flask 主程序，包含 SystemMonitor 类
├── requirements.txt    # 项目依赖清单
├── templates/
│   └── index.html      # 前端模板（Jinja2）
└── README.md

## 作者
xumeng66