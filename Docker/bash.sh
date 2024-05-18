mkdir solr_data

chmod -R 777 solr_data

docker run --name solr -d -p 9983:9983 --network main-network -v $(pwd)/solr_data:/var/solr solr

sleep 5

docker exec --user solr solr bin/solr create_core -c Digikala