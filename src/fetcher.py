import httpx
import datetime
from config import BASE_URL, ITEMS_PER_PAGE, PAGES_TO_FETCH


def fetch_top_anime():
    """
    Coleta os top animes mais vistos.
    Retorna uma lista com os dados dos animes.
    """
    top_anime = []
    for page in range(1, PAGES_TO_FETCH + 1):
        url = f"{BASE_URL}/top/anime"
        params = {"page": page, "limit": ITEMS_PER_PAGE}
        response = httpx.get(url, params=params)
        if response.status_code == 200:
            data = response.json().get("data", [])
            top_anime.extend(data)
        else:
            print(f"Erro ao buscar página {page}: {response.status_code}")
    return top_anime


def fetch_top_manga():
    """
    Coleta os top mangás mais vistos.
    Retorna uma lista com os dados dos mangás.
    """
    top_manga = []
    for page in range(1, PAGES_TO_FETCH + 1):
        url = f"{BASE_URL}/top/manga"
        params = {"page": page, "limit": ITEMS_PER_PAGE}
        response = httpx.get(url, params=params)
        if response.status_code == 200:
            data = response.json().get("data", [])
            top_manga.extend(data)
        else:
            print(f"Erro ao buscar página {page}: {response.status_code}")
    return top_manga


def fetch_all_details(item_type, item_id):
    """
    Busca os detalhes completos de um anime ou mangá.
    Parâmetros:
      - item_type: 'anime' ou 'manga'
      - item_id: ID do item
    Retorna os detalhes do item.
    """
    url = f"{BASE_URL}/{item_type}/{item_id}"
    response = httpx.get(url)
    if response.status_code == 200:
        return response.json().get("data", {})
    else:
        print(
            f"Erro ao buscar detalhes para {item_type} {item_id}: {response.status_code}"
        )
        return {}


def fetch_recent_anime():
    """
    Busca animes lançados nos últimos 5 anos.
    Essa função utiliza parâmetros de data para filtrar os resultados.
    Retorna uma lista de animes.
    """
    current_year = datetime.datetime.now().year
    start_year = current_year - 5
    # Exemplo: utilizando o endpoint de busca com parâmetros de data
    url = f"{BASE_URL}/anime"
    params = {
        "start_date": f"{start_year}-01-01",
        "end_date": f"{current_year}-12-31",
        "order_by": "start_date",
        "sort": "desc",
        "limit": ITEMS_PER_PAGE,  # pode ser necessário paginar se houver muitos resultados
    }

    recent_anime = []
    page = 1
    while True:
        params["page"] = page
        response = httpx.get(url, params=params)
        if response.status_code == 200:
            data = response.json().get("data", [])
            if not data:
                break
            recent_anime.extend(data)
            page += 1
        else:
            print(
                f"Erro na busca de animes recentes na página {page}: {response.status_code}"
            )
            break
    return recent_anime
