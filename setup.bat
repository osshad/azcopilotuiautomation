IF NOT EXIST selenv/Scripts/activate.bat (
    py -m venv selenv
)
call selenv/Scripts/activate.bat
py -m pip install -r requirements.txt