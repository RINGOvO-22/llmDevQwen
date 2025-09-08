from openai import OpenAI
from utils import apiLoader

"""
Qwen api 调用测试
https://help.aliyun.com/zh/model-studio/first-api-call-to-qwen?accounttraceid=d34dff1acd564aacb919e075dead3643zvqd#e4cd73d544i3r
"""

def hello_qwen():
    try:
        client = OpenAI(
            api_key=apiLoader.load_key(),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        )

        completion = client.chat.completions.create(
            model="qwen-plus",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
            messages=[
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': '你是谁？'}
                ]
        )

        print(completion.choices[0].message.content)
        
    except Exception as e:
        print(f"错误信息：{e}")
        print("请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")