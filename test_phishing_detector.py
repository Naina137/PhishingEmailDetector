import unittest
from phishing_detector import check_email_content

class TestPhishingDetector(unittest.TestCase):
    def test_suspicious_email(self):
        result = check_email_content("Urgent! Verify your account at http://192.168.0.1/login")
        self.assertIn("Contains suspicious keyword: urgent", result["issues"])

    def test_safe_email(self):
        result = check_email_content("Hello Naina, meeting at 5 PM")
        self.assertEqual(result["issues"], [])

if __name__ == "__main__":
    unittest.main()
