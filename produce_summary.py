def delivery( the_file):
        #prints everyline of the txt file
    for line in the_file:
        #it removed all the white spaces at the end
        line = line.rstrip();
        #converts it into an array
        words = line.split('|')
        #assigns variebles to items from array
        melon = words[0]
        count = words[1]
        amount = words[2]
        #prints output
        print(f"Delivered {count} {melon}s for total of ${amount}")    

for i in range(3):
    print(f'Day{i+1}')
    the_file = open(f'um-deliveries-day-{i+1}.txt')
    delivery(the_file)
    the_file.close()
   

