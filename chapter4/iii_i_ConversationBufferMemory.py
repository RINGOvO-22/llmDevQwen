from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from utils import apiLoader

# 1. 初始化对话模型

# 这里将参数temperature设置为0.0，从而减少生成答案的随机性。
# 如果想要每次得到不一样的有新意的答案，可以尝试增大该参数。
llm = ChatOpenAI(
        api_key= apiLoader.load_key(),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        model="qwen-plus",  # 此处以qwen-plus为例，可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        temperature=0.0
    )
memory = ConversationBufferMemory()

# 新建一个 ConversationChain Class 实例
# verbose参数设置为True时，程序会输出更详细的信息，以提供更多的调试或运行时信息。
# 相反，当将verbose参数设置为False时，程序会以更简洁的方式运行，只输出关键的信息。
conversation = ConversationChain(llm=llm, memory = memory, verbose=True)

# 2. 第一轮对话