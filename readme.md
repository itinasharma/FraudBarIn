![Alt text](view.jpeg?raw=true "Title")

## Clean up
###### docker stop $(docker ps -a -q)
###### docker rm $(docker ps -a -q)

## download code and run the containers
###### download code
###### download spark 2.4.8 from https://archive.apache.org/dist/spark/
###### update the location of spark in compose file "/Users/mubarak/Documents/Demos/spark248"
###### cd FruadAnalytics
###### docker-compose up

## run producer (on port 9000)
###### curl --header "Content-Type: application/json" --request POST --data '{"transaction":"123"}'  http://localhost:9000/add

## see messages in kafka
###### docker images ps
###### docker exec -it 1c31511ce206 bash
###### /* list all topics */
###### kafka-topics.sh --bootstrap-server localhost:9092 --list
###### /* read */
###### kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic my-topic -from-beginning
###### /* if you want to write directly */
###### kafka-console-producer.sh --broker-list localhost:9092 --topic my-topic
###### > '{"transaction":"234"}'
###### > '{"transaction":"456"}'
###### > ^c


## open zeppelin editor (on port 8080)
###### http://localhost:8080/

## configure Spark interpeter
###### org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.8 
###### mysql:mysql-connector-java:8.0.11

## run Spark job
###### copy job1.py code to the editor
###### run code

## check data in SQL
###### docker exec -it id /bin/bash
###### mysql -u[username] -p[password]
###### mysql -u[username] -p[password]
###### mysql> use FRAUDSDB;
###### mysql> select * from fraudtrans;


## see output in web App (on port 9000)
###### http://localhost:9000
###### configure llm key
###### run query "show all frauds"



