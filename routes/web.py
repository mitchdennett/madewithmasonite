''' Web Routes '''
from masonite.routes import Get, Post

ROUTES = [
    Get().route('/', 'ViewerController@show').name('main'),
    Get().route('/@id:int', 'ViewerController@show'),
    Get().route('/submit', 'SubmitController@show').name('submit')
]
