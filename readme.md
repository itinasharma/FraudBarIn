![Alt text](view.jpeg?raw=true "Title")

## download code and run the containers
###### clone repo
###### cd FruadAnalytics
###### docker-compose up

## run producer (on port 9000)
###### curl --header "Content-Type: application/json" --request POST --data '{"transactionId":"123"}'  http://localhost:9000/add

## open zeppelin editor (on port 8080)
###### http://localhost:8080/

## configure Spark interpeter
###### org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.8 
###### mysql:mysql-connector-java:8.0.11

## run Spark job
###### copy job1.py code to the editor
###### run code

## see output in web App (on port 9000)
###### http://localhost:9000
###### configure llm key
###### run query "show all frauds"



