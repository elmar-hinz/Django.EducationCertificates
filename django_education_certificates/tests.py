from pathlib import Path

from django.test import TestCase

from thumbnails import get_thumbnail
import os.path


# Create your tests here.
class MyTests(TestCase):

    def test_thumbnail(self):
        # path = os.path.abspath('public/media/elmar.jpg')
        path = '/Volumes/Work/Projects/ElmarHinzDjango/public/media/Coursera' \
         '-Bioinformatics-Finding-Hidden-Messages-in-DNA.pdf'
        tn = get_thumbnail( path, '300x300', crop='center')
        x = 1
