import unittest
from phonesimulator import phone

try:
    from mock import MagicMock, patch, Mock
except:
    from unittest.mock import MagicMock, patch, Mock

# import xmldict

txt = 'text rss00000'
txt2 = 'text 2 DDDD'


class TxtObject(object):
    def __init__(self):
        self.text = txt2


class factPhone(unittest.TestCase):
    def setUp(self):
        self.phone = phone.Phone()

    def test_workfor(self):
        with self.assertRaises(NotImplementedError):
            self.phone.workfor(1)

    def test_chargefor(self):
        with self.assertRaises(NotImplementedError):
            self.phone.chargefor(1)

    def test_show_news_mock(self):
        mock_method = MagicMock(return_value=txt)
        self.phone._real_get_news = mock_method
        news = self.phone.show_news()
        self.assertEqual(news, txt)
        news = self.phone.show_news()
        self.assertEqual(news, txt)
        mock_method.assert_called_once_with()
        self.assertEqual(news, txt)

    @patch('requests.get')
    def test_show_news_decorator(self, mock):
        xxx = TxtObject()
        setattr(xxx, 'text', txt2)
        mock.return_value = xxx
        news = self.phone.show_news()
        self.assertEqual(news, txt2)
        mock.assert_called_once_with("https://www.yahoo.com/news/rss/entertainment")

    def test_show_news_patch_with(self):
        xxx = TxtObject()
        setattr(xxx, 'text', txt2)
        with patch('requests.get') as mock_get:
            mock_get.return_value = xxx
            news = self.phone.show_news()
            self.assertEqual(news, txt2)

    def test_show_news(self):
        news = self.phone.show_news()
        self.assertNotEqual(news, txt)


if __name__ == '__main__':
    unittest.main()
