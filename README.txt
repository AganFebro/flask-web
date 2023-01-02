Tested using Ubuntu 20.04.
Error? fix sendiri mas bro!

apt install apache2
cd /var/www/
git clone https://github.com/AganFebro/flask-web.git
mv flask-web/ flaskweb
cd flaskweb
mkdir logs
touch logs/error.log
touch logs/access.log
apt install pipenv
pip install flask flask_sqlalchemy flask_login
apt install libapache2-mod-wsgi-py3
cp flask.conf /etc/apache2/sites-available/
nano /etc/apache2/sites-available/
#Bagian ServerName isi IP VPS mu! Lalu save (Ctrl+O) dan exit (Ctrl+X)
a2ensite flask.conf
systemctl reload apache2