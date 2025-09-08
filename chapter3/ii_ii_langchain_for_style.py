"""
场景: 用普通话表达海盗邮件.
- 需求1: 翻译为普通话, 方便不同文化的人能理解.
- 需求2: 在翻译时我们期望模型采用平和尊重的语气.
- 解决方案要求: 不直接调用 llm API, 而是使用 LangChain 框架
"""

from langchain_openai import ChatOpenAI
from utils import apiLoader
from langchain.prompts import ChatPromptTemplate

def helloLangChain():
    """test for LangChain"""
    chat = ChatOpenAI(
        api_key= apiLoader.load_key(),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        model="qwen-plus",  # 此处以qwen-plus为例，您可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        # other params...
    )
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你是谁？"}]
    response = chat.invoke(messages)
    print(chat)
    print("response:", response)

# 1. 构建 ChatOpenAI 对象
chat = ChatOpenAI(
    api_key= apiLoader.load_key(),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus",  # 此处以qwen-plus为例，您可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    temperature=0.5# other params...
)

# 2. 首先，构造一个提示模版字符串：`template_string`.
template_string = """把由三个反引号分隔的文本\
翻译成一种]n{style}风格。\
文本: ```{text}```
"""

# 3. 然后，我们调用`ChatPromptTemplatee.from_template()`函数将
# 上面的提示模版字符`template_string`转换为提示模版`prompt_template`
prompt_template = ChatPromptTemplate.from_template(template_string)
# print("\n", prompt_template.messages[0].prompt) # test

def transform_received_email():
    """将收到的海盗邮件翻译为普通话"""

    # 4. 使用提示模版prompt_template的format_messages方法生成想要的客户消息customer_messages。
    customer_style = """正式普通话 \
    用一个平静、尊敬的语气
    """

    customer_email = """
    嗯呐，我现在可是火冒三丈，我那个搅拌机盖子竟然飞了出去，把我厨房的墙壁都溅上了果汁！
    更糟糕的是，保修条款可不包括清理我厨房的费用。
    伙计，赶紧给我过来！
    """

    # 使用提示模版
    customer_messages = prompt_template.format_messages(
                        style=customer_style,
                        text=customer_email)
    
    # # test
    # # 打印客户消息类型
    # print("客户消息类型:",type(customer_messages),"\n")

    # # 打印第一个客户消息类型
    # print("第一个客户消息的类型:", type(customer_messages[0]),"\n")

    # # 打印第一个元素
    # print("第一个客户消息: ", customer_messages[0],"\n")

    # 5. 最后, 将经过 prompt 模板处理后的客户消息传递给 chat 对象, 获取模型的响应
    customer_response = chat.invoke(customer_messages)
    print("Model response:", customer_response.content)

def transform_sent_email():
    """将要发送的邮件转换为海盗风格"""

    # 6. 将要发送的邮件填入提示词模板
    service_reply = """嘿，顾客， \
    保修不包括厨房的清洁费用， \
    因为您在启动搅拌机之前 \
    忘记盖上盖子而误用搅拌机, \
    这是您的错。 \
    倒霉！ 再见！
    """

    service_style_pirate = """\
    一个有礼貌的语气 \
    使用海盗风格\
    """
    service_messages = prompt_template.format_messages(
        style=service_style_pirate,
        text=service_reply)

    # print("\n", service_messages[0].content) # test

    # 7. 将模板填充后得到的发送邮件传递给 chat 对象, 让它翻译
    service_response = chat.invoke(service_messages)
    print("Model response:", service_response.content)



