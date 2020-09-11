#
# Uncomment one of these QUERY variables at a time and use "Test Run" to run it.
# You'll see the results below.  Then try your own queries as well!
#

# QUERY = "select max(name) from animals;"

# QUERY = "select * from animals limit 10;"

# QUERY = "select * from animals where species = 'orangutan' order by birthdate;"

# QUERY = "select name from animals where species = 'orangutan' order by birthdate desc;"

# QUERY = "select name, birthdate from animals order by name limit 10 offset 20;"

# QUERY = "select species, min(birthdate) from animals group by species;"

# QUERY = '''
# select name, count(*) as num from animals
# group by name
# order by num desc
# limit 5;
# '''

QUERY = '''
select food, count(animals.name) as num
       from diet, animals 
       where diet.species = animals.species
       group by food
       having num = 1
'''



#
# List all the taxonomic orders, using their common names, sorted by the number of
# animals of that order that the zoo has.
#
# The animals table has (name, species, birthdate) for each individual.
# The taxonomy table has (name, species, genus, family, t_order) for each species.
# The ordernames table has (t_order, name) for each order.
#
# Be careful:  Each of these tables has a column "name", but they don't have the
# same meaning!  animals.name is an animal's individual name.  taxonomy.name is
# a species' common name (like 'brown bear').  And ordernames.name is the common
# name of an order (like 'Carnivores').

'''
select ordernames.name, count(*) as num
  from animals, taxonomy, ordernames
  where animals.species = taxonomy.name
    and taxonomy.t_order = ordernames.t_order
  group by ordernames.name
  order by num desc
'''

# OR
'''
select ordernames.name, count(*) as num
  from (animals join taxonomy 
                on animals.species = taxonomy.name)
                as ani_tax
        join ordernames
             on ani_tax.t_order = ordernames.t_order
  group by ordernames.name
  order by num desc
  '''




  SUBQUERY = 
  '''
  select name, weight
    from players,
    (select avg(weight) as av
        from players) as subq  #have to name this subquery even though we don't use the name
    where weight < av;

'''



create table drivers (
  id serial primary key,
  first_name varchar,
  last_name varchar
);

create table vehicles (
  id serial primary key,
  make varchar,
  model varchar,
  driver_id integer references drivers(id)
);





INSERT INTO drivers (first_name, last_name) VALUES ('Bella', 'Redmond');
INSERT INTO drivers (first_name, last_name) VALUES ('Brandon', 'Redmond');
INSERT INTO drivers (first_name, last_name) VALUES ('Felipe', 'Pedrosa');


INSERT INTO vehicles (make, model, driver_id) 
VALUES ('Subaru', 'Crosstrek', 
        (SELECT id FROM drivers WHERE first_name = 'Brandon'));
INSERT INTO vehicles (make, model, driver_id) 
VALUES ('Subaru', 'Outback', 
        (SELECT id FROM drivers WHERE first_name = 'Felipe'));
INSERT INTO vehicles (make, model, driver_id) 
VALUES ('Subaru', 'Forester', 
        (SELECT id FROM drivers WHERE first_name = 'Bella'));



SELECT * from drivers;
SELECT * from vehicles;