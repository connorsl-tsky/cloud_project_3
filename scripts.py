import socket

INPUT_DIR = "/home/data/"
OUTPUT_DIR = "/home/output/"

FILE_IF = "IF.txt"
FILE_ALWAYS = "AlwaysRememberUsThisWay.txt"


contractions = {
    "it's": "it is",
    "i'm": "i am",
    "can't": "cannot",
    "won't": "will not",
    "i'll": "i will",
    "don't": "do not",
    "you're": "you are",
    "that's": "that is"
}

def count_words(file):
    file.seek(0)
    count = 0
    for line in file:
        words = line.split(" ")
        count += len(words)
    return count

def word_frequency(file):
    file.seek(0)
    word_dict = {}
    for line in file:
        words = line.split(" ")
        for word in words:
            word = word.strip("\n,.;")
            word = word.lower()
            if word in contractions:
                results = contractions[word].split(" ")
                for word in results:
                    if word in word_dict:
                        word_dict[word] += 1
                    else:
                        word_dict[word] = 1
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    return word_dict

def most_frequent(word_dict):
    most_freq = {}
    s = sorted(word_dict, key=word_dict.get)
    for i in range(-3,0,1): # -3 -2 -1
        most_freq[s[i]] = word_dict[s[i]]
    return most_freq

def get_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip

def output(func, count_if, count_always, m_if, m_always, ip):
    func(f"Total words in IF: {count_if}\n")
    func(f"Total words in Always Remember Us This Way: {count_always}\n")
    func(f"Grand total words: {count_if+count_always}\n")
    func(f"Most frequent words in IF:\n")
    for word in m_if:
        func(f" - {word}: {m_if[word]}\n")
    func(f"Most frequent words in Always Remember Us this Way:\n")
    for word in m_always:
        func(f" - {word}: {m_always[word]}\n")
    func(f"IP: {ip}\n")

if __name__ == "__main__":
    with open(INPUT_DIR + FILE_ALWAYS, "r") as file:
        count_always = count_words(file)
        dict = word_frequency(file) 
        m_always = most_frequent(dict)
        
    with open(INPUT_DIR + FILE_IF, "r") as file:
        count_if = count_words(file)
        dict = word_frequency(file) 
        m_if = most_frequent(dict)

    ip = get_ip()

    with open(OUTPUT_DIR + "results.txt", "w") as file:
        output(file.write, count_if, count_always, m_if, m_always, ip)
    output(print, count_if, count_always, m_if, m_always, ip)
