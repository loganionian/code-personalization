import unittest
from code_personalization.main import CodePersonalizationModel

class TestCodePersonalizationModel(unittest.TestCase):
    def test_learn_and_suggest(self):
        model = CodePersonalizationModel()
        model.learn("print('Hello, World!')")
        suggestion = model.suggest("context")
        self.assertIn("Suggested", suggestion)

if __name__ == "__main__":
    unittest.main()