@@ -0,0 +1,12 @@
import search
import data_load
import indexer
import quotes


indexer.indexer()
search.search()
data_load.traverser()

n = indexer.indexer("raw_data.pickle")
search.search(n)
