# This file demonstrates how to use Python to interface with MongoDB
import datetime
import pymongo

# With MongoEngine installed, we need to direct the library to connect with
# the running instance of Mongo using connect() and passing the host and port
# of the MongoDB database
from mongoengine import *

# MongoClient is used to communicate with the running database instance
from pymongo import MongoClient

# SQL vs NoSQL
# MongoDB is a NoSQL database. NoSQL databases provide features of retrieval
# and storage of data in a much different way than relational databases.
#
# The need to store complex data structures led to the birth of NoSQL
# databases, which allow a developer to store heterogeneous and structure-less
# data
#
# Both SQL and NoSQL have their strengths and weaknesses, you should choose the
# one that fits your application requirements.
#
# SQL
# - Of a relational nature
# - Data is stored in tables
# - Suitable for solutions where every record is of the same kind and possesses
#   the same properties
# - Adding a new property means having to alter the whole schema
# - The schema is very strict
# - Supports ACID transactions
# - Scales well vertically
#
# NoSQL
# - Non-relational
# - May be stored as JSON, key-value, etc. (depending on type of NoSQL
#   database)
# - Not every record has to be of same nature (making it flexible)
# - Add new properties to data without disturbing anything
# - No schema requirements to adhere to
# - Support for ACID transactions varies depending on which NoSQL DB is used
# - Consistency can vary
# - Scales well horizontally
#
# When choosing a database, consider the strengths and weaknesses of each
#
# There are different types of NoSQL databases to choose from, each with its
# own use-cases:
# - Key-Value Store: DynamoDB
# - Document Store: CouchDB, MongoDB, RethinkDB
# - Column Store: Cassandra
# - Data-Structures: Redis
#
# SQL and NoSQL databases have begun to merge. PostgreSQL now supports storing
# and querying JSON data, much like Mongo. Mongo still provides the advantage
# of horizontal scaling and a simple interface.
#
# If your active data sits comfortably in a relational schema and the JSON
# content is a cohort to that data, then you should be fine with PostgreSQL and
# its efficient JSONB representation and indexing capabilities. If though, your
# data model is that of a collection of mutable documents, then you probably
# want to look at a database engineered primarily around JSON documents like
# MongoDB or RethinkDB.

# MONGODB
# MongoDB is a document-oriented, open-source database program that is
# platform-independent. MongoDB, like some NoSQL databases, stores its data in
# documents using a JSON structure. This is what allows the data to be so
# flexible and not require a schema.
#
# Some important features:
# - Support for standard query types, like matching (==), comparison (<, >), or
#   even regex
# - You can store virtually any kind of data - structured, partially
#   structured, polymorphic
# - To scale up and handle more queries, just add more machines
# - Highly flexible and agile, allowing you to quickly develop applications
# - Document-based means you can store all information regarding your model in
#   a single document
# - You can change the schema on the fly
# - Many relational database functionalities are available (e.g. indexing)
#
# There are tools and features for MongoDB that you can't find with any other:
# - Whether you need a standalone server or complete clusters of independent
#   servers, MongoDB is as scalable as you need it to be
# - MongoDB provides load balancing support by automatically moving data across
#   the various shards
# - It has automatic failover support - in case your primary server goes down,
#   a new primary will be up and running automatically
# - The MongoDB Management Service (MMS) is a nice web tool that provides the
#   ability to track your machines
# - Thanks to memory mapped files, you save quite a bit of RAM, unlike
#   relational databases
#
# If you take advantage of the indexing features, much of the data will be kept
# in memory for quick retrieval. Even without indexing on specific document
# keys, Mongo caches quite a bit of data using the least recently used method
#
# One common drawback is Mongo's lack of support for ACID transactions. Mongo
# does support ACID transactions in a limited sense, but not in all cases. At
# the single-document level, ACID transactions are supported (which is where
# most transactions take place anyway). However, transactions dealing with
# multiple documents are not supported due to Mongo's distributed nature.
#
# Mongo also lacks support for native joins, which must be done manually (and
# therefore much more slowly). Documents are meatn to be all-encompassing,
# which means, in general, they shouldn't need to reference other documents.
# In the real world, this doesn't always work as much of the data we work with
# is relational by nature. Therefore many will argue that Mongo should be used
# as a complementary database to a SQL DB, but as you use MongoDB you'll find
# that is not necessarily true.

# PYMONGO
# The official driver published by Mongo developers is called PyMongo. This is
# a good place to start when first firing Python with MongoDB.

# Establishing a Connection
# Using PyMongo
# By default, the connection is established to the 'localhost' and
# 27017 port. Below is the customized version
client = MongoClient('localhost', 27017)

# Using MongoEngine
# connect('mongoengine_test', host='localhost', port=27017)
# Since we're still using the default host and port, we omit these parameters
mongo_eng = connect('mongoengine_test')

# Using the Mongo URI format:
# client = MongoClient('mongodb://localhost:27017')

# Accessing Databases
# Once you have a connected instance of MongoClient, you can access any of the
# datbases within that Mongo server.
# To specify which database you actually want to use, access it as an attribute
# db = client.pymongo_test

# THIS CODE REMOVES DATABASE TO ENSURE WE WORK CLEANLY WITH EACH RUN
# Using PyMongo
client.drop_database('pymongo_test')

# Using MongoEngine
mongo_eng.drop_database('mongoengine_test')

# Or by dictionary_style access:
db = client['pymongo_test']

# It doesn't matter if the specified database has been created yet. By
# specifying this database name and saving data to it, you create the database
# automatically

# Inserting Documents
# Storing data is as easy as calling two lines of code:
# The first line specifies which collection to use.
posts = db.posts

# A collection is a group of documents that are stored together within the
# database. Collections and documents are akin to SQL tables and rows,
# respectively. Retrieving a collection is as easy as getting a database
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Roy'
}

# The second line is where you actually insert the data into the collection
# using the insert_one() method
result = posts.insert_one(post_data)
print(f'One post: {result.inserted_id}')  # One post: 5e150dcd1b5d8d5350bf6577

# We can even insert many documents at a time using insert_many(), which takes
# an array of document data
post_2 = {
    'title': 'Virtual Environments',
    'content': 'Use virtual environments, you guys',
    'author': 'Scott'
}

post_3 = {
    'title': 'Learning Python',
    'content': 'Learn Python, it is easy',
    'author': 'Bill'
}

new_result = posts.insert_many([post_2, post_3])
print(f'Multiple posts: {new_result.inserted_ids}')
# Multiple posts: [ObjectId('5e150dcd1b5d8d5350bf6578'),
# ObjectId('5e150dcd1b5d8d5350bf6579')]

# Retrieving Documents
# To retrieve a document, use the find_one() method, the argument it takes is
# a dictionary that contains fields to match. It can take other arguments.
#
# Retrieve the post that was written by Bill
bills_post = posts.find_one({'author': 'Bill'})
print(bills_post)
# {'_id': ObjectId('5e150b181b5d8d524ea862fa'), 'title': 'Learning Python',
# 'content': 'Learn Python, it is easy', 'author': 'Bill'}

# If we want to find more than one document, we can use find()
#
# Find all posts written by Scott
scotts_posts = posts.find({'author': 'Scott'})
print(scotts_posts)  # <pymongo.cursor.Cursor object at 0x10acd3910>

# Cursor object is iterable, just iterate to get each document
print("Scott's Posts:")
for post in scotts_posts:
    print(post)
# {'_id': ObjectId('5e1514051b5d8d5f43825f18'),
# 'title': 'Virtual Environments',
# 'content': 'Use virtual environments, you guys', 'author': 'Scott'}

# MONGOENGINE
# PyMongo can be a bit too low-level for many projects.
#
# One library that provides higher abstraction is MongoEngine. MongoEngine is
# an object document mapper (ODM), which is rougly equivalent to a SQL-based
# object relational mapper (ORM). The abstraction is class-based, so all models
# you create are classes.
#
# While other abstraction libraries exist, MongoEngine is one of the better
# ones as it has a mix of features, flexibility, and community support


# Defining a Document
# To set up our document object, we define what data we want our document
# object to have. Similar to many ORMs, we do this by subclassing the
# Document class and providing the types of data we want
class Post(Document):
    """
    A class used to represent a Post

    Parent: Document

    Attributes
    ----------
    title : str
        The title of a post
    content : str
        The content of the post
    author : str
        The author of the post
    published : str
        The date the post was published
    """
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    author = StringField(required=True, max_length=50)
    published = DateTimeField(default=datetime.datetime.now)


# NOTE: One of the more difficult tasks with database models is validating
#       data. How do you make sure that the data you're saving conforms to some
#       format you need? Just because a database is said to be schema-less
#       doesn't mean it is schema-free.

# The Document object uses the information in a Post instance to validate the
# data we provide it

# Saving Documents
# To save a document we use the save() method. If the document already exists
# in the database, then all the changes will be made on the atomic level to the
# existing document. If it doesn't exist, then it will be created.
post_4 = Post(
    title='Sample Post',
    content='Some engaging content',
    author='Scott'
)

post_4.save()  # This performs an insert
print(post_4.title)  # Sample Post
post_4.title = 'A Better Post Title'
post_4.save()  # This performs an atomic edit on "title"
print(post_4.title)  # A Better Post Title

# A few things about save():
# - PyMongo will perform validation when you call save(). This means it will
#   check the data you're saving against the schema you declared in the class.
#   If the schema (or constraint) is violated, an exception is thrown and the
#   data is not saved.
# - Since Mongo doesn't support true transactions, there is no way to "roll
#   back" the save() call like in SQL databases. Although you can get close to
#   performing transactions with two phase commits, they still don't support
#   rollbacks.

# Object Oriented Features
# With MongoEngine being object oriented, you can also add methods to your
# subclassed document.


# Referencing Other Documents
# You can use the ReferenceField object to create a reference from one document
# to another. MongoEngine handles the lazy de-referencing automatically upon
# access, which is more robust and less error-prone than having to remember to
# do it yourself everywhere in your code
# class Author(Document):
#     """
#     A class used to represent an Author
#
#     Parent: Document
#
#     Attributes
#     ----------
#     name : str
#         The name of the author
#     """
#     name = StringField(required=True, max_length=50)
#
#
# Post.objects.first().author.name
