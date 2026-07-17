import unittest
from unittest.mock import patch
from app import get_username

class TestDatabase(unittest.TestCase):

    @patch("app.Database.get_user")
    def test_get_username(self, mock_get_user):
        # Fake database response
        mock_get_user.return_value = {
            "id": 1,
            "name": "Bob"
        }

        result = get_username(1)

        self.assertEqual(result, "Bob")

        # Verify the mocked method was called once
        mock_get_user.assert_called_once_with(1)

if __name__ == "__main__":
    unittest.main()

Output:
.
----------------------------------------------------------------------
Ran 1 test

OK
