import unittest

SERVER = "server_b"


class AllAsertsTest(unittest.TestCase):

    def test_assert_equal_when_values_match_should_pass(self):
        self.assertEqual(10, 10)
        self.assertEqual("Hola", "Hola")

    def test_assert_true_and_false_when_conditions_are_true_or_false_should_pass(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_assert_raises_when_value_is_invalid_should_raise_value_error(self):
        with self.assertRaises(ValueError):
            int("No_soy_un_numero")

    def test_assert_in_when_value_is_present_and_absent_should_pass(self):
        self.assertIn("a", "Hola")
        self.assertNotIn("z", "Hola")

    def test_assert_dicts_when_dictionaries_have_same_content_should_be_equal(self):
        dict1 = {"a": 1, "b": 2}
        dict2 = {"a": 1, "b": 2}
        self.assertDictEqual(dict1, dict2)
        self.assertSetEqual(set(dict1.keys()), set(dict2.keys()))

    @unittest.skip("Trabajo en progreso, sera habilitada nuevamente")
    def test_skip_when_test_is_not_ready_should_be_skipped(self):
        self.assertEqual("Hola", "chao")

    @unittest.skipIf(SERVER == "server_b", "Saltado porque no estamos en el servidor")
    def test_skip_if_when_server_is_not_target_should_be_skipped(self):
        self.assertEqual(100, 100)

    @unittest.expectedFailure
    def test_expected_failure_when_intentional_failure_is_expected_should_be_reported(self):
        self.assertEqual(10, 20, "Este test esta diseñado para fallar")