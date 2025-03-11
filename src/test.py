import httpx

url = "https://api.jikan.moe/v4/top/anime"

# Testando a requisição antes de implementar no código
# Isso é uma boa prática, pois se houver algum erro, você pode corrigir antes de implementar
try:
    response = httpx.get(url)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())  # Isso vai mostrar a resposta da API
except Exception as e:
    print("Erro ao fazer a requisição:", e)
