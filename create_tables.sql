create table Provider (
  id integer NOT NULL PRIMARY KEY,
  first_name varchar(50) NOT NULL,
  last_name varchar(50) NOT NULL,
  sex varchar(20) NOT NULL,
  birth_date date NOT NULL,
  rating numeric(3,1) NOT NULL,
  primary_skills varchar(300) NULL,
  secondary_skill varchar(300) NULL,
  company varchar(150) NULL,
  active boolean NOT NULL,
  country varchar(100),
  "language" varchar(50)
);

/*secondary tables if needed 
create table PrimarySkill (
	id int generated always as identity,
	providerId int not null,
	skill varchar(100) NOT NULL,
	constraint fk_provider foreign key(providerId) references Provider(id)
);

create table SecondarySkill (
	id int generated always as identity,
	providerId int not null,
	skill varchar(100) NOT NULL,
	constraint fk_provider foreign key(providerId) references Provider(id)
); */