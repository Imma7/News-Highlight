from app import create_app #Import create app function
from flask_script import Manager,Server #Import manager class to initialize our extension and server class to launch our server

# Creating app instance
app = create_app('development') #Call create_app function and pass the configuration options

manager = Manager(app) #Instantiate manager class by passing the app instance
manager.add_command('server',Server) #Command line on how our app should run

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()



