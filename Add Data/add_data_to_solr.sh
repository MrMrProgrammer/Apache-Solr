docker cp /home/user/Desktop/Apache Solr/Add Data/data.csv solr:/var/solr/data/Digikala/data.csv

docker exec --user solr solr post -c Digikala /var/solr/data/Digikala/data.csv