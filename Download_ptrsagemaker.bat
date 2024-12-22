@echo off
setlocal

rem Define variables
set "REPO_URL=https://github.com/mfitzasp/ptrsagemaker/archive/refs/heads/main.zip"
set "ZIP_FILE=ptrsagemaker.zip"
set "DEST_DIR=ptrsagemaker"

rem Download the ZIP file using PowerShell
PowerShell -Command "Invoke-WebRequest -Uri '%REPO_URL%' -OutFile '%ZIP_FILE%'"

rem Check if the download was successful
if not exist "%ZIP_FILE%" (
    echo Failed to download the repository.
    exit /b 1
)

rem Extract the ZIP file using PowerShell
PowerShell -Command "Expand-Archive -Path '%ZIP_FILE%' -DestinationPath '%DEST_DIR%'"

rem Check if the extraction was successful
if not exist "%DEST_DIR%" (
    echo Failed to extract the repository.
    exit /b 1
)

rem Move the contents from ptrsagemaker-main to ptrsagemaker
if exist "%DEST_DIR%\ptrsagemaker-main\" (
    move "%DEST_DIR%\ptrsagemaker-main\*" "%DEST_DIR%\"
    rmdir "%DEST_DIR%\ptrsagemaker-main"
)

rem Clean up by deleting the ZIP file
del "%ZIP_FILE%"

echo Repository downloaded and extracted to %DEST_DIR%.