Эндоскопическая капсула (видеокапсула) — это одноразовое устройство, которое используется для диагностики состояния органов пищеварительного тракта.

На данный момент я занимаюсь проектом на тему разработки аппаратного комплекса эндоскопической капсулы для исследования ЖКТ. Что бы продвинутся дальше на пути к успешному завершению проекта я решила сделать прототип камеры, которая будет находится в такой капсуле. В качестве основы мне порекомендовали выбрать raspbery py и raspbery py camera.Конечно, можно было выбрать аналог на Arduino, ведь со средой для програмирования компонентов Arduino IDU я больше знакома, но все же стоит выделить основные для меня приемущества raspbery py:
1. Дешевизна и доступность. В Центре Талантов Кемерово имеется в доступе камера rasbery py и она в разы дешевле, чем аналог от Arduino.
2. Возможные проблемы. Из-за неопытности в програмировании есть рийск сломать дорогую камеру, что явно будет усложнять работу.
3. Простота в кодинге. Так как модуль rasbery py програмируется на языке python, это явно упростит работу, ведь весь мой код будет находится в одной среде

Основной функцией проекта является считывание изображения с камеры и передача на экран монитора.
