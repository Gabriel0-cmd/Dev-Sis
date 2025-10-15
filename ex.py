import requests

def buscar_piada(categoria="Any"):
    url = f"https://v2.jokeapi.dev/joke/{categoria}?format=json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        
        if dados["error"]:
            print("Ocorreu um erro ao buscar a piada.")
            return

        if dados["type"] == "single":
            print(f"\n😂 Piada: {dados['joke']}")
        elif dados["type"] == "twopart":
            print(f"\n❓ Pergunta: {dados['setup']}")
            print(f"😂 Resposta: {dados['delivery']}")
    except requests.RequestException as e:
        print(f"Erro na conexão: {e}")

def menu():
    print("==== Bem-vindo ao sistema de Piadas (JokeAPI) ====")
    print("Categorias disponíveis:")
    print("1 - Programming")
    print("2 - Misc (Diversas)")
    print("3 - Dark")
    print("4 - Pun")
    print("5 - Spooky")
    print("6 - Christmas")
    print("0 - Sair")

    categorias = {
        "1": "Programming",
        "2": "Misc",
        "3": "Dark",
        "4": "Pun",
        "5": "Spooky",
        "6": "Christmas",
    }

    while True:
        escolha = input("\nEscolha uma categoria (0 para sair): ")
        
        if escolha == "0":
            print("Saindo... Até a próxima!")
            break
        elif escolha in categorias:
            categoria = categorias[escolha]
            buscar_piada(categoria)
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
