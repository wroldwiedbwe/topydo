# Topydo - A todo.txt client written in Python.
# Copyright (C) 2014 Bram Schoenmakers <me@bramschoenmakers.nl>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import CommandTest
import PriorityCommand
import TodoList

class PriorityCommandTest(CommandTest.CommandTest):
    def setUp(self):
        todos = [
            "(A) Foo",
            "Bar",
        ]

        self.todolist = TodoList.TodoList(todos)

    def test_set_prio1(self):
        command = PriorityCommand.PriorityCommand(["1", "B"], self.todolist, self.out, self.error)
        command.execute()

        self.assertTrue(self.todolist.is_dirty())
        self.assertEquals(self.output, "Priority changed from A to B\n(B) Foo\n")
        self.assertEquals(self.errors, "")

    def test_set_prio2(self):
        command = PriorityCommand.PriorityCommand(["2", "Z"], self.todolist, self.out, self.error)
        command.execute()

        self.assertTrue(self.todolist.is_dirty())
        self.assertEquals(self.output, "Priority set to Z.\n(Z) Bar\n")
        self.assertEquals(self.errors, "")

    def test_invalid1(self):
        command = PriorityCommand.PriorityCommand(["99", "A"], self.todolist, self.out, self.error)
        command.execute()

        self.assertFalse(self.todolist.is_dirty())
        self.assertFalse(self.output)
        self.assertEquals(self.errors, "Invalid todo number given.\n")

    def test_invalid2(self):
        command = PriorityCommand.PriorityCommand(["1", "ZZ"], self.todolist, self.out, self.error)
        command.execute()

        self.assertFalse(self.todolist.is_dirty())
        self.assertFalse(self.output)
        self.assertEquals(self.errors, "Invalid priority given.\n")

    def test_invalid3(self):
        command = PriorityCommand.PriorityCommand(["A"], self.todolist, self.out, self.error)
        command.execute()

        self.assertFalse(self.todolist.is_dirty())
        self.assertFalse(self.output)
        self.assertEquals(self.errors, command.usage() + "\n")

    def test_invalid4(self):
        command = PriorityCommand.PriorityCommand(["1"], self.todolist, self.out, self.error)
        command.execute()

        self.assertFalse(self.todolist.is_dirty())
        self.assertFalse(self.output)
        self.assertEquals(self.errors, command.usage() + "\n")

    def test_empty(self):
        command = PriorityCommand.PriorityCommand([], self.todolist, self.out, self.error)
        command.execute()

        self.assertFalse(self.todolist.is_dirty())
        self.assertFalse(self.output)
        self.assertEquals(self.errors, command.usage() + "\n")