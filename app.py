# 从 flask 包中导入 Flask 类（用于创建网站应用）和 render_template 函数（用于渲染 HTML 模板）
from flask import Flask, render_template
# 导入 psutil 库，用于获取 CPU、内存等系统信息
import psutil
# 导入 datetime 模块，用于处理日期和时间
import datetime

# 创建一个 Flask 应用对象，__name__ 帮助 Flask 找到模板和静态文件所在的目录
app = Flask(__name__)

# 定义一个类，把获取系统信息的功能封装在一起，方便后续扩展和维护
class SystemMonitor:
    # 获取 CPU 当前使用率，interval=1 表示取 1 秒内的平均值
    def get_cpu_info(self):
        return psutil.cpu_percent(interval=1)

    # 获取内存使用情况，返回一个包含总量、已用量和百分比的字典
    def get_memory_info(self):
        mem = psutil.virtual_memory()  # 获取虚拟内存详细信息
        return {
            'total': round(mem.total / (1024**3), 1),  # 总内存转换为 GB，保留 1 位小数
            'used': round(mem.used / (1024**3), 1),    # 已用内存转换为 GB
            'percent': mem.percent                     # 已用内存百分比
        }

    # 获取系统已经运行了多长时间，格式为“时:分:秒”，去掉微秒部分
    def get_uptime(self):
        boot = datetime.datetime.fromtimestamp(psutil.boot_time())  # 开机时间点
        now = datetime.datetime.now()                               # 当前时间点
        return str(now - boot).split('.')[0]  # 计算时间差，按 '.' 分割后取前半段，去掉微秒

# 当用户访问网站根路径 '/' 时，执行这个函数
@app.route('/')
def index():
    monitor = SystemMonitor()          # 创建一个监控类的实例
    # 把获取到的数据传给模板 index.html，等号左边的名字就是模板里要使用的变量名
    return render_template('index.html',
                           cpu=monitor.get_cpu_info(),
                           memory=monitor.get_memory_info(),
                           uptime=monitor.get_uptime())

# 如果这个文件是直接被运行的（例如 python app.py），就启动内置的测试服务器
if __name__ == '__main__':
    # host='0.0.0.0' 让局域网内其他设备也能访问，port=5000 指定端口，debug=True 开启调试模式
    app.run(host='0.0.0.0', port=5000, debug=True)