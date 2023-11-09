from dotenv import dotenv_values

env = dotenv_values()

print(env['OPENAI_API_KEY'])
