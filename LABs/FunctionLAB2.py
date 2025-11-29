







import random #allows the program to use the random number function


NUM_DICE_TO_ROLL = 5
SEED = 2183

# implement roll_dice() here!
def roll_dice(num_dice): #the vairabe is a placeholder
    dice_list = [] #it will hold all the values your dice function rolls
    for i in range(num_dice): #repeat this loop for everytime number of dice you have
        value = random.randint(1,6)
        dice_list.append(value)
    return dice_list


    
# implement most_repeats() here!
def most_reapeast(dice list):
  


def main():
    random.seed(SEED)
# implement remaining logic here!
if __name__ == "__main__":
main()