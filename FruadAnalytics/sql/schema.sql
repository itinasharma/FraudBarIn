/* Create the database */
CREATE DATABASE  IF NOT EXISTS FRAUDSDB;

USE FRAUDSDB;

/* Drop existing tables  */
DROP TABLE IF EXISTS fraudtrans;

/* Create the tables */
CREATE TABLE fraudtrans(
  transaction varchar(500)
);
