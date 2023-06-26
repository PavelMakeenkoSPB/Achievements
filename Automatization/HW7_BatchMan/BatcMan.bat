@echo off
@chcp 866

REM Запрос запуска с правами администратора
REM if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

TITLE BatcMan Returns!!
cls
color F0
:menu

echo ■═══════════════════════■ МЕНЮ ■══════════════════════════■
echo ╔═════════════════════════════════════════════════════════╗
echo ║ [ 1 ] --  Увидеть файлы в папке system.32           --║
echo ╠=========================================================╣
echo ║ [ 2 ] --  Посмотреть содержимое папки с этим файлом --║
echo ╠=========================================================╣
echo ║ [ 3 ] --  Указать желаемую папку для просмотра      --║
echo ╠=========================================================╣
echo ║ [ 4 ] --  (='.'=)     Выйти     (=-.-=)             --║
echo ╚═════════════════════════════════════════════════════════╝

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
	GOTO system32
) ELSE IF %choise%==2 (
	GOTO batFileDir
) ELSE IF %choise%==3 (
	GOTO yourDir
) ELSE IF %choise%==4 (
	GOTO end
) ELSE GOTO error

REM Просмотр system32
:system32
set wind=C:\Windows\System32
cd %wind% 
dir
GOTO end

REM Просмотр текущей папки с bat файлом
:batFileDir
set current=/d "%~dp0"
cd %current% 
dir
GOTO end

REM Просмотр указанной папки 
:yourDir
echo __________________________________________________________________________________
set /p yourDirictory="Введите путь к желаемой папке, например: C:\Windows\, или 4 для вывода Меню ===> "
IF EXIST "%yourDirictory%" (
	cd %yourDirictory%
	dir
	GOTO end
) ELSE IF %yourDirictory%==4 (
	GOTO menu
) ELSE (
	echo По указанному адресу ничего не найдено :(
	GOTO yourDir)

REM Сообщение об ошибке и выход
:error
echo ___________________________________________________________
echo Введённые данные некорректны. Выход из программы с ошибкой
pause
EXIT /b 128

REM Завершение работы
:end
echo ■═════════════════════════════■
echo ║ Всем спасибо, все свободны! ║
echo ■═════════════════════════════■
pause
EXIT /b 0
echo on 

