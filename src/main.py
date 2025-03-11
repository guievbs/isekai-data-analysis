import json
import os
from fetcher import (
    fetch_top_anime,
    fetch_top_manga,
    fetch_recent_anime,
    fetch_all_details,
)


def save_data(data, filename):
    """
    Salva os dados em um arquivo JSON na pasta 'data'.
    """
    os.makedirs("data", exist_ok=True)
    with open(os.path.join("data/raw", filename), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Dados salvos em data/raw/{filename}")


def main():
    # Coleta dos top 500 animes
    print("Coletando top animes...")
    top_anime = fetch_top_anime()
    save_data(top_anime, "top_anime.json")

    # Coleta dos top 500 mangás
    print("Coletando top mangás...")
    top_manga = fetch_top_manga()
    save_data(top_manga, "top_manga.json")

    # Coleta dos animes dos últimos 5 anos
    print("Coletando animes recentes...")
    recent_anime = fetch_recent_anime()
    save_data(recent_anime, "recent_anime.json")

    # Buscar detalhes completos de um anime específico (id exemplo: 1)
    print("Buscando detalhes do anime com id 1...")
    details = fetch_all_details("anime", 1)
    save_data(details, "anime_1_details.json")


if __name__ == "__main__":
    main()
