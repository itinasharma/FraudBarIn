![Alt text](view.jpeg?raw=true "Title")

## Clean up
stop all containers
###### docker stop $(docker ps -a -q)
remove all containers
###### docker rm $(docker ps -a -q)
delete producer image
###### docker rmi <id>
delete web image
###### docker rmi <id>

## download code and run the containers
###### download code
###### download spark 2.4.8 from https://archive.apache.org/dist/spark/
###### update the location of spark in compose file "/Users/mubarak/Documents/Demos/spark248"
###### cd FraudAnalytics
###### docker-compose up

## run producer (on port 9000)
###### curl --header "Content-Type: application/json" --request POST --data "{\"transaction\":\"123\"}" http://localhost:9000/add

## see messages in kafka
###### docker images ps
###### docker exec -it 1c31511ce206 bash
###### /* list all topics */
###### kafka-topics.sh --bootstrap-server localhost:9092 --list
###### /* read */
###### kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic my-topic -from-beginning
###### /* if you want to write directly */
###### kafka-console-producer.sh --broker-list localhost:9092 --topic my-topic
###### > {"transaction":"234"}
###### > {"transaction":"456"}
###### > ^c


## open zeppelin editor (on port 8080)
###### http://localhost:8080/

## configure Spark interpeter
###### org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.8 
###### mysql:mysql-connector-java:8.0.11

## in zeppelin editor install mysql connector 
###### %sh
###### pip install mysql-connector-python

## run Spark job
###### copy StreamJob.py code to the editor
###### run code

## check data in SQL
###### docker exec -it id /bin/bash
###### mysql -u[username] -p[password]
###### mysql -uroot -pabc
###### mysql> use FRAUDSDB;
###### mysql> select * from fraudtrans;


## see output in web App (on port 8000)
###### http://localhost:8000
###### configure llm key
###### run query "show all frauds"

## data
###### https://www.kaggle.com/datasets/devondev/financial-anomaly-data/data
###### https://www.kaggle.com/datasets/mohammadbolandraftar/my-dataset/data?select=Clickstream+dataset.csv
###### https://www.kaggle.com/code/turkayavci/fraud-detection-on-bank-payments/input?select=bsNET140513_032310.csv
###### https://www.kaggle.com/code/turkayavci/fraud-detection-on-bank-payments/notebook
###### https://github.com/atavci/fraud-detection-on-banksim-data/blob/master/Fraud%20Detection%20on%20Bank%20Payments.ipynb

## reference
###### https://github.com/tankwin08/PySpark_Fraud_detection_ML/blob/master/pyspark_RF_fraud_detection.ipynb
###### https://www.linkedin.com/pulse/build-machine-learning-model-detect-fraudulent-using-mich-rkxje/
###### http://umu.diva-portal.org/smash/get/diva2:1772824/FULLTEXT01.pdf
