from unittest.case import TestCase

from tsau import tongmia


class TongMia(TestCase):
    def test_tongmia(self):
        self.assertEqual(tongmia('h-demo_postgres_1_23f035bb92e5'), 'h-demo')
