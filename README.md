# NewsProject
<h2>NewsProject - это веб-приложение Django, представляющее собой новостной портал</h2>
<hr>

<h3>Проект создан для обучения на курсе SkillFactory и закрепления полученных знаний</h3>

<h3>Для того, чтобы запустить код достаточно загрузить себе на компьютер данный репозиторий, затем выполнить команды:<br>
  -установить и запустить Redis;<br>
  -в первом терминале перейти в директорию NewsProject/NewsPro/NewsPaper и написать команду python manage.py runserver;<br>
  -запустить Celery во втором терминале с помощью команды: celery -A NewsPaper worker  --pool=solo (--pool=solo использовать в случае использования Python 3.10 и выше), а в третьем терминале ввести команду: celery -A NewsPaper beat.<br> 
  После этого можно будет перейти по ссылке (http://127.0.0.1:8000/news/) и лицезреть этот прекрасный портал :)<br>
  Удачи!</h3>

  <h3>UPD 10.07: Было добавлено приложение "deletenews", которое удаляет все новости из выбранной категории.<br> Для использования достаточно ввести в терминале: <br> python manage.py deletenews <название категории большими буквами> <br> Доступный список категорий на данный момент:<br> SPORT <br> IT <br> MUSIC <br> AUTO <br> NATURE <br> POLITICS</h3>
