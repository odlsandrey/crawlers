
### promoprice парсер цен портала prom.ua
#### Может быть использована для отслеживания цен конкурентов
##### Программа принимает базовые значения цен вашего сайта, орентируясь на ваш файл выгрузки с портала пром. Выполняет поиск всех товаров на проме, согласно наименованию и артикулу, производит анализ и записывает результат в excel файл.
- В программу встроен не большой классификатор текста, поскольку в файле выгрузки обнаружены некоторые ошибки и не соответствия, в идеале используя валидатор, эти ошибки необходимо устранить из базового файла.

#### Запуск программы
* Установите зависимости
* Исполняемый файл находиться в каталоге spiders prom.py
* Запуск паука можно осуществить из каталога promoprice файл run.py
* Переименуйте файл выгрузки с прома в export.xlsx
* Результат будет записан в файл result.xlsx
* Не корректные поля записываются в error-price.xlsx (необходим для анализа и отладки, а также просмотр результата выдачи)

#### Файл пользовательских настроек usersettings.ini
* Раздел [engine] Переменная pricelist=True Используется при чтении файла прайса. True - значить файл содержит все поля выгрузки с прома. Важно цена должна быть в колонке "I", если установить значение в False пример pricelist=False - значит входящий файл содержит поля (код товара название позиции, цена) 3 колонки последовательно
* Видео заметка https://youtu.be/XNC1PJ-iSpU
##### !!! Продукт может поддерживаться в индивидуальном порядке! 










