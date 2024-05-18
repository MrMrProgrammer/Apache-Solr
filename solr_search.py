import pysolr

def SearchSolr(query):

    try:
        solr = pysolr.Solr('http://solr:8983/solr/Digikala', always_commit=True)

        result = solr.search(q=f"product_name:{query}", 
                        qf='product_name',
                        mm='2<-1 5<70%',
                        pf='product_name^10',
                        df='product_name', 
                        defType='edismax',
                        **{'q.op' : "or"})
        
        if len(result) == 0:
            return "No results found."
        
        else:    
            for i in result:
                product_id = i['product_id'][0]
                product_name = i['product_name'][0]

                print(f"{product_id} : {product_name}")

                return product_id, product_name
    
    except Exception as e:
        print(e)