''' A Module Description '''
from app.Site import Site

class SubmitController:
    ''' Class Docstring Description '''

    def show(self, Application):
        return view('submit', {
            'app': Application
        })

    def store(self, Application):
        site = Site()
        site.site_name = request().input('site_name')
        site.submitter_name = request().input('submitter_name')
        site.submitter_email = request().input('submitter_email')
        site.url = request().input('url')
        site.image_url = ''
        site.approved = False
        site.save()
        request().redirect('/1')
