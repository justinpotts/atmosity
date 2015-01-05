drop table if exists entries;
create table entries (
	id integer primary key autoincrement,
	time_stamp text not null,
	temperature text not null,
	humidity text not null,
	pressure text not null
);
