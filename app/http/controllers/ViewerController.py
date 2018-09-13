''' A Module Description '''
import math
from app.Site import Site

class ViewerController:
    ''' Class Docstring Description '''

    def show(self, Application, Request):
        id = Request.param('id')
        print(id)
        prev_page = -1
        
        if id == False:
            id = 1
            sites = Site.paginate(15, 1)
        else:
            id = int(id)
            sites = Site.paginate(15, id)

        users_length = Site.count()
        num_of_pages = math.ceil(users_length/15)

        next_page = id + 1
        if next_page > num_of_pages:
            next_page = -1

        prev_page = id - 1
        if prev_page < 1:
            prev_page = -1

        page_array = self.abbreviated_pages(num_of_pages, id)
        return view('viewer', {
            'app': Application,
            'sites': sites,
            'current_page': str(id),
            'prev_page': prev_page, 
            'next_page': next_page , 
            'page_array': page_array
        })

    def abbreviated_pages(self, n, page):
        """
        Return a string containing the list of numbers from 1 to `n`, with
        `page` indicated, and abbreviated with ellipses if too long.

        >>> abbreviated_pages(5, 3)
        '1 2 [3] 4 5'
        >>> abbreviated_pages(10, 10)
        '1 2 3 4 5 6 7 8 9 [10]'
        >>> abbreviated_pages(20, 1)
        '[1] 2 3 ... 18 19 20'
        >>> abbreviated_pages(80, 30)
        '1 2 3 ... 28 29 [30] 31 32 ... 78 79 80'
        """
        assert(0 < n)
        assert(0 < page <= n)

        # Build set of pages to display
        if n <= 10:
            pages = set(range(1, n + 1))
        else:
            pages = (set(range(1, 4))
                    | set(range(max(1, page - 2), min(page + 3, n + 1)))
                    | set(range(n - 2, n + 1)))

        # Display pages in order with ellipses
        def display():
            last_page = 0
            for p in sorted(pages):
                if p != last_page + 1: yield '...'
                yield ('{0}').format(p)
                last_page = p

        return display()