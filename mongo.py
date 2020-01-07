# This file demonstrates how to use Python to interface with MongoDB
import pymongo

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
# By default, the connection is established to the 'localhost' and
# 27017 port. Below is the customized version
client = MongoClient('localhost', 27017)

# Using the Mongo URI format:
# client = MongoClient('mongodb://localhost:27017')

# Accessing Databases
# Once you have a connected instance of MongoClient, you can access any of the
# datbases within that Mongo server.
# To specify which database you actually want to use, access it as an attribute
# db = client.pymongo_test

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
print(f'One post: {result.inserted_id}')
