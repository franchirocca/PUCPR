import unittest
from unittest.mock import patch
from todo_app import TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo = TodoList()

    @patch('builtins.print')
    def test_add_task(self, mock_print):
        self.todo.add_task("Aprender Python")
        mock_print.assert_called_with("Tarefa adicionada: Aprender Python")

    @patch('builtins.print')
    def test_list_tasks(self, mock_print):
        self.todo.add_task("Aprender Python")
        self.todo.list_tasks()
        mock_print.assert_called_with("1. Aprender Python - Pendente")

    @patch('builtins.print')
    def test_complete_task(self, mock_print):
        self.todo.add_task("Aprender Python")
        self.todo.complete_task(1)
        mock_print.assert_called_with("Tarefa 1 marcada como completada!")

if __name__ == '__main__':
    unittest.main()
