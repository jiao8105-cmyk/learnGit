from dotenv import load_dotenv
import os
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_deepseek import ChatDeepSeek

load_dotenv()

api_key = os.getenv("Ali_api_key", "sk-45974c1519d04cffa918d8f942e7627e")
base_url = os.getenv("Ali_Base_url","https://dashscope.aliyuncs.com/compatible-mode/v1")


# client = OpenAI(
#     # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
#     api_key=api_key,
#     base_url=base_url,
# )
# completion = client.chat.completions.create(
#     model="qwen3-max",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "你是谁？"},
#     ],
#     stream=True
# )
# for chunk in completion:
#     print(chunk.choices[0].delta.content, end="", flush=True)
# model = ChatOpenAI(
#     model="qwen3-max",
#     api_key=api_key,
#     base_url=base_url,
# )
# completion = model.invoke("你是谁？")
# print(completion)


llm = ChatDeepSeek(
    model="deepseek-v3.2-exp",
    api_key=api_key,
    api_base=base_url,
    temperature=0.5,
)
completion = llm.invoke("你是谁？")
print(completion)
