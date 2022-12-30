import os, json


class Cve:
	def __init__(self, service):
		self.service = service

	
	# search CVEs with searchsploit and return a CVEs dictionary 
	def search_Cve(self) -> dict:
		os.system(f"searchsploit -j {self.service} >> $HOME/Documents/result_search_cve.json")
		file = open(f"$HOME/Documents/result_search_cve.json")
		dictionary_cve = json.loads(file.read())
		return dictionary_cve

	# control which CVE is valide
	def are_valide(self, cve_dictionary):
		pass
			



service = input("Inserisci servizio:\n")
cve = Cve(service)
cve_dictionary = cve.search_Cve()
print(cve_dictionary)

