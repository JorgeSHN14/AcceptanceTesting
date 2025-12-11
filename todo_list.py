import sys

class TodoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, priority="Normal", description="Sin descripción"):
        """
        Requisito: Añadir una nueva tarea[cite: 157].
        Cumple con el requisito de tener mínimo 4 atributos por tarea:
        1. Name, 2. Status, 3. Priority, 4. Description.
        """
        task = {
            "name": name,
            "status": "Pending",
            "priority": priority,
            "description": description
        }
        self.tasks.append(task)
        print(f"Tarea '{name}' añadida exitosamente.")

    def list_tasks(self):
        """Requisito: Listar todas las tareas[cite: 158]."""
        if not self.tasks:
            print("La lista de tareas está vacía.")
            return []
        
        print("\n--- Lista de Tareas ---")
        # Se actualizó el encabezado para mostrar Descripción en lugar de Fecha
        print(f"{'Nombre':<20} | {'Estado':<10} | {'Prioridad':<10} | {'Descripción'}")
        print("-" * 70)
        for task in self.tasks:
            # Se muestra la descripción en la impresión
            print(f"{task['name']:<20} | {task['status']:<10} | {task['priority']:<10} | {task['description']}")
        return self.tasks

    def mark_completed(self, name):
        """Requisito: Marcar una tarea como completada[cite: 159]."""
        for task in self.tasks:
            if task["name"] == name:
                task["status"] = "Completed"
                print(f"Tarea '{name}' marcada como completada.")
                return True
        print(f"Error: Tarea '{name}' no encontrada.")
        return False

    def clear_list(self):
        """Requisito: Limpiar toda la lista[cite: 160]."""
        self.tasks = []
        print("La lista de tareas ha sido vaciada.")

# Bloque para que funcione como aplicación de línea de comandos (CLI)
if __name__ == "__main__":
    manager = TodoListManager()
    
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Añadir tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Limpiar lista")
        print("5. Salir")
        
        choice = input("Selecciona una opción: ")

        if choice == '1':
            name = input("Nombre de la tarea: ")
            prio = input("Prioridad (Baja/Normal/Alta): ")
            # Se solicita descripción en lugar de fecha
            desc = input("Descripción de la tarea: ")
            manager.add_task(name, prio, desc)
        elif choice == '2':
            manager.list_tasks()
        elif choice == '3':
            name = input("Nombre de la tarea a completar: ")
            manager.mark_completed(name)
        elif choice == '4':
            manager.clear_list()
        elif choice == '5':
            print("Saliendo...")
            sys.exit()
        else:
            print("Opción inválida, intenta de nuevo.")