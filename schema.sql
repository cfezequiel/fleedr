drop table if exists images;
create table images (
    id integer primary key autoincrement,
    nsid text not null,
    title text not null,
    url text not null,
    tags text not null,
    likes integer
);
