# -*- coding: utf-8 -*-
import sys
import numpy
import time
# from hanger import function

def main():

	from signal import signal, SIGPIPE, SIG_DFL 
	# #Ignore SIG_PIPE and don't throw exceptions on it... (http://docs.python.org/library/signal.html)
	signal(SIGPIPE,SIG_DFL) 
	
	
	print "HAPPY BIRTHDAY CHIWA!"
	print "do you want to input your stats? [y/n]"
	stats = raw_input()
	print "\n\n"
	if stats.lower() == "y":

		print "How old are you?",
		age = raw_input()
		print "How tall are you?",
		height = raw_input()
		print "How much do you weigh? (lbs)",
		weight = raw_input()
		STweight = float(weight) * 0.0714286
		STweight = round(STweight , 2)
		
		print "\n\n\nSo, you're %r years old today!, %r tall and weigh %r stones." % (age, height, STweight)
		print "\nSO CUTE!"
		
	
	elif stats.lower() == "n" :
		return lolz()


	elif stats == "abcd" :
		return secret()

		

	else :
		return lolz()
	
	return ""



def Dingo():
	print "HAPPY BIRTHDAY!!!"
	print "put in the correct value [y/n]!!!"

	# print "guess the word\n"
	print "\nhint: the answer is 'y' "

def testone(): 
	import hanger
	from hanger import function
	print hanger.function()

def snapshot():
	import screener
	# print screener.snap()
	print screener



def instructions():
	print "instructions: press 'q' when you are feelin flashy"
	time.sleep(3)
	print "3\n"
	time.sleep(1)
	print "2\n"
	time.sleep(1)
	print "1\n"
	time.sleep(1)


def codebreaker():
	solution = ''' TOP SECRET

	48657920436869776121204920686f706520796f7
	52068616420612067726561742064617920746f6461792e2049207
	76173206e6f742073757265207768617420746f206d616b6520736
	f204920646964207468697320746f6f2068616861682e204966207
	96f7520676f74207468726f75676820697420616c6c20746861742
	06d65616e7320796f7520617265206120736d61727420636f6f6b6
	9652120452e672e2063686f636f6c6174652063686970206f72207
	36f6d657468696e672028706864292e200d0a0d0a416c736f20686
	f706520796f75206761696e65642061206c6f74206f66206e65772
	06b6e6f776c6564676520616e642068617665206c6561726e65642
	061206c6f7420696e207363686f6f6c2c20657370656369616c6c7
	920746865206f6e65207769746820796f757220627269746973682
	074656163686572207468617420796f75206c696b6520616168616
	8612e204d6179626520796f752063616e2066696e6420736f6d657
	468696e67209373776565749420746f20757365207468652067696
	67420666f72850d0a0d0a0d0a6168616861680d0a4f74686572207
	468616e20746861742c204b6565702075702074686520676f6f642
	0776f726b20616e64206b656570206265696e67206368656573792
	e20546865726520617265206d616e79206772756d7079207365726
	96f75732070656f706c652c20736f2069747320676f6f642074686
	57265206172652070656f706c65206c696b6520796f7520746f206
	b6565702074686520776f726c6420696e2062616c616e6365206c6
	f6c2e205374727567676c65206973207265616c2c207372732e200
	d0a496e206f74686572206e6577732c20746f64617920697320796
	f757220626972746864617920736f20686176652066756e210d0a0
	d0a4c6f766520796f752c200d0a2d4d6178696d696c61696e200d0
	a 

	'''
	print solution 

	print "\ncontinue? 'y/n'"
	answer = raw_input()

	if answer.lower() == 'y':
		print "you did it!"
		time.sleep(3)
		print heart()
		# wtf is up with this
		time.sleep(1)
		return 0
	elif answer.lower() == 'n':
		print lolz()





def testtwo():

	text = '''

	uoy llet t'now eh KJ-

	dneirfyob ruoy ksa-

	).cte drow ,regetni( esnes lanoitidart eht ni ton tub ,eulav fo redloh a ma I-

	"___ hanoJ" dellac mlif elbirret a ni ma I-

	kroy-wen ot dedulcni serutaef gub htiw yot a tnes uoy-

	elohw...ton ma I esuaceb ,das ma I semitemos-

	tcaf modnar a ma I-

	xis fo esab a ma I-

	:stnih emos era ereH



	tniop tellub tsal ot dnoces eht fo drow tsal eht rebmemer .dnuof ecno tub ,kees uoy hcihw ot melborp eht ot rewsna eht
	'''

	
	print "\n\n\ncan you solve this puzzle?\n\n\n"

	print text 

	print "hint: you have done this before"
	print "\nonce you have the answer type in the code here:"
	answer = raw_input()

	if answer.lower() == 'boyfriend':
		print "well done, on we go"
		# break
	else:
		print "\n\noh snap!\n"
		time.sleep(1)
		print "you done messed up!\n"
		time.sleep(1) 
		print lose()

def lose():
	print '''

 _____                        _____                
|  __ \                      |  _  |               
| |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __ 
| | __ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
| |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |   
 \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|   
                                                  Maximilian has won!

                       u mad?                                 
	'''
	time.sleep(4)

	sys.exit("beep! errors! QQ + rage bye!")
	time.sleep(4)



def secret():
	print "holy shit you found the secret!"


def lolz():
	print "WRONG INPUT LOL \n\n\n"
	print "YOLOOO"
	print "FREEBASEDGOD"
	print "FREEBASEDGOD"
	print "FREEBASEDGOD"
	print "FREEBASEDGOD"
	print "YOLOOO"
	print "#hashtag#omg\n\n"
	time.sleep(3)
	print lose()
	time.sleep(3)

# here is all the art and stuff
# here is all the art and stuff
# here is all the art and stuff


def heart():

	heart = '''
	         MMMMMMMMM                         MMMMMMMMM
          MMMMMMMMMMMMMMMMMM               MMMMMMMMMMMMMMMMMM
       MMMMMMMXXXXXXXXXXMMMMMMM         MMMMMMMXXXXXXXXXXMMMMMMM
    MMMMMMXXXXXXXXXXXXXXXXXMMMMMM     MMMMMMXXXXXXXXXXXXXXXXXMMMMMM
   MMMMMXXXXXXXXOOOOOOOOXXXXXXMMMM   MMMMXXXXXXOOOOOOOOXXXXXXXXMMMMM
  MMMMXXXXXXXOOOOOOOOOOOOOOOXXXXMMM MMMXXXXOOOOOOOOOOOOOOOXXXXXXXMMMM
 MMMMXXXXXXOOOOOOOOOOOOOOOOOOOOXXXMMMXXXOOOOOOOOOOOOOOOOOOOOXXXXXXMMMM
 MMMXXXXXOOOOOOOOOOOOOOOOOOOOOOOOXXXXXOOOOOOOOOOOOOOOOOOOOOOOOXXXXXMMM
MMMXXXXXOOOOOOOOOOO       OOOOOOOOOXOOOOOOOOO       OOOOOOOOOOOOXXXXMMM
MMMXXXXOOOOOOOOO              OOOOOOOOOOO              OOOOOOOOOOXXXMMM
MMMXXXXOOOOOOOO                  OOOOO                  OOOOOOOOOXXXMMM
MMMXXXXOOOOOOO    H A P P Y        O        H A P P Y    OOOOOOOOXXXMMM
MMMXXXXOOOOOOO                                           OOOOOOOOXXXMMM
MMMXXXXOOOOOOO               B I R T H D A Y             OOOOOOOOXXXMMM
MMMXXXXXOOOOOO                                           OOOOOOOXXXXMMM
 MMMXXXXOOOOOOO                                         OOOOOOOOXXXMMM
 MMMMXXXXOOOOOOO                                       OOOOOOOOXXXMMMM
  MMMXXXXOOOOOOOOO                                    OOOOOOOOOXXXMMM
  MMMMXXXXOOOOOOOOOO                                OOOOOOOOOOXXXMMMM
   MMMXXXXXOOOOOOOOOOO                           OOOOOOOOOOOOXXXXMMM
    MMMXXXXXOOOOOOOOOOOOO                     OOOOOOOOOOOOOOXXXXMMM
     MMMXXXXXOOOOOOOOOOOOOOO               OOOOOOOOOOOOOOOOXXXXMMM
      MMMXXXXXOOOOOOOOOOOOOOOOO         OOOOOOOOOOOOOOOOOXXXXXMMM
       MMMXXXXXXOOOOOOOOOOOOOOOOOO   OOOOOOOOOOOOOOOOOOXXXXXXMMM
         MMMXXXXXXXOOOOOOOOOOOOOOOO OOOOOOOOOOOOOOOOXXXXXXXMMM
           MMMXXXXXXXXOOOOOOOOOOOOOOOOOOOOOOOOOOOXXXXXXXXMMM
             MMMMXXXXXXXXXOOOOOOOOOOOOOOOOOOOXXXXXXXXXMMMM
                MMMMXXXXXXXXXXXOOOOOOOOOXXXXXXXXXXMMMMM
                   MMMMMXXXXXXXXXXXOXXXXXXXXXXXMMMMM
                      MMMMMMXXXXXXXXXXXXXXXMMMMMM
                          MMMMMMXXXXXXXMMMMMM
                              MMMMMXMMMMM
                                 MMMMM
                                  MMM
                                   M

                                   '''
	print heart                                   
                                   



def endo():
	doodle = """
	██╗  ██╗ █████╗ ██████╗ ██████╗ ██╗   ██╗                       
	██║  ██║██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝                       
	███████║███████║██████╔╝██████╔╝ ╚████╔╝                        
	██╔══██║██╔══██║██╔═══╝ ██╔═══╝   ╚██╔╝                         
	██║  ██║██║  ██║██║     ██║        ██║                          
	╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝        ╚═╝                          
	                                                                
	██████╗ ██╗██████╗ ████████╗██╗  ██╗██████╗  █████╗ ██╗   ██╗██╗
	██╔══██╗██║██╔══██╗╚══██╔══╝██║  ██║██╔══██╗██╔══██╗╚██╗ ██╔╝██║
	██████╔╝██║██████╔╝   ██║   ███████║██║  ██║███████║ ╚████╔╝ ██║
	██╔══██╗██║██╔══██╗   ██║   ██╔══██║██║  ██║██╔══██║  ╚██╔╝  ╚═╝
	██████╔╝██║██║  ██║   ██║   ██║  ██║██████╔╝██║  ██║   ██║   ██╗
	╚═════╝ ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝

	╔╦╗╔═╗  ╔═╗╔═╗╔═╗╦ ╦╦╔═╗┬  
	 ║ ║ ║  ╚═╗║ ║╠═╝╠═╣║╠═╣│  from maximilian
	 ╩ ╚═╝  ╚═╝╚═╝╩  ╩ ╩╩╩ ╩o
	"""
	print doodle                                                             






# THIS IS THE START OF THE PROGRAM EXECUTION
# ===================

print ''' 

 __ _             _     _____          _   
/ _\ |_ __ _ _ __| |_  /__   \___  ___| |_ 
\ \| __/ _` | '__| __|   / /\/ _ \/ __| __|
_\ \ || (_| | |  | |_   / / |  __/\__ \ |_ 
\__/\__\__,_|_|   \__|  \/   \___||___/\__|
                                           
                                           '''

print main()
print '''
 _                _   _ 
| | _____   _____| | / |
| |/ _ \ \ / / _ \ | | |
| |  __/\ V /  __/ | | |
|_|\___| \_/ \___|_| |_|
'''

print testone()
print '''
 _                _   ____  
| | _____   _____| | |___ \ 
| |/ _ \ \ / / _ \ |   __) |
| |  __/\ V /  __/ |  / __/ 
|_|\___| \_/ \___|_| |_____|
                            
                           '''
print testtwo()
print ''' 
 _                _   _____ 
| | _____   _____| | |___ / 
| |/ _ \ \ / / _ \ |   |_ \ 
| |  __/\ V /  __/ |  ___) |
|_|\___| \_/ \___|_| |____/ 
                            '''

print codebreaker()

print instructions()
print snapshot()

# print endo() 

# ======================
# make this only at the ending 



print "congrats! you won!"
print '''

 _____ _                 _                          
/__   \ |__   __ _ _ __ | | __ /\_/\___  _   _      
  / /\/ '_ \ / _` | '_ \| |/ / \_ _/ _ \| | | |     
 / /  | | | | (_| | | | |   <   / \ (_) | |_| |     
 \/   |_| |_|\__,_|_| |_|_|\_\  \_/\___/ \__,_|     
                                                    
  __                    _             _             
 / _| ___  _ __   _ __ | | __ _ _   _(_)_ __   __ _ 
| |_ / _ \| '__| | '_ \| |/ _` | | | | | '_ \ / _` |
|  _| (_) | |    | |_) | | (_| | |_| | | | | | (_| |
|_|  \___/|_|    | .__/|_|\__,_|\__, |_|_| |_|\__, |
                 |_|            |___/         |___/ 
                 '''
print endo()







# add a puzzle where she converts hex or something to get the secret code input then do other tasks
# add a puzzle where she converts hex or something to get the secret code input then do other tasks



# add a way to make the program run this script as well as a gui of a timer or something that takes a screenshot of dingo
# os.system("screencapture screen.png") 


# thats for a literal screen capture

# add screenshot functionallity








