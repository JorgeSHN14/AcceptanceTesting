from behave import given, when, then
from todo_list import TodoListManager
import sys
from io import StringIO

# --- GIVEN STEPS ---

@given('the to-do list is empty')
def step_impl(context):
    # Inicializamos una nueva instancia del manager para cada escenario
    context.manager = TodoListManager()

@given('the to-do list contains tasks:')
def step_impl(context):
    context.manager = TodoListManager()
    # Iteramos sobre la tabla definida en el archivo .feature
    for row in context.table:
        # Extraemos los valores. Si no existen en la tabla, usamos valores por defecto.
        name = row['Name']
        priority = row.get('Priority', 'Normal') 
        description = row.get('Description', 'Sin descripción')
        status = row.get('Status', 'Pending')
        
        # Añadimos la tarea usando la lógica del programa
        context.manager.add_task(name, priority, description)
        
        # Si el escenario requiere que la tarea esté "Completed", forzamos el estado
        if status == 'Completed':
            context.manager.mark_completed(name)

# --- WHEN STEPS ---

@when('the user adds a task "{name}" with priority "{priority}" and description "{description}"')
def step_impl(context, name, priority, description):
    context.manager.add_task(name, priority, description)

@when('the user lists all tasks')
def step_impl(context):
    # Llamamos al método y guardamos el retorno para verificarlo después
    context.list_result = context.manager.list_tasks()

@when('the user marks task "{name}" as completed')
def step_impl(context, name):
    context.manager.mark_completed(name)

@when('the user clears the to-do list')
def step_impl(context):
    context.manager.clear_list()

@when('the user attempts to mark task "{name}" as completed')
def step_impl(context, name):
    # TRUCO PRO: Como tu programa usa 'print' para mostrar errores, 
    # necesitamos capturar la consola (stdout) para leer ese mensaje.
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Ejecutamos la acción
    context.manager.mark_completed(name)
    
    # Restauramos la consola normal y guardamos lo que se imprimió
    sys.stdout = sys.__stdout__
    context.printed_output = captured_output.getvalue().strip()

# --- THEN STEPS ---

@then('the to-do list should contain "{name}"')
def step_impl(context, name):
    # Verificamos si el nombre existe en alguna de las tareas actuales
    found = False
    for task in context.manager.tasks:
        if task['name'] == name:
            found = True
            break
    assert found, f'La tarea "{name}" no fue encontrada en la lista.'

@then('the output should contain:')
def step_impl(context):
    # Verificamos que las tareas listadas coincidan con la tabla esperada
    current_tasks = context.manager.tasks
    for row in context.table:
        name_to_find = row['Name']
        found = False
        for task in current_tasks:
            if task['name'] == name_to_find:
                # Verificamos también prioridad y descripción si están en la tabla
                assert task['priority'] == row['Priority']
                assert task['description'] == row['Description']
                found = True
                break
        assert found, f'La tarea "{name_to_find}" no se encontró en la salida.'

@then('the to-do list should show task "{name}" with status "{status}"')
def step_impl(context, name, status):
    for task in context.manager.tasks:
        if task['name'] == name:
            assert task['status'] == status, f"Se esperaba estado {status}, pero se encontró {task['status']}"
            return
    assert False, f'Tarea "{name}" no encontrada para verificar su estado.'

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.manager.tasks) == 0, "La lista no está vacía."

@then('the system should display an error message "{message}"')
def step_impl(context, message):
    # Verificamos si el mensaje esperado está dentro de lo que capturamos del print
    assert message in context.printed_output, \
        f"Se esperaba el mensaje '{message}', pero se obtuvo: '{context.printed_output}'"