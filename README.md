# Игра про вертолёте
Простенькая игра, суть которой, набивать очки за тушение пожара в лесу.
В игре реализована система подсчета очков.
Вертолет имеет несколько характеристик: 
 - Жизни, при потери всех жизней игра заканчивается;
 - Запас воды, для тушения огня;
 - Очки, которые можно получить за тушения огня.

Управлять вертолётом можно при помощи классической раскладки WASD.
Графика сделана из смайликов.

Площадь игрового поля можно будет изменять.
Присутствует система слоев, игровая зона состоит из двух слоев, так называемые "Небо" и "Земля". 
На слое "Небо" есть такие объекты как:
 - Вертолет, которым мы соответственно управляем;
 - Облака, скрывающие то что находятся за ними;
 - Грозы, наносящие урон вертолету.

На слое "Земля" есть такие объекты как:
 - Река, в которой нужно будет пополнять запас воды для тушения;
 - Дерево, которое может сгореть;
 - Здание Улучшений, улучшающий вертолет за n-ное кол-во очков;
 - Госпиталь, востанавливющий по единице здоровья за n-ное кол-во очков.

Присутствует система радомизации, т.е. при каждом новой игре, игровое поле рандомизируется, Леса и Реки будут находиться на различных позициях, так же как и Здания Улучшения и Госпиталя