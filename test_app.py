import unittest
from app import QUESTIONS, validate_answers
class SurveyTests(unittest.TestCase):
    def setUp(self):
        self.answers = {q["id"]: q["options"][0]["value"] for q in QUESTIONS}
    def test_counts(self):
        self.assertEqual(len(QUESTIONS), 7)
        self.assertEqual(sum(len(q["options"]) for q in QUESTIONS), 29)
    def test_valid(self):
        self.assertEqual(validate_answers(self.answers), self.answers)
    def test_every_option(self):
        for q in QUESTIONS:
            for o in q["options"]:
                payload = dict(self.answers)
                payload[q["id"]] = o["value"]
                self.assertEqual(validate_answers(payload)[q["id"]], o["value"])
    def test_missing(self):
        self.answers.pop("Q7")
        with self.assertRaises(ValueError): validate_answers(self.answers)
    def test_bad(self):
        self.answers["Q1"] = "unknown"
        with self.assertRaises(ValueError): validate_answers(self.answers)
    def test_wrong_type(self):
        with self.assertRaises(ValueError): validate_answers([])
if __name__ == "__main__": unittest.main()
