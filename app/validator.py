from pathlib import Path
import json
import jsonschema
from jsonschema.validators import Draft202012Validator
from jsonschema.validators import RefResolver
from functools import partial


def _validate(object, schema, schema_index, resolver):
    jsonschema.validate(
        object,
        schema=schema_index[schema],
        cls=Draft202012Validator,
        resolver=resolver,
    )


with open("./schemas/_index.json") as schema_file:
    schema_index = json.load(schema_file)
resolver = RefResolver(Path().resolve().as_uri() + "/", True)

_validate = partial(_validate, schema_index=schema_index, resolver=resolver)

validate_author_in = partial(_validate, schema="AuthorIn")
validate_author_out = partial(_validate, schema="AuthorOut")
validate_author_partial = partial(_validate, schema="AuthorPartial")
validate_author_filter = partial(_validate, schema="AuthorFilter")

validate_book_in = partial(_validate, schema="BookIn")
validate_book_out = partial(_validate, schema="BookOut")
validate_book_partial = partial(_validate, schema="BookInPartial")
validate_book_filter = partial(_validate, schema="BookFilter")

validate_currency = partial(_validate, schema="Currency")

validate_integer_filter = partial(_validate, schema="IntegerFilter")
validate_regex_filter = partial(_validate, schema="RegexFilter")

validate_id = partial(_validate, schema="Id")

validate_isbn = partial(_validate, schema="ISBN")
validate_isbn10 = partial(_validate, schema="ISBN10")
validate_isbn13 = partial(_validate, schema="ISBN13")

validate_link = partial(_validate, schema="Link")

validate_page = partial(_validate, schema="Page")

validate_price = partial(_validate, schema="Price")

validate_publisher_in = partial(_validate, schema="PublisherIn")
validate_publisher_in = partial(_validate, schema="PublisherOut")
validate_publisher_in = partial(_validate, schema="PublisherPartial")
validate_publisher_in = partial(_validate, schema="PublisherFilter")

validate_year = partial(_validate, schema="Year")
