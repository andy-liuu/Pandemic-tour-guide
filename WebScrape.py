import requests

result = requests.get("https://blog.wego.com/saudi-arabia-travel-restrictions-and-quarantine-requirements/")
print(result.status_code)

src = result.content
lines = src.splitlines()
print(lines[20])
