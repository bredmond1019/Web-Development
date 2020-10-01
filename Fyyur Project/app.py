#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
from flask_migrate import Migrate

from sqlalchemy.exc import SQLAlchemyError
from datetime import date
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)


migrate = Migrate(app, db)
#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#



class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, nullable = False, default = True)
    website = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    shows = db.relationship('Show',
      backref=db.backref('venues', lazy=True))

    def __repr__(self):
      return f'<Venue {self.id}: {self.name} in {self.city}>'



class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    genres = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, nullable = False, default = True)
    seeking_description = db.Column(db.String(120))
    website = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    shows = db.relationship('Show', backref = db.backref('artist', lazy = True))

    def __repr__(self):
      return f'<Artist {self.id} {self.name}>'

class Show(db.Model):
    __tablename__ = 'show'
    id = db.Column(db.Integer, primary_key = True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable = False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable = False)
    start_time = db.Column(db.DateTime, nullable = False)

    def __repr__(self):
      return f'<Show {self.id}, Venue: {self.venue_id}, Artist: {self.artist_id}>'




#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format)

app.jinja_env.filters['datetime'] = format_datetime



#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')


#  Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
  now = datetime.utcnow()
  all_places = Venue.query.distinct(Venue.state, Venue.city)
  data = []
  for places in all_places:
    venues = Venue.query.filter(Venue.state == places.state, Venue.city == places.city).all()
    record = {
      'city': places.city, 
      'state': places.state,
      'venues' : [{'id': venue.id, 
                   'name':venue.name, 
                   "num_upcoming_shows" : Show.query.filter_by(venue_id = venue.id).filter(Show.start_time>now).count()} for venue in venues],
    }
    data.append(record)
  return render_template('pages/venues.html', areas=data);

@app.route('/venues/search', methods=['POST'])
def search_venues():

  search = request.form.get('search_term')
  
  now = datetime.utcnow()
  venues = Venue.query.filter(Venue.name.ilike(f'%{search}%')).all()
  print(venues)
  response = {
    "count" : len(venues),
    "data" : [{"id": venue.id, 
               "name": venue.name,
               "num_upcoming_shows": Show.query.filter_by(venue_id = venue.id).filter(Show.start_time>now).count()} 
               for venue in venues]
  }
  return render_template('pages/search_venues.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  # shows the venue page with the given venue_id
  now = datetime.utcnow()
  venue = Venue.query.get(venue_id)
  data = venue.__dict__
  data['past_shows'] = []
  data['upcoming_shows'] = []
  data['genres'] = data['genres'].strip('}{').split(',')
  past_shows = Show.query.filter_by(venue_id = venue_id).filter(Show.start_time < now).all()
  upcoming_shows = Show.query.filter_by(venue_id = venue_id).filter(Show.start_time > now).all()
  if past_shows:
    for show in past_shows:
      tmp = {
        "artist_id" : show.artist_id, 
        "artist_name" : Artist.query.filter_by(id = show.artist_id).all()[0].name,
        "artist_image_link" : Artist.query.filter_by(id = show.artist_id).all()[0].image_link,
        "start_time" : show.start_time
      }
      data['past_shows'].append(tmp)
  if upcoming_shows:
    for show in upcoming_shows:
      tmp = {
        "artist_id" : show.artist_id, 
        "artist_name" : Artist.query.filter_by(id = show.artist_id).all()[0].name,
        "artist_image_link" : Artist.query.filter_by(id = show.artist_id).all()[0].image_link,
        "start_time" : show.start_time
      }
      data['upcoming_shows'].append(tmp)
  data["past_shows_count"] = len(past_shows)
  data["upcoming_shows_count"] = len(upcoming_shows)

  return render_template('pages/show_venue.html', venue=data)

#  Create Venue
#  ----------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
    print(request.form)
    try:

      venue = Venue(
        name = request.form['name'],
        city = request.form['city'],
        state = request.form['state'],
        address = request.form['address'],
        phone = request.form['phone'],
        genres = request.form.getlist('genres'),
        image_link = request.form['image_link'],
        facebook_link = request.form['facebook_link'],
        website = request.form['website'],
        seeking_talent = True if 'seeking_talent' in request.form else False,   
      )
      db.session.add(venue)
      db.session.commit()
      flash('Venue ' + request.form['name'] + ' was successfully listed!')
    except SQLAlchemyError as e:
      db.session.rollback()
      flash('An error occurred. Venue ' + request.form['name'] + ' could not be listed.')
      print(request.form)
      print(e)
    finally:
      db.session.close()
    return render_template('pages/home.html')

@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):

  try:
    venue = Venue.query.get(venue_id)
    db.session.delete(venue)
    db.session.commit()
    flash('Venue successfully Deleted')
  except SQLAlchemyError as e:
    db.session.rollback()
    print(e)
    flash('An error occurred. Could not delete Venue')
  finally:
    db.session.close()  

  return jsonify({ 'success' : True })

#  Artists
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
  
  artists = Artist.query.all()
  data = [{
    'id' : artist.id, 
    'name' : artist.name
    } for artist in artists]

  return render_template('pages/artists.html', artists=data)

@app.route('/artists/search', methods=['POST'])
def search_artists():

  search = request.form.get('search_term')
  artists = Artist.query.filter(Artist.name.ilike(f'%{search}%')).all()
  response = {
    'count' : len(artists), 
    "data" : [{
      "id" : artist.id,
      'name' : artist.name
    } for artist in artists]
  }
  
  return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  # shows the venue page with the given venue_id
  # TODO: replace with real venue data from the venues table, using venue_id
  now = datetime.utcnow()
  artist = Artist.query.get(artist_id)
  data = artist.__dict__
  data['past_shows'] = []
  data['upcoming_shows'] = []
  data['genres'] = data['genres'].strip('}{').split(',')
  past_shows = Show.query.filter_by(artist_id = artist_id).filter(Show.start_time < now).all()
  upcoming_shows = Show.query.filter_by(artist_id = artist_id).filter(Show.start_time > now).all()
  if past_shows:
    for show in past_shows:
      tmp = {
        "venue_id" : show.venue_id, 
        "venue_name" : Venue.query.filter_by(id = show.venue_id).all()[0].name,
        "venue_image_link" : Venue.query.filter_by(id = show.venue_id).all()[0].image_link,
        "start_time" : show.start_time
      }
      data['past_shows'].append(tmp)
  if upcoming_shows:
    for show in upcoming_shows:
      tmp = {
        "venue_id" : show.venue_id, 
        "venue_name" : Venue.query.filter_by(id = show.venue_id).all()[0].name,
        "venue_image_link" : Venue.query.filter_by(id = show.venue_id).all()[0].image_link,
        "start_time" : show.start_time
      }
      data['upcoming_shows'].append(tmp)
  data["past_shows_count"] = len(past_shows)
  data["upcoming_shows_count"] = len(upcoming_shows)
  
  
  return render_template('pages/show_artist.html', artist=data)

#  Update
#  ----------------------------------------------------------------
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  form = ArtistForm()
  artist={
    "id": 4,
    "name": "Guns N Petals",
    "genres": ["Rock n Roll"],
    "city": "San Francisco",
    "state": "CA",
    "phone": "326-123-5000",
    "website": "https://www.gunsnpetalsband.com",
    "facebook_link": "https://www.facebook.com/GunsNPetals",
    "seeking_venue": True,
    "seeking_description": "Looking for shows to perform at in the San Francisco Bay Area!",
    "image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80"
  }
  # TODO: populate form with fields from artist with ID <artist_id>
  return render_template('forms/edit_artist.html', form=form, artist=artist)

@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  # TODO: take values from the form submitted, and update existing
  # artist record with ID <artist_id> using the new attributes

  return redirect(url_for('show_artist', artist_id=artist_id))

@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  form = VenueForm()
  venue={
    "id": 1,
    "name": "The Musical Hop",
    "genres": ["Jazz", "Reggae", "Swing", "Classical", "Folk"],
    "address": "1015 Folsom Street",
    "city": "San Francisco",
    "state": "CA",
    "phone": "123-123-1234",
    "website": "https://www.themusicalhop.com",
    "facebook_link": "https://www.facebook.com/TheMusicalHop",
    "seeking_talent": True,
    "seeking_description": "We are on the lookout for a local artist to play every two weeks. Please call us.",
    "image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60"
  }
  # TODO: populate form with values from venue with ID <venue_id>
  return render_template('forms/edit_venue.html', form=form, venue=venue)

@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  # TODO: take values from the form submitted, and update existing
  # venue record with ID <venue_id> using the new attributes
  return redirect(url_for('show_venue', venue_id=venue_id))

#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  # called upon submitting the new artist listing form
    try:
      artist = Artist(
        name = request.form['name'],
        city = request.form['city'],
        state = request.form['state'],
        phone = request.form['phone'],
        genres = request.form.getlist('genres'),
        image_link = request.form['image_link'],
        seeking_venue = True if 'seeking_venue' in request.form else False,
        seeking_description = request.form['seeking_description'],
        website = request.form['website'],
        facebook_link = request.form['facebook_link'],   
      )
      db.session.add(artist)
      db.session.commit()
      flash('Artist ' + request.form['name'] + ' was successfully listed!')
    except SQLAlchemyError as e:
      db.session.rollback()
      flash('An error occurred. Artist ' + request.form['name'] + ' could not be listed.')
      print(request.form)
      print(e)
    finally:
      db.session.close()
  
    return render_template('pages/home.html')


#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  # displays list of shows at /shows
  # TODO: replace with real venues data.
  #       num_shows should be aggregated based on number of upcoming shows per venue.
  shows = Show.query.all()
  data = [{
    'venue_id' : show.venue_id,
    'venue_name' : Venue.query.filter_by(id = show.venue_id).all()[0].name,
    'artist_id' : show.artist_id,
    "artist_name" : Artist.query.filter_by(id = show.artist_id).all()[0].name,
    "artist_image_link": Artist.query.filter_by(id = show.artist_id).all()[0].image_link,
    "start_time": show.start_time
  } for show in shows]
  
  return render_template('pages/shows.html', shows=data)

@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  # called to create new shows in the db, upon submitting new show listing form
  try:
    show = Show(
      venue_id = request.form['venue_id'],
      artist_id = request.form['artist_id'],
      start_time = request.form['start_time'],
    )
    db.session.add(show)
    db.session.commit()
    flash('Show was successfully listed!')
  except SQLAlchemyError as e:
    db.session.rollback()
    flash('An error occurred. Show could not be listed.')
    print(request.form)
    print(e)
  finally:
    db.session.close()

  return render_template('pages/home.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
