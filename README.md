# 12_image_resize

Модуль позволяет изменять размер изображения в формате jpg и png
_____________________________________________

Установка:

    pip install -r requirements.txt

Запуск:

    python image_resize.py pic.jpg

Возможные ключи запуска:

 * --width - задать ширину новому файлу

 * --height - задать высоту новому файлу

 * --scale - масштаб нового файла относительно оригинала

 * --output - путь к новому файлу

_________________________________

Логика работы:

 * Если указана только ширина – высота считается так, чтобы сохранить пропорции изображения. И наоборот. – Если указана и ширина и высота – создать именно такое изображение. Вывести в консоль предупреждение, если пропорции не совпадают с исходным изображением.

 * Если указан масштаб, то ширина и высота указаны быть не могут. Иначе никакого ресайза не происходит и скрипт ломается с понятной ошибкой.

 * Если не указан путь до финального файла, то результат кладётся рядом с исходным файлом. Если исходный файл называется pic.jpg (100x200), то после вызова python image_resize.py --scale 2 pic.jpg должен появиться файл pic__200x400.jpg.
