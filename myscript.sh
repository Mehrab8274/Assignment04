venvname="myvenv"

if [ ! -d "$venvname" ]; then
    python -m venv "$venvname"
fi

source "$venvname/bin/activate"
pip install flask gunicorn

gunicorn -w 4 -b 0.0.0.0:3700 --reload Flask:app

