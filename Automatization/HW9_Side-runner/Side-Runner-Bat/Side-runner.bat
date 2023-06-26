@echo off
@chcp 866

REM Запрос запуска с правами администратора
REM if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

TITLE Side-runner
cls
color F0
set PATH=%PATH%;C:\temp\driver
set current=/d "%~dp0"
cd %current%


:mainMenu

echo ■═════════════════════■ ГЛАВНОЕ МЕНЮ ■════════════════════■
echo ╔═════════════════════════════════════════════════════════╗
echo ║  [ 1 ] --  Установка всего необходимого              --║
echo ╠=========================================================╣
echo ║  [ 2 ] --  Запуск .side проектов                     --║
echo ╠=========================================================╣
echo ║  [ 3 ] --  Запустить Командную строку                --║
echo ╠=========================================================╣
echo ║  [ 4 ] --  (='.'=)     Выйти     (=-.-=)             --║
echo ╚═════════════════════════════════════════════════════════╝

GOTO insert



:insert
REM Ввод данных
echo _______________________ 
set /p inserted="Введите цифру режима: "

REM Присвоение введённого значения перменной, которая может быть только числом
set /a choise=%inserted%

REM Проверка данных на принадлежность к числам. Если присвоено не число, переменная имеет значение  0
IF %choise% leq 0 (
	GOTO error
)ELSE (
	GOTO action
)

REM Условия рвботы программы
:action
IF %choise%==1 (
	GOTO setupMenu
) ELSE IF %choise%==2 (
	GOTO sideMenu
) ELSE IF %choise%==3 (
	GOTO cmdLine
) ELSE IF %choise%==4 (
	GOTO end
) ELSE GOTO mainMenu

REM Просмотр system32
:system32
set wind=C:\Windows\System32
cd %wind% 
dir
GOTO end

REM Сообщение об ошибке и выход
:error
echo ___________________________________________________________
echo Введённые данные некорректны. Выход из программы с ошибкой
pause
EXIT /b 128

REM Меню выбора установок и настроек
:setupMenu
echo ■════════════════════■ МЕНЮ УСТАНОВОК ■═══════════════════■
echo ╔═════════════════════════════════════════════════════════╗
echo ║ [ 1 ] --  Установить Node.js                        --║
echo ╠=========================================================╣
echo ║ [ 2 ] --  Установить Side-runner                    --║
echo ╠=========================================================╣
echo ║ [ 3 ] --  Скачать webdrivers для Node               --║	 
echo ╠=========================================================╣
echo ║ [ 4 ] --  Скопировать webdrivers  .exe              --║
echo ╠=========================================================╣
echo ║ [ 5 ] --  Выйти в Главное меню        (=-.-=)       --║
echo ╚═════════════════════════════════════════════════════════╝

GOTO setupInsert

REM Ввод и проверка данных полльзователя
:setupInsert
echo _______________________ 
set /p inserted="Введите цифру установщика: "

REM Присвоение введённого значения перменной, которая может быть только числом
set /a choise=%inserted%

REM Проверка данных на принадлежность к числам. Если присвоено не число, переменная имеет значение  0
IF %choise% leq 0 (
	GOTO setupMenu
)ELSE (
	GOTO setupAction
)

REM Выбор функциии установщика
:setupAction
IF %choise%==1 (
	GOTO nodeSetup
) ELSE IF %choise%==2 (
	GOTO sideSetup
) ELSE IF %choise%==3 (
	GOTO downloadWDrivers
) ELSE IF %choise%==4 (
	GOTO copyWDrivers
) ELSE IF %choise%==5 (
	GOTO mainMenu
) ELSE GOTO setupMenu

REM Запуск установки Node.js
:nodeSetup
node-v18.16.0-x64.msi
GOTO setupMenu

REM Запуск установки selenium-side-runner
:sideSetup
npm install -g selenium-side-runner@3.17.0
GOTO setupMenu

REM Скачивание веб-драйверов для Node
:downloadWDrivers
npm install -g chromedriver && npm install -g edgedriver && npm install -g geckodriver && npm install -g opera && Side-runner.bat


REM копирование скаченных ранее в папку, указанную в PATH

:copyWDrivers
set DriverDir=C:\temp\driver
IF NOT EXIST "%DriverDir%" mkdir C:\temp\driver
REM set PATH=%PATH%;C:\temp\driver
copy driver C:\temp\driver 
GOTO setupMenu


REM Меню выбора режимов работы SIDE-RUNNER
:sideMenu
echo ■══════════════════════■ SIDE-RUNNER ■════════════════════■
echo ╔═════════════════════════════════════════════════════════╗
echo ║   [ 1 ] --  Использовать Chrome                    --║
echo ╠=========================================================╣
echo ║   [ 2 ] --  Использовать Firefox                   --║
echo ╠=========================================================╣
echo ║   [ 3 ] --  Использовать Edge                      --║
echo ╠=========================================================╣
echo ║   [ 4 ] --  Не Использовать Opera                  --║
echo ╠=========================================================╣
echo ║   [ 5 ] --  Выйти в Главное Меню                   --║
echo ╚═════════════════════════════════════════════════════════╝

GOTO sideInsert

:sideInsert
REM Ввод данных
echo _______________________ 
set /p inserted="Введите цифру браузера: "

REM Присвоение введённого значения перменной, которая может быть только числом
set /a choise=%inserted%

REM Проверка данных на принадлежность к числам. Если присвоено не число, переменная имеет значение  0
IF %choise% leq 0 (
	GOTO sideMenu
)ELSE (
	GOTO side-RunnerAction
)


:side-RunnerAction
IF %choise%==1 (
	GOTO sideChrome
) ELSE IF %choise%==2 (
	GOTO sideFirefox
) ELSE IF %choise%==3 (
	GOTO sideEdge
) ELSE IF %choise%==4 (
	GOTO sideOpera
) ELSE IF %choise%==5 (
	GOTO mainMenu
)ELSE GOTO sideMenu



:sideChrome
set /p sidePath="укажите путь до файла .side, например C:\temp\1.side ===>  "
selenium-side-runner -c "browserName=chrome" %sidePath%
echo Введите Side-runner.bat чтобы запусить программу снова или exit для выхода

:sideFirefox
set /p sidePath="укажите путь до файла .side, например C:\temp\1.side ===>  "
selenium-side-runner -c "browserName=firefox" %sidePath%
echo Введите Side-runner.bat чтобы запусить программу снова или exit для выхода

:sideEdge
set /p sidePath="укажите путь до файла .side, например C:\temp\1.side ===>  "
selenium-side-runner -c "browserName=MicrosoftEdge" %sidePath%

:sideOpera
set /p sidePath="укажите путь до файла .side, например C:\temp\1.side ===>  "
selenium-side-runner --c "browserName='opera'" %sidePath%



:cmdLine
cmd


REM Завершение работы
:end
echo ■═════════════════════════════■
echo ║ Всем спасибо, все свободны! ║
echo ■═════════════════════════════■
pause
EXIT /b 0
echo on 


