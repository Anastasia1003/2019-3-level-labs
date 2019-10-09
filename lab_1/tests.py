import datetime
import unittest
import json
import validators
from lab_1.parser import get_html_page, find_articles, publish_report



class TestCrawler(unittest.TestCase):
    def setUp(self):
        page = open("lab_1/vc.html", "r", encoding="UTF-8")
        page_content = page.read()
        page.close()
        self.url = 'https://vc.ru/'
        self.html = page_content
        self.array = [{'title': 'Как Slack-боты убили дашборды'},
                              {'title': 'Как за десять дней заработать $60 тысяч и получить бесценные инсайты о продукте'},
                              {'title': '10 вещей, без которых ваш ресторан превратится в забегаловку'}, {'title': 'Офис JetBrains в Санкт-Петербурге'},
                              {'title': 'Факторы ранжирования медицинских сайтов по коммерческим запросам'},
                              {'title': 'Структура SDR-отдела в сервисной ИТ-компании'},
                              {'title': 'Как айтишники 20 километров проплыли'},
                              {'title': 'Откуда не ждали: три финтех-стартапа из Африки, Южной Америки и Юго-Восточной Азии'}, 
                              {'title': 'Языковой сервис Duolingo запустит приложение для обучения детей родному языку \n\n\nМатериал редакции'},
                              {'title': 'Лекторий vc.ru в Москве: как сообщество и продукт развивают друг друга \n\n\nМатериал редакции'},
                              {'title': 'Собери сам: как магазин мебели выстроил экосистему аналитики в одном окне'}, 
                              {'title': 'Власти России разрешат продавцам на экспорт получать возврат НДС без сбора бумажных документов с апреля 2020 года \n\n\nМатериал редакции'},
                              {'title': 'Суд оставил основателя Baring Vostok Майкла Калви под домашним арестом до 13 января 2020 года \n\n\nМатериал редакции'},
                              {'title': 'Три эпичных моментов стартапа: как пройти и выжить'}, 
                              {'title': 'Сеть книжных магазинов «Республика» сменила гендиректора второй раз за месяц \n\n\nМатериал редакции'},
                              {'title': '«Яндекс» предложил Avito, ivi, «2ГИС» и другим уладить конфликт из-за мест в поисковой выдаче \n\n\nМатериал редакции'},
                              {'title': 'Бот на проводе: как выбрать кейс и платформу для обзвона (и не разозлить клиента)'}, {'title': 'Как мы продаём сайты и SEO в США, часть вторая'},
                              {'title': 'UX-исследования не решат всех ваших проблем'}, 
                              {'title': 'Продуктовая сеть «Вкусвилл» откроет аптеки в своих магазинах вместе с партнёром \n\n\nМатериал редакции'}, 
                              {'title': 'Что нового в macOS Catalina: закрытие iTunes, iPad как второй монитор, обновление приложений и «Локатор» \n\n\nМатериал редакции'},
                              {'title': 'Алгоритмы подбора лучших предложений'}, {'title': 'Нормальный текст вакансии'},
                              {'title': 'Чем занимается «белый хакер», как им стать и сколько можно заработать \n\n\nМатериал редакции'}]

     def test_get_html_page(self):
        self.assertEqual(get_html_page(self.url).status_code, 200) 
        
        
    def test_find_articles(self):
        self.assertListEqual(find_articles(self.html), self.array)


    def test_file_structure(self):
        result = {"url": page_url,
              "creationDate": datetime.datetime.now().strftime("%b %m, %Y, %H:%M"),
              "articles": articles}
        path = "lab_1/articles.json"
        publish_report(path, result)
        with open(path, 'r', encoding="UTF-8") as h_content:
            data = json.load(h_content.read())
        self.assertTrue(validators.url(data["url"]))
        try:
            creation_date_datetime = datetime.datetime.strptime(data["creationDate"], '%Y-%m-%d').date()
        except ValueError:
            print('Invalid date!')
        self.assertNotEqual(len(data["articles"]), 0)

    if __name__ == '__main__':
        unittest.main()
