#!/usr/bin/env python

import requests
import argparse

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

class MovieScraper(object):
    
    def __init__(self):
        self.movie = raw_input('What movie did you wish to look up? ')
        self.movie = self.movie.split(' ') 

    def scrape(self, options):
        req = requests.get('http://www.imdbapi.org/?title=%s' % self.movie)
        try:
            data = req.json()[0]
        except KeyError:
            print '****************************************************'
            print ''
            print 'Make sure the title is correct!'
            print ''
            print '----------------------------------------------------'
            return
        print '****************************************************'
        print ''
        print 'Title: %s' % data['title']
        print ''
        print '----------------------------------------------------'
        if options.directors:
            d = ''
            for director in data['directors']:
                d = d + director + ', '
            d = d.rstrip(', ')
            print ''
            print 'Directors: %s' % d
        if options.writers:
            w = ''
            for writer in data['writers']:
                w = w + writer + ', '
            w = w.rstrip(', ')
            print ''
            print 'Writers: %s' % w
        if options.actors:
            a = ''
            for actor in data['actors']:
                a = a + actor + ', '
            a = a.rstrip(', ')
            print ''
            print 'Actors/Actresses: %s' % a
        if options.rating:
            print ''
            print 'Movie Rating: %s' % data['rating']
        if options.rated:
            print ''
            print 'Rated: %s' % data['rated']
        if options.language:
            l = ''
            for lang in data['language']:
                l = l + lang + ', '
            l = l.rstrip(', ')
            print ''
            print 'Language: %s' % l
        if options.poster:
            print ''
            print 'Poster Url: %s' % data['poster']
        if options.url:
            print '' 
            print 'IMDB address: %s' % data['imdb_url']
        if options.ID:
            print ''
            print 'IMDB id: %s' % data['imdb_id']
        if options.plot:
            print ''
            print 'Plot: %s' % data['plot_simple']
        if options.release:
            rel = str(data['release_date'])
            print ''
            print 'Release Date: %s' % rel[4:6] + ' ' + rel[6:8] + ' ' + rel[:4]
        if options.year:
            print ''
            print 'Year: %s' % data['year']
        if options.location:
            print ''
            print 'Filming Locations: %s' % data['filming_locations']
        if options.runtime:
            r = ''
            for runtime in data['runtime']:
                r = r + runtime + ', '
            r = r.rstrip(', ')
            print ''
            print 'Total Runtime: %s' % r
        if options.country:
            c = ''
            for cntry in data['country']:
                c = c + cntry + ', '
            c = c.rstrip(', ')
            print ''
            print 'Country: %s' % c
        if options.genre:
            g = ''  
            for genre in data['genres']:
                g = g + genre + ', '
            g = g.rstrip(', ')
            print ''
            print 'Genre: %s' % g
        print '----------------------------------------------------'
        return  

if __name__ == '__main__':
    ap = agpar()
    ms = MovieScraper()
    ms.scrape(ap)

