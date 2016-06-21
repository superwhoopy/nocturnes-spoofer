import os
import os.path
import urllib.request
import shutil
import feedparser

FEED       = 'http://www.rtl.fr/podcast/les-nocturnes.xml'
OUTPUT_DIR = './out'

def main():
    feed = feedparser.parse(FEED)
    for entry in feed.entries:
        link = entry.guid
        filename = link.split('/')[-1]
        filepath = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(filepath):
            print('file {} already exists: skipping'.format(filename))
            continue
        try:
            print('Getting {}'.format(filename))
            urllib.request.urlretrieve(link,
                    filename=os.path.join(OUTPUT_DIR, filename))
        except:
            print('FAILED downloading {}'.format(link))
            if os.path.exists(filepath):
                os.remove(filepath)
    return feed

if __name__ == '__main__':
    main()
