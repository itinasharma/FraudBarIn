![Alt text](view.jpeg?raw=true "Title")

## download code and run the containers
###### clone repo
###### cd FruadAnalytics
###### docker-compose up

## run producer (on port 9000)
###### curl --header "Content-Type: application/json" --request POST --data '{"transactionId":"123"}'  http://localhost:9000/add

## see messages in kafka
###### docker images ps
###### docker exec -it 1c31511ce206 bash
###### /* list all topics */
###### kafka-topics.sh --bootstrap-server localhost:9092 --list
###### /* read */
###### kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic my-topic -from-beginning
###### /* if you want to write directly */
###### kafka-console-producer.sh --broker-list localhost:9092 --topic my-topic
###### > {“name":"Ronda Shepard", "email":"rondashepard@solaren.com"}
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
###### docker exec -t id /bin/bash
###### mysql -u[username] -p[password]
###### mysql> select * from fraudtrans


## see output in web App (on port 9000)
###### http://localhost:9000
###### configure llm key
###### run query "show all frauds"



