IMDbSkM
=======

IMDbSkM is tool for retrieving information on your favorite(or not so favorite) tv shows and movies.  

As you can tell from the name, this data is coming from the well-known website http://www.imdb.com.
Using an api provided by http://www.imdbapi.org, you can find most information on just about any
movie or tv show.

There are two IMDbSkM versions.  A UI version that uses the popular toolkit wxPython.  The GUI has
checkboxes, so you can pick and chose what data you'd like to return.  There is also a command-line 
version, that can take a number of optional arguments.

Sample cmdline version:
    
    python cmdlne.py -rgdaTP

    ********************************************

    Title: Blade Runner

    --------------------------------------------

    Directors: Ridley Scott

    Actors/Actresses: Harrison Ford, Rutger Hauer, Sean Young, Edward James Olmos, M. Emmet Walsh, Daryl Hannah, William Sanderson, Brion James, Joe Turkel, Joanna Cassidy, James Hong, Morgan Paull, Kevin Thompson, John Edward Allen, Hy Pyke

    Movie Rating: 8.3

    Plot: Deckard, a blade runner, has to track down and terminate 4 replicants who hijacked a ship in space and have returned to earth seeking their maker.

    Total Runtime: 117 min

    Genre: Drama, Sci-Fi, Thriller
    --------------------------------------------



IMDbSkM uses two modules that are not part of the python standard library, so you will need to install them first.

    pip install wxPython

and 

    pip install requests
