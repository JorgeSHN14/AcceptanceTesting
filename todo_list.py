import sys

class TodoListManager:
    def __init__(self):
        self.tasks = []
        self._id_counter = 1

    def add_task(self, name):
        """
        Requisito: Añadir tarea.
        Atributos (Mínimo 4 ): 
        1. id, 2. name, 3. status.
        """
        task = {
            "id": self._id_counter,
            "name": name,
            "status": "Pending"
        }
        self.tasks.append(task)
        self._id_counter += 1
        print(f"Tarea '{name}' añadida exitosamente.")

    def list_tasks(self):
        """Requisito: Listar tareas."""
        if not self.tasks:
            print("La lista de tareas está vacía.")
            return []
        
        print("\n--- Lista de Tareas ---")
        # Formato limpio mostrando ID, Nombre, Estado 
        print(f"{'ID':<3} | {'Nombre':<20} | {'Estado':<10}")
        print("-" * 60)
        for task in self.tasks:
            print(f"{task['id']:<3} | {task['name']:<20} | {task['status']:<10}")
        return self.tasks

    def mark_completed(self, name):
        """Requisito: Marcar como completada."""
        for task in self.tasks:
            if task["name"] == name:
                task["status"] = "Completed"
                print(f"Tarea '{name}' marcada como completada.")
                return True
        print(f"Error: Tarea '{name}' no encontrada.")
        return False

    def clear_list(self):
        """Requisito: Limpiar lista."""
        self.tasks = []
        print("La lista de tareas ha sido vaciada.")

    def edit_task(self, original_name, new_name):
        """
        Requisito EXTRA (5ta funcionalidad): Editar una tarea existente.
        Permite cambiar el nombre
        """
        for task in self.tasks:
            if task["name"] == original_name:
                task["name"] = new_name
                print(f"Tarea actualizada exitosamente a: '{new_name}'")
                return True
        print(f"Error: No se pudo editar. Tarea '{original_name}' no encontrada.")
        return False

# Bloque principal para ejecución en consola (CLI)
if __name__ == "__main__":
    manager = TodoListManager()
    
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Añadir tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Editar tarea (NUEVO)")
        print("5. Limpiar lista")
        print("6. Salir")
        
        choice = input("Selecciona una opción: ")

        if choice == '1':
            name = input("Nombre de la tarea: ")
            manager.add_task(name)
        elif choice == '2':
            manager.list_tasks()
        elif choice == '3':
            name = input("Nombre de la tarea a completar: ")
            manager.mark_completed(name)
        elif choice == '4':
            orig_name = input("Nombre de la tarea a editar: ")
            new_name = input("Nuevo nombre: ")
            manager.edit_task(orig_name, new_name)
        elif choice == '5':
            manager.clear_list()
        elif choice == '6':
            print("Saliendo...")
            sys.exit()
        else:
            print("Opción inválida, intenta de nuevo.")