import dashscope
from dashscope import Generation
dashscope.base_http_api_url = 'https://dashscope-intl.aliyuncs.com/api/v1'
dashscope.api_key = 'sk-95a168a9cefd4f2fb5a3c1b7847929fc'
response = Generation.call(
    model='qwen-plus',
    prompt='Explain climate change in simple terms.'
)
print("🤖 Response:")
print(response.output.text)
