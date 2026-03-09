from fret_map import fret_map

def generate_tabs(sequence):

    tabs=["E| ","A| ","D| ","G| ","B| ","e| "]
    
    for note in sequence:
        for index,line in enumerate(tabs):
            
            if(note[0]==index): tabs[index]+= f"{note[1]:02d}-"
            else: tabs[index]+= "---"
    tabs.reverse()
    return tabs

if(__name__=="__main__"):
    sequence = [
        (5,8),
        (4,10),
        (3,9),
        (2,10),
        (1,12)
    ]
    tabs=generate_tabs(sequence)
    for line in tabs:
        print(line)