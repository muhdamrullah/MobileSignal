from subprocess import Popen, PIPE

def getIPfromMAC():
    command = ''' nmap -n -sP 192.168.1.0/24 | awk '/Nmap scan report/{printf $5;printf " ";getline;getline;print $3;}' '''
    (stdout, stderr) = Popen(command, stdout=PIPE, shell=True).communicate() #This command retrieves the table of IP/MAC from the nmap command


    your_search_word = raw_input("Enter a MAC Address: ")
    your_string = stdout
    list_of_words = your_string.split()
    next_word = list_of_words[list_of_words.index(your_search_word) - 1]
    print next_word

getIPfromMAC()
