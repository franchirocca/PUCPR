import unittest
from AS1.todo import TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo = TodoList()

    def test_add_task(self):
        task = self.todo.add_task("Learn Python")
        self.assertIn("Learn Python", task['description'])
        self.assertFalse(task['completed'])

    def test_get_tasks(self):
        self.todo.add_task("Learn Python")
        self.todo.add_task("Build a project")
        self.assertEqual(len(self.todo.get_tasks()), 2)

    def test_complete_task(self):
        self.todo.add_task("Learn Python")
        task = self.todo.complete_task(0)
        self.assertTrue(task['completed'])

if __name__ == '__main__':
    unittest.main()
