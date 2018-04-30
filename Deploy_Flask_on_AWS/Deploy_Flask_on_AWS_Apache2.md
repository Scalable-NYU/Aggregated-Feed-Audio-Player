# Deploy Flask on AWS with Apache2

## 1. Start EC2

Choose Ubuntu Server 16.04 LTS

Configure Security Group: SSH and HTTP

## 2. Install apache webserver and mod_wsgi

Set default system python version to 3.5.* / 3.6.*

    sudo apt-get update
    sudo apt-get install apache2
    # mod_wsgi is the interface for python webapplication on apache webserver.
    sudo apt-get install libapache2-mod-wsgi-py3

## 3. Install python-pip (pip) for python 3 and Flask

Google

## 4. We use ~/Aggregated-Feed-Audio-Player/ as our root directory, all scripts for this web application is under ~/Aggregated-Feed-Audio-Player

## 5. Link our script home directory to site-root.

The site-root for apache is defined at '/var/www/html' by default.

    sudo ln -sT ~/Aggregated-Feed-Audio-Player /var/www/html/AudioPlayer

## 6. Put out main python script directly under ~/Aggregated-Feed-Audio-Player

Our main script, [audioplayerapp.py](http://audioplayerapp.py) should have the following key lines:

    from flask import Flask
    app = Flask(__name__)
    ...
    @app.route('/') 
    def some_function():
    	...
    	return ...
    ...
    if __name__ == '__main__':
    	app.run()

## 7. Create .wsgi file for loading the web application

Create audioplayerapp.wsgi file directly under home directory:

    import sys
    sys.path.insert(0, '/var/www/html/audioplayerapp')
    
    from audioplayerapp import app as application

## 8. Modify dynamic content loading config file:

Replace the following config file with the /etc/apache2/sites-enabled/000-default.conf:

This file is also available on Github in our repository.

    <VirtualHost *:80>
            # WARNING!
            # Copy this file to ~/etc/apache2/sites-enabled, replace 000-default.conf
            #
            # Run:
            #       sudo service apache2 restart
            # to (re)start the service.
            #
            # The ServerName directive sets the request scheme, hostname and port that
            # the server uses to identify itself. This is used when creating
            # redirection URLs. In the context of virtual hosts, the ServerName
            # specifies what hostname must appear in the request's Host: header to
            # match this virtual host. For the default virtual host (this file) this
            # value is not decisive as it is used as a last resort host regardless.
            # However, you must set it for any further virtual host explicitly.
            #ServerName www.example.com
    
            ServerAdmin webmaster@localhost
            DocumentRoot /var/www/html
    
            WSGIDaemonProcess audioplayerapp threads=5
            WSGIScriptAlias / /var/www/html/AudioPlayer/audioplayerapp.wsgi
    
            <Directory audioplayerapp>
                WSGIProcessGroup audioplayerapp
                WSGIApplicationGroup %{GLOBAL}
                Order deny,allow
                Allow from all
            </Directory>
    
            # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
            # error, crit, alert, emerg.
            # It is also possible to configure the loglevel for particular
            # modules, e.g.
            #LogLevel info ssl:warn
    
            ErrorLog ${APACHE_LOG_DIR}/error.log
            CustomLog ${APACHE_LOG_DIR}/access.log combined
    
            # For most configuration files from conf-available/, which are
            # enabled or disabled at a global level, it is possible to
            # include a line for only one particular virtual host. For example the
            # following line enables the CGI configuration for this host only
            # after it has been globally disabled with "a2disconf".
            #Include conf-available/serve-cgi-bin.conf
    </VirtualHost>
    # vim: syntax=apache ts=4 sw=4 sts=4 sr noet

## 9. Start/Re-start the webserver:

    sudo service apache2 restart

## 10*. Tail the server log:

The server log is available at /var/log/apache2/error.log, investigate any error by:

    tail -20f  ~/var/log/apache2/error.log