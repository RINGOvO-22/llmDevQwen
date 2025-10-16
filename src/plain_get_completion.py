import os
from openai import OpenAI
from utils import apiLoader

def get_completion(messages:list, model:str="qwen-plus", temperature: float=0.5):
    """
    单轮对话
    messages: list 消息列表
    model: str 模型名称
    return: str 模型回复
    """
    try:
        client = OpenAI(
            # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
            api_key=apiLoader.load_key(),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        )

        completion = client.chat.completions.create(
            # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
            model=model,
            messages=messages,
            temperature=temperature,
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"错误信息：{e}")
        print("请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")