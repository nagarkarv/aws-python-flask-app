from flask import (
	Flask,
	render_template
	)
import connexion

print('Starting')
# Create the application instance
print('Creating app instance')
#app = Flask(__name__, template_folder="templates")

application = connexion.App(__name__, specification_dir='./')
application.add_api('swagger.yml')

print('Creating default route')
# Create a URL route in our application for "/"
@application.route('/')
def home():
	return render_template('home.html')

@application.route('/contactus')
def contactus():
	return "Welcome to contact us page!"

# if we are running in standalone mode, run the application
if __name__ == "__main__":
	print('running app.run')
	application.debug = True
	application.run(host='0.0.0.0')