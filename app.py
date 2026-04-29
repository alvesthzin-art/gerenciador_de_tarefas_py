import json
import os

def carregar_tarefas():
    if os.path.exists("tarefas.json"):
        with open("tarefas.json", "r") as arquivo:
            return json.load(arquivo)
    return []

def salvar_tarefas(tarefas):
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo, indent=4)

def adicionar_tarefa(tarefas):
    nome = input("Digite a tarefa: ")
    tarefas.append({"tarefa": nome, "concluida": False})
    print("✅ Tarefa adicionada!")

def listar_tarefas(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return
    
    print("\n--- SUAS TAREFAS ---")
    for i, t in enumerate(tarefas):
        status = "✔" if t["concluida"] else " "
        print(f"{i + 1}. [{status}] {t['tarefa']}")

def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("\nDigite o número da tarefa concluída: ")) - 1
        tarefas[indice]["concluida"] = True
        print("🎉 Parabéns por concluir a tarefa!")
    except (ValueError, IndexError):
        print("❌ Opção inválida.")

def menu():
    tarefas = carregar_tarefas()
    
    while True:
        print("\n1. Adicionar Tarefa\n2. Listar Tarefas\n3. Concluir Tarefa\n4. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            salvar_tarefas(tarefas)
            print("Dados salvos. Até mais!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
