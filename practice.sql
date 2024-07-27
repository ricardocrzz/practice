--Altering Tables Many Examples

--Add a new column
ALTER TABLE tablename 
ADD columnname VARCHAR(8)

--Modify a column
ALTER TABLE tablename 
ALTER COLUMN columnname
SET
NOT NULL;

--Change name of a column
ALTER TABLE tablename 
RENAME COLUMN columnname 
TO newcolumnname;

--Drop a column
ALTER TABLE tablename 
DROP COLUMN columnname;

--rename table
alter table tablename
rename to newtablename;


--Create index based on a single column
CREATE INDEX transaction_id ON transaction(name)

--Create an index based on 2 columns
CREATE INDEX transaction_id_2 ON transaction(name, payment_type)

--Delete data in a table
TRUNCATE TABLE transaction

--delete value from a table
delete from mytable
where id = num;

--change type
alter table mytable
alter column mycolumn type
newtype;

--reset the serial id 
select setval('nameoftable_id_seq', (select max(id)
    from table));

SELECT sequence_name
FROM information_schema.sequences
WHERE sequence_schema = 'public';

--add two rows together
select first_name || ' ' || last_name as name
from table;

--join three tables
select so.id, si.quantity, i.price, (si.quantity * i.price) as total
from sales_item si
    join sales_order so on si.sales_order_id = so.id
    join item i on si.item_id = i.id
order by so.id;