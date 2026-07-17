from unittest.mock import Mock

mock = Mock()

mock.side_effect = [
    {"name": "Alice"},
    {"name": "Bob"}
]

print(mock())
print(mock())

Output:
{'name': 'Alice'}
{'name': 'Bob'}
