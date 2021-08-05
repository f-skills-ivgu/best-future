# best-future

1.	Зайти на сайт http://uptoqa.ru:5000/
2.	Пользователь может зарегистрироваться. При регистрации заводится электронная почта, пароль (повторяется дважды), имя пользователя. В поле “role” таблицы User при регистрации автоматически проставляется 0, т.е. без прав администратора. Свой статус администратор меняет самостоятельно вручную, непосредственно в самой БД 
В программе реализованы 2 типа учетной записи:
– обычный пользователь: 
– администратор: 
3.	Авторизация проводится путём введения почты и пароля. 
4.	Права обычного пользователя:
     – просмотр расписания;
     – выход из учетной записи для повторной авторизации.
5.	Права администратора:
– просмотр расписания,
– создание новых занятий с указанием всех данных,
– редактирование свойств существующих занятий;
	
Для тестирования возможностей обычных пользователей:
	Логин: edan@gmail.com
	Пароль: 1
Для тестирования возможностей администратора:
	Логин: apav@mail.ru
	Пароль: 1 







ЗАДАНИЕ 3. ИНКЛЮЗИВНЫЕ РЕШЕНИЯ ДЛЯ ЛИЦ С НАРУШЕНИЯМИ ЗРЕНИЯ – не реализовано, но обдумано!

Настройки по Требованиям ГОСТ Р 52872-2019
Интернет-ресурсы и другая информация, представленная в электронно-цифровой форме.
Приложения для стационарных и мобильных устройств, иные пользовательские интерфейсы.
Требования доступности для людей с инвалидностью и других лиц с ограничениями жизнедеятельности
1.	Крупный знак на странице авторизации A (приемлемый), AA (высокий) и AAA (наивысший) либо глаз.
2.	Страница выбора настроек:
– шрифт (3 разных);
– цветовые настройки (белый на черном, черный на белом, белый на синем)
– возможность увеличивать межбуквенные расстояния;
– возможность отключения изображений;
– возврат на обычную версию.
3.	Остальные страницы:
– нет .pdf
– замена медиаконтента текстовым;
– масштабирование до 200%;
– замена видеоконтента на аудио;
– замена капча на аудиовопросы;
– контрастность оптимальная 7:1
– аудиоуправление функциями сайта;
– возможность работать без помощи мыши, только клавишами Enter и Tab;
Инклюзивное решение Команды BestFuture – полностью аудиоверсия сайта с управлением голосом и клавишами ДА (Y) и НЕТ (N).
Блоки:
1.	Авторизация голосом. Установка голосового анализатора.
2.	 Использование нейросети для построения системы распознавания речи.
3.	База данных голосов – эталонный голос пользователя для прохождения авторизации. 
4.	Дерево решений для навигации по сайту.
5.	Использование Android.Media для ввода/вывода информации.