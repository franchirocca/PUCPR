class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = {'Descricao': description, 'completada': False}
        self.tasks.append(task)
        print(f"Tarefa adicionada: {description}")

    def list_tasks(self):
        if not self.tasks:
            print("Sem tarefas para mostrar.")
        for i, task in enumerate(self.tasks):
            status = "Completada" if task['completada'] else "Pendente"
            print(f"{i + 1}. {task['Descricao']} - {status}")

    def complete_task(self, index):
        if 0 <= index - 1 < len(self.tasks):
            self.tasks[index - 1]['completada'] = True
            print(f"Tarefa {index} marcada como completada!")
        else:
            print("Numero de tarefa invalido.")

def main():
    todo_list = TodoList()
    while True:
        print("\n1. Adicionar tarefa")
        print("2. Lista de tarefas")
        print("3. Completar alguma tarefa")
        print("4. Sair")
        choice = input("Escolha uma opcao: ")

        if choice == '1':
            task_description = input("Descrava a terafa: ")
            todo_list.add_task(task_description)
        elif choice == '2':
            todo_list.list_tasks()
        elif choice == '3':
            task_number = int(input("Insira uma tarefa para completar: "))
            todo_list.complete_task(task_number)
        elif choice == '4':
            print("Tchau!")
            break
        else:
            print("Opcao invalida, teste novamente")

if __name__ == "__main__":
    main()
