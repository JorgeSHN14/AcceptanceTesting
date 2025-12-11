Feature: To-Do List Manager
  As a user
  I want to manage my tasks with priorities and descriptions
  So that I can organize my work efficiently

  # Escenario 1: Añadir tarea (Requisito básico)
  Scenario: Add a task with priority and description
    Given the to-do list is empty
    When the user adds a task "Estudiar Python" with priority "Alta" and description "Repasar clases y objetos"
    Then the to-do list should contain "Estudiar Python"

  # Escenario 2: Listar tareas (Verificando nuevos atributos)
  Scenario: List all tasks showing priority and description
    Given the to-do list contains tasks:
      | Name            | Priority | Description       |
      | Comprar pan     | Baja     | Pan integral      |
      | Pagar internet  | Alta     | Vence hoy         |
    When the user lists all tasks
    Then the output should contain:
      | Name            | Priority | Description       |
      | Comprar pan     | Baja     | Pan integral      |
      | Pagar internet  | Alta     | Vence hoy         |

  # Escenario 3: Marcar tarea como completada
  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Name            | Status  |
      | Lavar ropa      | Pending |
    When the user marks task "Lavar ropa" as completed
    Then the to-do list should show task "Lavar ropa" with status "Completed"

  # Escenario 4: Limpiar la lista
  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Name            |
      | Tarea 1         |
      | Tarea 2         |
    When the user clears the to-do list
    Then the to-do list should be empty

  # Escenario 5: Manejo de errores (El escenario extra requerido por el PDF )
  Scenario: Try to complete a non-existent task
    Given the to-do list is empty
    When the user attempts to mark task "Tarea Fantasma" as completed
    Then the system should display an error message "Error: Tarea 'Tarea Fantasma' no encontrada"