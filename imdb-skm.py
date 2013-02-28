#!/usr/bin/env python

import requests
import argparse
from lib.results import SkM 

def agpar():
    parser = argparse.ArgumentParser(description='IMDB scraper!')
    parser.add_argument('-r', '--rating', help='The rating review.', action='store_true')
    parser.add_argument('-g', '--genre', help='The genre of the movie you are looking up.', action='store_true')
    parser.add_argument('-R', '--rated', help='The rated of motion picture.', action='store_true')
    parser.add_argument('-l', '--language', help='The language the movie is in.', action='store_true')
    parser.add_argument('-p', '--poster', help='Url for the movie poster.', action='store_true')
    parser.add_argument('-d', '--directors', help='Director of movie.', action='store_true')
    parser.add_argument('-u', '--url', help='The imdb url for the movie.', action='store_true')
    parser.add_argument('-i', '--ID', help='The imdb id for the movie.', action='store_true')
    parser.add_argument('-c', '--country', help='The country.', action='store_true')
    parser.add_argument('-L', '--location', help='The locations where filmed.', action='store_true')
    parser.add_argument('-w', '--writers', help='The movie writers.', action='store_true')
    parser.add_argument('-a', '--actors', help='The starring actors/actresses.', action='store_true')
    parser.add_argument('-P', '--plot', help='Gives simple overview of plot.', action='store_true')
    parser.add_argument('-y', '--year', help='Year of release.', action='store_true')
    parser.add_argument('-T', '--runtime', help='Movie length.', action='store_true')
    parser.add_argument('-o', '--release', help='Date of release.', action='store_true')
    parse = parser.parse_args()
    return parse


    
def main(options):
    lookup = raw_input('What movie/show did you wish to look up? ')
    try:
        lookup = lookup.split(' ') 
    except AttributeError:
        print 'Invalid data type!'
        return
    SkM(lookup, ap)    
 

if __name__ == '__main__':
    ap = agpar()
    main(ap)

