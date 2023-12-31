# Учебный проект - "Доска объявлений"
1. Регистрация пользователей реализована с помощью библиотеки allauth.
При регистрации пользователю на email высылается письмо с просьбой подтверждения регистрации и ссылкой для подтверждения.
При регистрации пользователи автоматически добавляются в группу authors c правами на создание и редактирование объявлений.
Board/accounts/forms.py
Суперюзер: логин: admin, пароль: admin. Имеет так же права на удаление любого объявления.
2. Реализованы модели Article(объявления) и UserResponse (Отклики пользователей) в приложении  Board/posts/models.py
3. На главной странице зарегистрированному пользователю доступна кнопка "Комментировать" на любое объявление для формирования откликов.
При добавлении объявления или комментария автор объекта заполняется автоматически значением зарегистрированного пользователя. Выбор категории персонажа
реализован с помощью выпадающего списка. При создании объявления автор обязательно должен определить категорию персонажа. При добавлении объявления
реализована возможность прикреплять изображение. 
При добавлении комментария статус комментария в форме скрыт и по умолчанию неактивен.
Заголовок объявлений кликабельный, переводит на представление для отражения конкретного объявления. К данному объявлению отражаются 
комментарии только в том случае, если они подтверждены автором объявления.
Формы: Board/posts/forms.py
Представления: Board/posts/views.py
Шаблоны: Board/templates
4. На приватной странице автора отражаются только объявления зарегистрированного автора. На данной странице пользователь может редактировать 
свои объявления, принимать, отклонять и удалять комментарии, которые оставили другие пользователи. Так же на этой странице реализован
поиск объявлений по заголовку, типу персонажа и дате публикации, чтобы легко найти нужное объявление и отработать комментарии по нему.
Для реализации действия принятия, отмены принятия комментария реализован метод update_status в модели UserResponse.

Board/posts/filters.py
5. В проекте реализованы сигналы по следующим событиям:
- При создании комментария к объявлению, автор объявления получает уведомление на адрес эл.почты, указанной при регистрации.
- При принятии комментария автором объявления, автор комментария получает уведомление на адрес эл.почты, указанной при регистрации.
- При удалении комментария автором объявления, автор комментария получает уведомление на адрес эл.почты, указанной при регистрации.
Board/posts/signals.py
6. В шапке сайта закреплены и работают все ссылки. Зарегистрированному пользователю доступны кнопки "Главная","Добавить объявление",
"Страница автора", "Профиль", "Выход". При выходе из профиля досупны ссылки "Главная","Регистрация","Вход".


