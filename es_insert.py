import glob,re
from pandas import read_csv
from elasticsearch import Elasticsearch


def es_insert(esindex,estype,filename,es_host=['localhost']):
    es = Elasticsearch(es_host)
    try:
        temp=es.search(index=esindex, doc_type=estype, size=0)
        id_start=temp['hits']['total'] + 1
    except:
        id_start=1
    df=read_csv(filename)
    df.columns =['TAG',"DATA"]
    df=df[df[df.columns[0]]!='\n'] # Clear rows with no data
    inserted =0
    for i in df.index:
        temp = df.loc[i].to_dict()
        temp['DATA'] = re.sub(' +',' ',temp['DATA']) #Clear multiple whitespaces with on space
        es.index(index=esindex, doc_type=estype, id=id_start, body=temp)
        id_start +=1
        inserted +=1
    return id_start - 1, inserted 

def es_delete(esindex,es_host=['localhost']):
    es = Elasticsearch(es_host)
    return es.indices.delete(index=esindex)

if __name__ == "__main__":
    import sys
    function = sys.argv[1]
    index= sys.argv[2]
    doc_type=sys.argv[3]
    if function.lower() =="delete":
        print(es_delete(index))
    elif function.lower()=="insert":
        for filename in sys.argv[4:]:
            tot_count,inserted = es_insert(index,doc_type,filename)
            print("{0} documents in index '{1}', doc_type '{2}'. {3} documents inserted from file: {4}'.".format(tot_count,index,doc_type,inserted,filename))
    else:
        print("function parameter must be either 'insert' or 'delete'")
