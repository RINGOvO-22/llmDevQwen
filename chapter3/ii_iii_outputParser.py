"""
主题: 使用 LangChain 的 output parser 来获得结构化的输出
场景:
- 给定一段描述一个商品的文本(customer review), 从中提取关于其三个方面的信息:
    1. 是否作为礼物
    2. 交货天数
    3. 价格
- 需求: 获得 dict (json) 格式的结构化输出
"""

from langchain_openai import ChatOpenAI
from utils import apiLoader
from langchain.prompts import ChatPromptTemplate

customer_review = """\
这款吹叶机非常神奇。 它有四个设置：\
吹蜡烛、微风、风城、龙卷风。 \
两天后就到了，正好赶上我妻子的\
周年纪念礼物。 \
我想我的妻子会喜欢它到说不出话来。 \
到目前为止，我是唯一一个使用它的人，而且我一直\
每隔一天早上用它来清理草坪上的叶子。 \
它比其他吹叶机稍微贵一点，\
但我认为它的额外功能是值得的。
"""

chat = ChatOpenAI(
        api_key= apiLoader.load_key(),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        model="qwen-plus",  # 此处以qwen-plus为例，您可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        temperature=0.5# other params...
    )

def without_output_parser():
    """不使用 output parser"""

    review_template = """\
    对于以下文本，请从中提取以下信息：

    礼物：该商品是作为礼物送给别人的吗？ \
    如果是，则回答 是的；如果否或未知，则回答 不是。

    交货天数：产品需要多少天\
    到达？ 如果没有找到该信息，则输出-1。

    价钱：提取有关价值或价格的任何句子，\
    并将它们输出为逗号分隔的 Python 列表。

    使用以下键将输出格式化为 JSON：
    礼物
    交货天数
    价钱

    文本: {text}
    """

    prompt_template = ChatPromptTemplate.from_template(review_template)
    print("提示模版：", prompt_template)


    messages = prompt_template.format_messages(text=customer_review)    
    
    response = chat.invoke(messages)

    print("结果类型:", type(response.content))
    print("结果:", response.content)

def with_output_parser():
    """使用了 output parser"""
    
    review_template_2 = """\
    对于以下文本，请从中提取以下信息：：

    礼物：该商品是作为礼物送给别人的吗？
    如果是，则回答 是的；如果否或未知，则回答 不是。

    交货天数：产品到达需要多少天？ 如果没有找到该信息，则输出-1。

    价钱：提取有关价值或价格的任何句子，并将它们输出为逗号分隔的 Python 列表。

    文本: {text}

    {format_instructions}
    """

    prompt = ChatPromptTemplate.from_template(template=review_template_2)

    from langchain.output_parsers import ResponseSchema
    from langchain.output_parsers import StructuredOutputParser

    gift_schema = ResponseSchema(name="礼物",
                                description="这件物品是作为礼物送给别人的吗？\
                                如果是，则回答 是的，\
                                如果否或未知，则回答 不是。")

    delivery_days_schema = ResponseSchema(name="交货天数",
                                        description="产品需要多少天才能到达？\
                                        如果没有找到该信息，则输出-1。")

    price_value_schema = ResponseSchema(name="价钱",
                                        description="提取有关价值或价格的任何句子，\
                                        并将它们输出为逗号分隔的 Python 列表")


    response_schemas = [gift_schema, 
                        delivery_days_schema,
                        price_value_schema]
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    format_instructions = output_parser.get_format_instructions()
    print("输出格式规定：",format_instructions)


    messages = prompt.format_messages(text=customer_review, format_instructions=format_instructions)
    print("第一条客户消息:",messages[0].content)

    response = chat.invoke(messages)

    print("结果类型:", type(response.content))
    print("结果:", response.content)

