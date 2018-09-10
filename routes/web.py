''' Web Routes '''
from masonite.routes import Get, Post

ROUTES = [
    Get().route('/', 'WelcomeController@show').name('welcome'),
    Get().route('/submit', 'SubmitController@show').name('submit')
]
