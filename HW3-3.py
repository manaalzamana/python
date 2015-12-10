from datetime import datetime
def count_frequency(listofwords):
	return_dict={}
	for aword in listofwords:

		if aword in return_dict:

			return_dict[aword]=return_dict[aword]+1
		else:
			return_dict[aword]=1

	return return_dict

string_of_words="Found at  31 For millions of years flowers have been producing thorns. For millions of years sheep have been eating them all the same. And it's not serious, trying to understand why flowers go to such trouble to produce thorns that are good for nothing? It's not important, the war between the sheep and the flowers? It's no more serious and more important than the numbers that fat red gentleman is adding up? Suppose I happen to know a unique flower, one that exists nowhere in the world except on my planet, one that a little sheep can wipe out in a single bite one morning, just like that, without even realizing what he'd doing - that isn't important? If someone loves a flower of which just one example exists among all the millions and millions of stars, that's enough to make him happy when he looks at the stars. He tells himself 'My flower's up there somewhere...' But if the sheep eats the flower, then for him it's as if, suddenly, all the stars went out. And that isn't important?"


dt1 = datetime.now()
print("First Iteration : Quotes are stored in the string, the search uses 'in' keyword")
print("query:sheep and flower important")
print("Performing AND search for: {'sheep', 'important', 'flower'}")
if "sheep" in string_of_words and "important" in string_of_words and "flower" in string_of_words:
	pass
dt2= datetime.now()
print("Execution time:", dt2.microsecond-dt1.microsecond)
print("\n\n\n")


listofword=string_of_words.split(" ")
dt1 = datetime.now()
print("Second Iteration : Quotes are stored in the list, the search uses 'in' keyword")
print("query:sheep and flower important")
print("Performing AND search for: {'sheep', 'important', 'flower'}")
if "sheep" in listofword and "important" in listofword and "flower" in listofword:
	pass
dt2= datetime.now()
print("Execution time:", dt2.microsecond-dt1.microsecond)
print("\n\n\n")

dictionaryofword=count_frequency(string_of_words)
dt1 = datetime.now()
print("Second Iteration : Quotes are stored in the Dictionary, the search uses 'in' keyword")
print("query:sheep and flower important")
print("Performing AND search for: {'sheep', 'important', 'flower'}")
if "sheep" in dictionaryofword and "important" in dictionaryofword and "flower" in dictionaryofword:
	pass
dt2= datetime.now()
print("Execution time:", dt2.microsecond-dt1.microsecond)
print("\n\n\n")


print("Obeservation: List is faster than text search and dictionary is more fast")
