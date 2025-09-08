from utils import get_completion

"""
场景: 用普通话表达海盗邮件.
- 需求1: 翻译为普通话, 方便不同文化的人能理解.
- 需求2: 在翻译时我们期望模型采用平和尊重的语气.
- 解决方案要求: 直接调用 llm API
"""

customer_email = """
嗯呐，我现在可是火冒三丈，我那个搅拌机盖子竟然飞了出去，把我厨房的墙壁都溅上了果汁！
更糟糕的是，保修条款可不包括清理我厨房的费用。
伙计，赶紧给我过来！
"""

style="""正式普通话 \
用一个平静, 尊重, 有礼貌的语气
"""

prompt = f"""
请把由三个波浪号包围的邮件翻译为{style}风格的普通话.仅返回翻译后的内容.
邮件内容: ~~~{customer_email}~~~
"""

message = [
    {'role': 'user', 'content': prompt}
]

def output():
    print(get_completion.get_completion(message))