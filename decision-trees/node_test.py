from unittest import TestCase
from Node import Node

class TestNode(TestCase):
    # define all the test cases
    def test_can_create_instance_of_node(self):
        node = Node("node", 1, [2])
        self.assertEqual(type(node), Node, msg="Node created is not of type Node.")

    def test_node_has_pythonic_getters(self):
        node = Node("mynode", 5, [6])
        class_name = node.class_name
        elements = node.elements
        branches = node.branches
        self.assertEqual("mynode", class_name)
        self.assertEqual(5, elements)
        self.assertEqual([6], branches)

    def test_node_has_pythonic_setters(self):
        node = Node("mynode", 0, [])
        node.class_name = "another class_name"
        node.elements = 2
        node.branches = [1, 2, 3]
        self.assertEqual("another class_name", node.class_name)
        self.assertEqual(2, node.elements)
        self.assertEqual([1, 2, 3], node.branches)

    def test_node_branches_should_be_a_list(self):
        self.assertRaises(TypeError, lambda: Node("mynode", 0, "I'm not a list!"))

    def test_node_class_name_should_be_a_string(self):
        self.assertRaises(TypeError, lambda: Node(1, 0, []))