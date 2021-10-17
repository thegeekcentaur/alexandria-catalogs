__author__ = 'archanda'
__date__ = '31-Mar-2021'
__copyright__ = "Copyright 2021"
__credits__ = ["archanda"]
__license__ = "All rights reserved"
__version__ = "0.1"
__maintainer__ = "archanda"
__email__ = "2020mt93064@wilp.bits-pilani.ac.in"
__status__ = "dev"

#Catalog APIs
create_catalog_url="/api/catalogs/local"
add_book_to_catalog_url="/api/catalogs/local/name/{catalog_name}/{book_id}"
update_books_to_catalog_url = "/api/catalogs/local/name/{catalog_name}/books"
delete_books_from_catalog_url = "/api/catalogs/local/name/{catalog_name}/books"
get_all_catalogs_of_user_url="/api/catalogs/local/name/{catalog_name}"
get_books_of_catalog_url="/api/catalogs/local/books"
delete_catalog_by_name_url="/api/catalogs/local/name/{catalog_name}"
get_all_catalogs_url="/api/catalogs/local/all"

