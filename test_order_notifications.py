import unittest

from order_notifications import format_order_status_message, normalize_language


class OrderNotificationTextsTest(unittest.TestCase):
    def test_normalize_language_fallback(self):
        self.assertEqual(normalize_language('ka-GE'), 'ka')
        self.assertEqual(normalize_language('fr'), 'en')

    def test_format_accepted_ru(self):
        text = format_order_status_message(
            status='accepted',
            language='ru',
            order_id=42,
            restaurant_name='Test Cafe',
        )
        self.assertIn('#42', text)
        self.assertIn('Test Cafe', text)

    def test_format_delivering_en(self):
        text = format_order_status_message(
            status='delivering',
            language='en',
            order_id=7,
            restaurant_name='Cafe',
        )
        self.assertIn('on the way', text)


if __name__ == '__main__':
    unittest.main()
