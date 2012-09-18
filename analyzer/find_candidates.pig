%declare INPUT_DIR 'data'

raw_readers = LOAD '$INPUT_DIR/reader.*.csv' USING PigStorage(',', '-tagsource') AS (source:chararray, book_id:int);
readers = FOREACH (FILTER raw_readers BY book_id > 0) GENERATE STRSPLIT(source, '\\.', 3).$1 AS reader_id, book_id;

/* load books
raw_books = LOAD '$INPUT_DIR/book.*.csv' USING PigStorage(',', '-tagsource') AS (source:chararray, reader_id:chararray);
books = FOREACH (FILTER raw_books BY reader_id != 'ID') GENERATE (int) STRSPLIT(source, '\\.', 3).$1 AS book_id, reader_id;
*/

/* find most read books
book_reading_grouped = GROUP books BY book_id;
book_reading_counts = FOREACH book_reading_grouped GENERATE group, COUNT(books) AS readings;
book_reading_counts_ordered = LIMIT (ORDER book_reading_counts BY readings DESC) 10;
DUMP book_reading_counts_ordered;
*/

good_books = LOAD 'good_books.csv' USING PigStorage(',') AS (book_id:int, book_title:chararray);
good_book_readings = JOIN readers BY book_id, good_books BY book_id;
good_book_reading_grouped = GROUP good_book_readings BY reader_id;
good_book_reading_counts = FOREACH good_book_reading_grouped GENERATE group, COUNT(good_book_readings) AS read_good_books;
top_readers = LIMIT (ORDER good_book_reading_counts BY read_good_books DESC) 20;
DUMP top_readers;
