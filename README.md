parallel-launcher
=================

Это обертка над GNU Parallel, призванная уменьшить ручной труд и увеличить производительность труда.
Обычно я пишу код на С и со временем мне приходится передаватьв негов качестве аргументов больше 10 параметров.
Это эмммм... утомляет. А пропустить один и получить на выходе мусор - совсем неприятно.:unamused:

Поэтому я написал `parallel-launcher`!

### Особенности

* Каждый вводимый параметр является строкой (если не должен быть раскрыт). Никаких потерь на приведение типов.

* Киллер-фича: диапазоны!

Легким движением руки `20:20:300` превращается в `20 40 60 80 100 120 140 160 180 200 220 240 260 280 300`

* Авто-подстановка значения по умолчанию. Просто нажми Enter!

### Как оно работает

* Подготавливается конфигурация, она же файл настроек, включающая в себя список всех параметров, их порядок, значения по умолчанию и т. д.
Если посмотреть на пример, станет понятнее.

* Конфигурация импортируется в основном файле.

* Всё! Интерактивная программа запуска готова к работе!


![parallel-launcher GIF](https://user-images.githubusercontent.com/5108025/82938596-bf362c80-9f9a-11ea-989b-bee5667efcd9.gif)


--------------------------

It is a wrapper for GNU Parallel created to minimize manual labor with my scientific code.
My simulation programs are often written in C and have 10+ command line arguments.
Filling them all up is really tedious. I have grown tired of losing a parameter and having computed junk:unamused:

So now we have `parallel-launcher`!

### Features

* Every input is treated as a string unless they should be expanded, so they are safe!

* Killer-feature: Ranges expansion!

`20:20:300` will be transmuted into `20 40 60 80 100 120 140 160 180 200 220 240 260 280 300`

* Auto substitute of default value. Just press Enter!

### How it works

* A configuration ('settings') file must be prepared. It includes all parameters to pass to main executable, their order and other stuff.
Have a look at an example, it is documented.
* Import settings inside main file.
* That's it! You now have an interactive GNU Parallel launcher.


