import datetime
import unittest
import json
import validators
from lab_1.main.parser import get_html_page, find_articles, publish_report



class TestCrawler(unittest.TestCase):
    def setUp(self):
        page = open("lab_1/main/test/BAR.htm", "r", encoding="UTF-8")
        page_content = page.read()
        page.close()
        self.url = 'http://thenoisetier.com/blog/tag/BAR'
        self.html = page_content
        self.array = [{'title': 'КУДА ПОЛЕТЕТЬ В БАРХАТНЫЙ СЕЗОН: 5 НАПРАВЛЕНИЙ'},
                      {'title': 'ЧТО СДЕЛАТЬ ЭТОЙ ОСЕНЬЮ: ВДОХНОВЛЯЮЩИЙ ЧЕК-ЛИСТ'},
                      {'title': 'КАК ПРОХОДИЛА ПЯТАЯ ГОДОВЩИНА СВАДЬБЫ АНАСТАСИИ ВОЛКОВОЙ В ТОСКАНЕ?'},

                      {'title': 'STRESS LESS: КАК НАУЧИТЬСЯ НЕ ПЕРЕЖИВАТЬ ПО ПУСТЯКАМ'},
                      {'title': '4 алкогольных коктейля, которые нужно попробовать этой осенью'},

                      {'title': 'Какое шампанское выбрать на Новый год: варианты от 2000 рублей'},

                      {'title': 'Три легких вина на жаркий летний вечер'},
                      {'title': 'Итальянский уикенд: 3 летних вина, о которых вы не знали'},

                      {'title': 'Как устроить идеальный бранч с подругами?'}]

    def test_get_html_page(self):
        a2 = get_html_page('http://thenoisetier.com/blog/tag/BARrrrr')
        print(a2)
        self.assertEqual(a2.status_code, 404)
        self.assertEqual(get_html_page(self.url).status_code, 200)



    def test_find_articles(self):
        self.assertListEqual(find_articles(self.html), self.array)

    def test_file_structure(self):
        creation_date = datetime.datetime.now().strftime("%b %m, %Y, %H:%M")
        result = {"url": self.url,
                  "creationDate": creation_date,
                  "articles": self.array}
        path = "lab_1/main/articles.json"
        publish_report(path, result)
        with open(path, 'r', encoding="UTF-8") as headers_content:
            content = json.load(headers_content)
        self.assertTrue(validators.url(content["url"]))
        try:
            datetime.datetime.strptime(content["creationDate"], '%b %m, %Y, %H:%M').date()
        except ValueError:
            print('Invalid date!')
        self.assertNotEqual(len(content["articles"]), 0)


    if __name__ == '__main__':
        unittest.main()
