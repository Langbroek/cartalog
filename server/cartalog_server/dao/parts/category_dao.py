from beartype import beartype

from cartalog_server.dao import database_connection, Cursor, NoneCursor
from cartalog_server.domain import DomainCategory

class CategoryDAO:

  @staticmethod
  @beartype
  @database_connection(commit=True)
  def insert_category(category: DomainCategory, db: Cursor = NoneCursor()) -> DomainCategory:
    """ Insert a new category into the database.  """
    db.execute('INSERT INTO part_categories (name, description) VALUES (?, ?)', 
               (category.name, category.description))
    return category.new(uid=db.lastrowid)