drop table items;
drop table categories;


create table categories (
    id serial primary key,
    name varchar(100) not null, 
    description text
);

insert into categories (name, description) values 
    ('Electronics', 'Gadgets to make life easier'),
    ('Car Parts', 'Expensive stuff for the box with 4 wheels'),
    ('Sports', 'Get out and play!'),
    ('Video Games', 'Stay in and play!')
;

create table items(
    id serial primary key,

    name varchar(200) not null,
    description text not null,
    
    category_id integer not null,
    foreign key (category_id) references categories (id)
);

