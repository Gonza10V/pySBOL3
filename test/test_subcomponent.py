import unittest

import sbol3


class TestSubComponent(unittest.TestCase):

    def test_create(self):
        instance_of = sbol3.Component('comp1')
        sc1 = sbol3.SubComponent('sc1', instance_of)
        self.assertIsNotNone(sc1)
        self.assertEqual(instance_of.identity, sc1.instance_of)
        sc2 = sbol3.SubComponent('sc2', instance_of.identity)
        self.assertEqual(instance_of.identity, sc2.instance_of)

    def test_invalid_create(self):
        # SubComponent requires an `instance_of` argument
        with self.assertRaises(TypeError):
            sbol3.SubComponent('sc1')


if __name__ == '__main__':
    unittest.main()
