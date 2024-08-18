@echo off
:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python before running this script.
    pause
    exit /b
)

:: Install required Python packages
echo Installing required Python packages...
pip install requests beautifulsoup4 >nul 2>&1

:: Run the Python script
echo Running the Python script...
python h2m-server-scraper.py

:: Pause at the end to see the result
pause
