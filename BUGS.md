BUG_report-1 : Отображение отрицательного значения в счетчике

Предусловие:

Открыть сайт Avito - https://www.avito.ru/
Зайти во вкладку "Польза"
Выбрать вкладку "Экосчетчик"
Шаги:


Поменять в тестовых данных JSON значение water = -1
Ожидаемый результат: Значение осталось прежним,0 или сообщение об ошибке
Фактический результат: Счетчик имеет значение "-1"

Окружение: Chromium Версия 125.0.6422.26 , (64 бит)

Приоритет: high

![img.png](attachments/img.png)