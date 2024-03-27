/* Create the database */
CREATE DATABASE  IF NOT EXISTS frauds;

USE frauds;

/* Drop existing tables  */
DROP TABLE IF EXISTS fraudtrans;

/* Create the tables */
CREATE TABLE fraudtrans(
  transaction varchar(500)
);