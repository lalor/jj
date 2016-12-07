import os
import jinja2
import unittest
from bs4 import BeautifulSoup

def render(tpl_path, **kwargs):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(**kwargs)

class TestJinja(unittest.TestCase):

    def test_simple(self):
        title = "Title  H   "
        items = ({'href':'a.com', 'caption':'ACaption'}, {'href':'b.com', 'caption':'Bcaption'})
        content="This is content"
        result = render('simple.html', title = title, content=content, items = items )

        soup = BeautifulSoup(result, 'lxml')
        self.assertEqual(soup.body.h1.text, title.strip()) # title
        a = soup.findAll('a')
        self.assertEqual(len(a), len(items)) # items
        self.assertEqual(soup.body.p.text, content) # content


if __name__ == '__main__':
    unittest.main()
