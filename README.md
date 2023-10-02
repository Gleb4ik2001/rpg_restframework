<h3 style="text-align: center;">How to deploy?</h3>
    <ol>
        <li>git clone https://github.com/Gleb4ik2001/rpg_restframework.git</li>
        <li>py -m venv env</li>
        <li>pip install -r requirements.txt</li>
        <li>you need to replace SECRET_KEY, DEBUG, BACKEND, DBNAME with the appropriate values.</li>
        <li>py manage.py makemigrations</li>
        <li>py manage.py migrate</li>
        <li>py manage.py runserver</li>
    </ol>
    <h3 style="text-align: center;">Routes:</h3>
    <ol>
        <li>http://localhost:8000/game_regimes/</li>
        <li>http://localhost:8000/characters/</li>
        <li>http://localhost:8000/maps/</li>
    </ol>
    <h3 style="text-align: center;">Allowed methods:</h3>
    <ol>
        <li>LIST</li>
        <li>RETRIEVE</li>
        <li>CREATE</li>
    </ol>