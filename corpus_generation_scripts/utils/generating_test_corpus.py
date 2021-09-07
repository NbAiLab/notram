## Generates sharded corpus test files 
## When done just run 'gzip *.json'

num_shards = 5
final_shard = f"{num_shards:04d}"

for shard in range(1,num_shards+1):
    this_shard = f"{shard:04d}"
    corpus_file_name = "test_corpus_train-shard-"+this_shard+"-of-"+final_shard+".json"

    with open(corpus_file_name,'w') as f:
        for n in range(1,10001):
            jsonline = "{\"id\": \"doc_"+str(this_shard)+"_"+str(n)+"\", \"text\": \"This is line #"+str(n)+" of shard "+this_shard+" of "+final_shard+". Testing 123 æøåÆØÅ.\"}\n"
            f.write(jsonline)


