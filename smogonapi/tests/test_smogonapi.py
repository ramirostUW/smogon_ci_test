"""
This test suite makes sure the API and its endpoints all
work and return valid and meaningful responses.
"""

import unittest
import hashlib
from fastapi.testclient import TestClient

from smogonapi.main import myApp

class TestSmogonAPI(unittest.TestCase):
    """
    This test suite makes sure the API and its endpoints all
    work and return valid and meaningful responses.
    """

    def test_valid_procfile(self):
        """
        This test makes sure the procfile has not been modified
        in any way. It uses an MD5 hash, as that is the strictest
        way to ensure there have been zero modifications.

        Rule number one of the procfile: Don't touch the procfile.
        """

        precalculated_hash = "941deab554bc6834eef26b1222fe0e51"
        with open('../procfile','rb') as file:
            hashval = hashlib.md5(file.read()).hexdigest()
            self.assertTrue(precalculated_hash == hashval)

    def test_smoke_root(self):
        """
        This smoke test ensures the root endpoint
        returns a valid response.
        """
        client = TestClient(myApp)
        response = client.get("/")
        assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()