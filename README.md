Для запуска проекта и получения результата вам требуется ввести ряд действий и команд

Скачивайте репозиторий и поместите в какое нибудь место на пк

создайте папки - "data" и "models"
необходимые данные test.csv и train.csv кидайте в папку data

далее в gitBash или в прочем терминале переходите в папку проекта и пишите



py -m venv venv

source venv/Scripts/activate

pip install -r requirements.txt



jupyter notebook

В открывшемся окне браузера открывайте файл  Notebook.ipynb

Выбираете Run/Run All Cells

затем тоже самое делайте в TestGetValue.ipynb

получайте результат в файл 'data/predict.csv'