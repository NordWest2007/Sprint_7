#   Sprint_7

# Sprint_7

Тесты для API учебного сервиса Яндекс Самокат.

Проект содержит автотесты для для учебного сервиса «Яндекс.Самокат».  согласно заданию:
Что нужно сделать

Протестируй ручки. Проверь, что они корректно работают и выдают нужные ошибки.

Создание курьера
Проверь:
*курьера можно создать;
*нельзя создать двух одинаковых курьеров;
*чтобы создать курьера, нужно передать в ручку все обязательные поля;
*запрос возвращает правильный код ответа;
*успешный запрос возвращает {"ok":true};
*если одного из полей нет, запрос возвращает ошибку;
*если создать пользователя с логином, который уже есть, возвращается ошибка.
Логин курьера
Проверь:
*курьер может авторизоваться;
*для авторизации нужно передать все обязательные поля;
*система вернёт ошибку, если неправильно указать логин или пароль;
*если какого-то поля нет, запрос возвращает ошибку;
*если авторизоваться под несуществующим пользователем, *запрос возвращает ошибку;
*успешный запрос возвращает id.
Создание заказа
Проверь, что, когда создаёшь заказ:
*можно указать один из цветов — BLACK или GREY;
*можно указать оба цвета;
*можно совсем не указывать цвет;
*тело ответа содержит track.

Чтобы протестировать создание заказа, нужно использовать параметризацию.
Список заказов
*Проверь, что в тело ответа возвращается список заказов.
Отчёт Allure
*Сгенерируй отчёт и запушь в репозиторий.

Дополнительное задание

Протестируй ещё три ручки.
Удалить курьера
Проверь:
*неуспешный запрос возвращает соответствующую ошибку;
*успешный запрос возвращает{"ok":true};
*если отправить запрос без id, вернётся ошибка;
*если отправить запрос с несуществующим id, вернётся ошибка.

Принять заказ
Проверь:
*успешный запрос возвращает{"ok":true};
*если не передать id курьера, запрос вернёт ошибку;
*если передать неверный id курьера, запрос вернёт ошибку;
*если не передать id заказа, запрос вернёт ошибку;
*если передать неверный id заказа, запрос вернёт ошибку.
Получить заказ по его номеру
Проверь:
*успешный запрос возвращает объект с заказом;
*запрос без номера заказа возвращает ошибку;
*запрос с несуществующим заказом возвращает ошибку.
## Authors

- @NordWest2007