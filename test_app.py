import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import app


class TestTodoApp(unittest.TestCase):
    def setUp(self) -> None:
        app.tasks.clear()

    def test_add_task_appends_new_task(self):
        with patch("builtins.input", return_value="Buy milk"):
            with io.StringIO() as buf, redirect_stdout(buf):
                app.add_task()
                output = buf.getvalue()

        self.assertEqual(len(app.tasks), 1)
        self.assertEqual(app.tasks[0]["task"], "Buy milk")
        self.assertFalse(app.tasks[0]["done"])
        self.assertIn("Task added successfully!", output)

    def test_view_tasks_prints_no_tasks_message(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            app.view_tasks()
            output = buf.getvalue()

        self.assertIn("No tasks to display.", output)

    def test_mark_done_sets_task_status_true(self):
        app.tasks.append({"task": "Buy milk", "done": False})
        with patch("builtins.input", return_value="1"):
            with io.StringIO() as buf, redirect_stdout(buf):
                app.mark_done()
                output = buf.getvalue()

        self.assertTrue(app.tasks[0]["done"])
        self.assertIn("Task marked as done.", output)

    def test_delete_task_removes_selected_task(self):
        app.tasks.extend([
            {"task": "Buy milk", "done": False},
            {"task": "Read book", "done": False},
        ])
        with patch("builtins.input", return_value="2"):
            with io.StringIO() as buf, redirect_stdout(buf):
                app.delete_task()
                output = buf.getvalue()

        self.assertEqual(len(app.tasks), 1)
        self.assertEqual(app.tasks[0]["task"], "Buy milk")
        self.assertIn("Task deleted.", output)


if __name__ == "__main__":
    unittest.main()
    