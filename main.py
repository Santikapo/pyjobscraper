import pyppeteer as p
import re




validURL = "https://ca.indeed.com/viewjob"

service_endpoint = 'https://sheets.googleapis.com/v4/spreadsheets/'
spreadsheetID = '1lj46ctDNhFLfK4eaSs193DZqCwHxTcmo8k_HnKaRpwQ'    
ran = 'db!A1:B2'

def main():


    # main loop
    while True:
        # takes input
        inp = input("Paste Link or Type 1 for exit\n")

        # user exits
        if inp == "1":
            return

        # url check
        if re.search(validURL, inp) != None:


            print(service_endpoint + spreadsheetID + '/values/' + ran + ':append')




            print("URL Accepted")
        else:
            print("Invalid URL")





if __name__ == "__main__":
    main()