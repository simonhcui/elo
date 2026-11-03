import os

directory = 'C:\\Users\\cui\\Desktop\\buylist'
buylists = []

for filename in os.listdir(directory):
    if(".txt" in filename):   
        buylists.append(filename)


final_list = open("final_list.csv", "w")
total_count = open("total_count.csv", "w")
token_list = open("tokens.csv", "w")


# buylist is organized by sets
# buylist[set_a] : card_condition : [num, price]

buylist = {}

def process_buylist(b_list):
    b_list_file = open(b_list, "r")
    current_set = ""

    for line in b_list_file:
        if(len(line) <= 3):
           continue
        
        if("$" not in line):
            current_set = line.strip()

            if(current_set not in buylist):
                buylist[current_set] = {}
            
        else:
            card_info = line.split("\t")
            card_name = card_info[0][:-1]
            card_quantity = card_info[1].split()[0]
            card_quality = card_info[1].split()[1]
            card_price = card_info[1].split()[3]

            full_card_name = card_name + "_" + card_quality
            
            if(full_card_name not in buylist[current_set]):
                buylist[current_set][full_card_name] = [card_quantity, card_price[1:]] 
            else:
                previous_amount = buylist[current_set][full_card_name][0]
                new_amount = int(previous_amount) + int(card_quantity)
                buylist[current_set][full_card_name] = [str(new_amount), card_price[1:]] 

    b_list_file.close()


def main():

    for buy_list in buylists:
        process_buylist(buy_list)

    for key, value in sorted(buylist.items(), key=lambda x: x[0]): 
        print("{} : {}".format(key, value))

        for key_2, value_2 in sorted(buylist[key].items(), key=lambda x: x[0]):
            final_list.write(key + "," + key_2.replace(",", "") + "," + value_2[0] + "," + value_2[1] + "\n")
        
    final_list.close()

    for key, value in sorted(buylist.items(), key=lambda x: x[0]): 
        print("{} : {}".format(key, len(buylist[key])))
        total_count.write(key + "," + str(len(buylist[key])) + "\n")

    for key, value in sorted(buylist.items(), key=lambda x: x[0]):
        for key_2, value_2 in sorted(buylist[key].items(), key=lambda x: x[0]):
            if("Token" in key_2):
                token_list.write(key + "," + key_2.replace(",", "") + "," + value_2[0] + "," + value_2[1] + "\n")
        

if __name__ == "__main__":
    main()
