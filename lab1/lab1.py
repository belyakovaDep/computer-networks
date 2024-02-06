import subprocess
import csv

def call_the_request(request):
    calling_process = subprocess.run(request, capture_output=True, text=True, check=True, encoding='cp1251', errors="replace")
    result = calling_process.stdout

    return result

domens = ["google.com", "yandex.ru", "nsu.ru", "youtube.com", "classroom.google.com", "duolingo.ru", "twitch.tv", "ensv.dict.cc", "vcrdb.net", "tracker.gg"]


with open("domens_data.csv", "w", newline='') as f:
    writer = csv.writer(f, lineterminator="\n")

    for domen in domens:
        request = "ping " + domen
        result = call_the_request(request)
        result=result[1:len(result)-1]

        row = [domen, result]

        writer.writerow(row)