from staticjinja import Site
import sys

import json
def load_json(file):
    def wrap():
        f = open(file, 'r')
        try:
            d = json.loads(f.read())
        except Exception as e:
            print("unable to load %s" % file)
            print(e)
            sys.exit(0)
        f.close()
        return d
    return wrap

if __name__ == "__main__":
    site = Site.make_site(contexts=[
        ('.*.html', load_json('content/base.json')),
        ('index.html', load_json('content/testimonials.json')),
        ('index.html', load_json('content/index.json')),
        ('how-it-works.html', load_json('content/testimonials.json')),
        ('how-it-works.html', load_json('content/how-it-works.json')),
        ('impact.html', load_json('content/impact.json')),
        ('contact.html', load_json('content/contact.json')),
        ('mission.html', load_json('content/mission.json')),        
        # ('about.html', load_json('content/about.json'))
    ], mergecontexts=True, outpath='site')

    site.render(use_reloader=True)
