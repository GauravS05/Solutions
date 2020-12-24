create database new;
use new;
create table user( User_Name varchar(20) Not Null default 'Unknown',Password varchar(20) Not Null);
create table Address(country varchar(50) Not Null,state varchar(50) Not Null, street varchar(50) Not Null,pincode int Not Null, Phone_no int Not Null);