                     #code simple calculator
import cmath #complex math
import math
from spellchecker import SpellChecker
from colorama import Fore, Style, init
init(autoreset=True)

# color

def success_print(text):
    print(Fore.GREEN + text)

def error_print(text):
    print(Fore.RED + Style.BRIGHT + text)

def menu_print(text):
    print(Fore.YELLOW + text)


#description or main code:

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y
   
def squareroot(x):
    if x < 0:
        return "Error! can't find sqrt of negative number"
    else:
        return x**0.5

def square(x):
    return x**2

def cube(x):
    return x**3

def power(x, y):
    return x ** y

def percentage(x, y):
    if y == 0:
        return "Error! can't find percentae of 0"
    else:
        return (y/100)*x

def cos(x):
    return math.cos(math.radians(x))

def sin(x):
    return math.sin(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def natural_log(x):
    if x <= 0:
        return "Error! log only works for positive numbers"
    else:
        return math.log(x)

def base10_log(x):
    if x <= 0:
        return "Error log base 10 only works on positive numbers"
    else:
        return math.log10(x)

def custom_base_log(x, base):
    if x <= 0:
        return "Error log only works on positive numbers"
    else:
        return math.log(x)/math.log(base)

def circle_area(radius):
    return math.pi*radius**2

def circle_circumference(radius):
    return 2*math.pi*radius

def pythagorean_theorem(x, y):
    return (x**2+y**2)**0.5

def pythagorean_theorem2(x, y):
    return (x**2+y**2)

def quadratic_formula(x, y, z):
    if x == 0:
        return "It is no longer a quadratic equation.\n Deu to a = 0 [ax^2 + bx + c = 0]"
    else:
        d = y**2 - 4*x*z
        if d < 0:
            x1 = (-y + cmath.sqrt(d)) / (2*x)
            x2 = (-y - cmath.sqrt(d)) / (2*x)
            return x1, x2
        if d > 0:
            x1 = (-y + math.sqrt(d)) / (2*x)
            x2 = (-y - math.sqrt(d)) / (2*x)
            return x1, x2
        if d == 0:
            x1 = -y / (2*x)
            return x1

# safe input:
def Afloat(prompt):
    while True:
        try:
            return float(input(Fore.CYAN + prompt))
        except ValueError:
            error_print("Oops, that needs to be a number. Try again:")

def Bint(prompt):
    while True:
        try:
            return int(input(Fore.CYAN + prompt))
        except ValueError:
            error_print("Whole numbers only. Try again:")
        

#main menu:

print(Fore.CYAN + Style.BRIGHT + "------------------------<Simple Calculator>-------------------------")
menu_print("1. Addition")
menu_print("2. Subtraction")
menu_print("3. Multiplication")
menu_print("4. Division")
menu_print("5. Squareroot")
menu_print("6. Square")
menu_print("7. Cube")
menu_print("8. Power")
menu_print("9. Percentage")
menu_print("10. Cosine")
menu_print("11. Sine")
menu_print("12. Tangent")
menu_print("13. Multiplication Table")
menu_print("14. Natural Logarithm (ln)")
menu_print("15. Base-10 Logarithm (log)")
menu_print("16. Custom Base Logarithm")
menu_print("17. area of a circle")
menu_print("18. circumference of a circle")
menu_print("19. Pythagorean theorem")
menu_print("20. Quadratic equation")
print(Fore.MAGENTA + "\nif you want to learn more about this calculator; type \"information\" in the choice section. If you want to exit then type \"exit\" in the choice.\n")

#Perform main Calculation:

while True:
    
    choice = input(Fore.CYAN + "Enter your choice (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20):")

    if choice in ('1','2','3','4'):
        num1 = Afloat("Enter first number: ")
        num2 = Afloat("Enter second number: ")
        if choice == '1':
            success_print(f"\n{num1} + {num2} = {add(num1,num2)}\n")

        elif choice == '2':
            success_print(f"\n{num1} - {num2} = {subtract(num1,num2)}\n")

        elif choice == '3':
            success_print(f"\n{num1} X {num2} = {multiply(num1,num2)}\n")

        elif choice == '4':
            result = divide(num1,num2)
            if isinstance(result, str):
                error_print(f"\n{num1} / {num2} = {result}\n")
            else:
                success_print(f"\n{num1} / {num2} = {result}\n")

                #Perform other Calculation:

    elif choice in ('5','6','7'):
        num3 = Bint("Enter the number: ")
        if choice == '5':
            result = squareroot(num3)
            if isinstance(result, str):
                error_print(f"\n{result}\n")
            else:
                success_print(f"\n√{num3} = {squareroot(num3)}\n")

        elif choice == '6':
            success_print(f"\n{num3}^2 = {square(num3)}\n")

        elif choice == '7':
            success_print(f"\n{num3}^3 = {cube(num3)}\n")

         #Perform Power: 
        
    elif choice == '8':
            num4 = Bint("Enter the base : ")
            num5 = Bint("Enter the index: ")
            success_print(f"\n{num4}^{num5} = {power(num4, num5)}\n")

        #Perform Percentage:

    elif choice == '9':
            num6 = Bint("Enter the part(%) : ")
            num7 = Afloat("Enter the whole : ")
            result = percentage(num6, num7)
            if isinstance(result, str):
                error_print(f"\n{result}\n")
            else:
                success_print(f"\n{num6}% out of {num7} is({result}%)\n")

         #Perform trigonometric:

    elif choice in ('10','11','12'):
        num8 = Bint("Enter the number:")
        if choice == '10':
            success_print(f"\ncos({num8}) = {cos(num8)}\n")
            
        elif choice == '11':
            success_print(f"\nsin({num8}) = {sin(num8)}\n")

        elif choice == '12':
            success_print(f"\ntan({num8}) = {tan(num8)}\n")

        #Do Multiplication Table:

    elif choice == '13':
        num9 = Bint("Enter the number:")
        num10 = Bint("upto:")
        for i in range(1,num10+1):
            ans = num9*i
            success_print(f"{num9} X {i} = {ans}")

            #Do logarithm:

    elif choice in ('14','15'):
        num11 = Afloat("Enter the number:")
        if choice == '14':
            result = natural_log(num11)
            if isinstance(result, str):
                error_print(f"\n{result}\n")
            else:
                success_print(f"\nln({num11}) = {result} \n")

        elif choice == '15':
            result = base10_log(num11)
            if isinstance(result, str):
                error_print(f"\n{result}\n")
            else:
                sucess_print(f"\nlog10({num11}) =  {result} \n")

    elif choice == '16':
        num12 = Afloat("Enter the number:")
        base = Afloat("Enter the base:")
        result = custom_base_log(num12, base)
        if isinstance(result, str):
            error_print(f"\n{result}\n")
        else:
            success_print(f"\nlog{base}({num12}) = {result}\n")

         #pi
           
    elif choice in ('17','18'):
        num13 = Bint("Enter the radius:")
        if choice == '17':
            success_print(f"\nπ{num13}^2 = {circle_area(num13)}\n")
        elif choice == '18':
            success_print(f"\n2π{num13} = {circle_circumference(num13)}\n")
            
        #Perform pythagorean theoram:
          
    elif choice == '19':
        print(Fore.YELLOW + "\n1. Find the Hypotenuse")
        print(Fore.YELLOW + "2. find the squre of Hypotenuse\n")
        choice2 = input(Fore.CYAN + "Enter your choice(1/2):")
        if choice2 == '1':
             num14 = Bint(Fore.GREEN + "Enter the base:")
             num15 = Bint(Fore.GREEN + "Enter the altitude:")
             success_print(f"\nHypotenuse = √{num14}^2 + {num15}^2 = {pythagorean_theorem(num14, num15)}\n")
        elif choice2 == '2':
            num16 = Bint(Fore.GREEN + "Enter the base:")
            num17 = Bint(Fore.GREEN + "Enter the altitude:")
            print(f"\n Sqare of Hypotenuse = {num16}^2 + {num17}^2 = {pythagorean_theorem2(num16, num17)}\n")
        else:
            print(Fore.RED + "\nInvalid choice\n")

    elif choice == '20':
            num18 = Bint("Enter the first number:")
            num19 = Bint("Enter the second number:")
            num20 = Bint("Enter the third number:")
            success_print(f'''\n {num18}X^2 + {num19}X + {num20} = 0

                    X = {quadratic_formula(num18, num19, num20)}''')

    
           
        #Information about the calculator

    elif choice == 'information':
        print(Fore.RED + Style.BRIGHT + '''\n
                      Dear sir,
                           this calculator runs on \"python\".
                           It was made on (16/02/2025). 
                           It is made for doing calculation.
                           
                           For now it can do:-
                           1. Addition
                           2. Subtraction
                           3. Multiplication
                           4. Division
                           5. Squareroot
                           6. Square
                           7. Cube
                           8. Power
                           9. Percentage
                           10. Cosine
                           11. Sine
                           12. Tangent
                           13. Multiplication Table
                           14. Natural Logarithm (ln)
                           17. area of a circle
                           18. circumference of a circle
                           19. Pythagorean theoram
                           20. Quadratic equation


                                     The updates on this calculator might
                                     take some time to come.
                                     But soon it will be capable of
                                     doing more complex calculations.
                                     And also it can run a preadded
                                     game in choice type 'game'.
                                     For more cool easter eggs type bunny, dog,
                                     coffee, pc.
                                     or want help in your spelling mistakes
                                     then type "spell corrector" (I dont know
                                     why would a calculator needs this but ok.)

                                                   Thank you for reding.

                                                   If you want to continue
                                                   please type \"yes\".

                    Last updated:
                    (6/05/2026)
                                                   \n''')
    elif choice in ["hi","Hi","hello","Hello","whats up"]:
        print(Fore.MAGENTA + '''\n
                    Hello user iam a very simple chat bot.
                    my name is **#@@$*. I cant answer like
                    the other AI I am just here for no reason.
                    If you want to learn about this caculator,
                    just type information in the choice sectioin.
                    Thankyou bye.\n''')
    elif choice in ["how are you", "How are you", "can you feel anything"]:
        print(Fore.MAGENTA + '''\n
                    My programing dosent have the word feeling so
                    i dont know.\n''')
    elif choice in ["what are you", "what is your porpouse"]:
        print(Fore.MAGENTA + '''\n
                   I am just a python script. nothing more....
                   .......[{(W#*H+=-A-_^T%$@A*()M#@%I!)}]

                    I am a calculator select the choice and
                    see the calculations''')
    elif choice in ["what is python", "python"]:
        print(Fore.MAGENTA + Style.BRIGHT + '''\n
                   Python is a popular, high-level, and versatile programming language known for its
                   simple syntax, making it easy to learn. It is used for a wide range of applications,
                   including web development, data science, artificial intelligence, automation, and
                   software development.

                   Key features:-
                   ^^^^^^^^^^^^
                   High-level and interpreted: Python is a high-level language, which means it is
                                                more abstract from computer hardware, and interpreted, meaning it is executed
                                               line by line without a separate compilation step. This makes the development cycle faster. 

                   Beginner-friendly: Its clean and readable syntax makes it one of the most beginner-friendly languages available. 

                   Versatile: Python is a general-purpose language used across many different fields, from web
                              applications and data analysis to AI and scientific computing. 

                   Large standard library: It comes with a vast standard library and supports a wide range of
                                           third-party libraries and frameworks, which saves developers from
                                           building everything from scratch

                   Open-source: Python is free to use and distribute, even for commercial purposes, and is
                                developed under an OSI-approved open-source license. 


                   Common uses:-
                   ^^^^^^^^^^^
                   Web Development: Used to build websites and web applications, often with frameworks like Django. 

                   Data Science and AI: A dominant language in machine learning and artificial intelligence due to
                                       its extensive libraries for data analysis and model training. 

                   Automation: Used to automate repetitive tasks, such as scripting and connecting different software components. 

                   Software Development: Used for building software, managing bugs, and automating testing processes.\n''')

    elif choice in ["give me your code", "what script do you follow"]:
        print(Fore.MAGENTA + '''\n
                   I Follow
                           [                     #code simple calculator


error --{S#O<>/M=-+E!%*T()_+{}H|":;I1234N./^G---I=]S----W$%R)(O_+-N^%G"}

oops sorry lookes like I cant do it. {S$%#H*()U&^(T&^*%D%&^_O$#%U#^%$*N}\n''')

    elif choice in ["are you alive", "somthing is wrong", "smth is wrong","are you ok"]:
        print('''\n
                   (01110011 01101000 01110101 01110100 00100000 01000100 01101111 01110111 01001110)\n''')
    elif choice in ["do you have games", "do you run games", "can you run games"]:
        print('''\n
                   Yes type \'game\'/n''')
    elif choice in ['bunny','Bunny','what are you thinking','draw me a picture']:
         _art_ = [
        "         ,",
        "        /|      __",
        "       / |   ,-~ /",
        "      Y :|  //  /",
        "      | jj /( .^",
        "      >-\"~\"-v\"",
        "     /       Y",
        "    jo  o    |",
        "   ( ~T~     j",
        "    >._-' _./",
        "   /   \"~\"  |",
        "  Y     _,  |",
        " /| ;-\"~ _  l",
        "/ l/ ,-\"~    \\",
        "\\//\\/      .- \\",
        " Y        /    Y",
        " l       I     !",
        " \\     ,-|     /",
        "  |    | |    |",
        "  |    | |    |"
    ]
         print(Fore.GREEN + "\n".join(_art_))

    elif choice in ['cat','Cat','kitty']:
         _cat_ = [
        " /\\_/\\",
        "( o.o )",
        " > ^ <"
    ]
         print(Fore.MAGENTA + "\n".join(_cat_))

    elif choice in ['dog','Dog','puppy']:
         _dog_ = [
        "  __",
        "o-''|\\_____/)",
        " \\_/|_)   _ )",
        "   |  __  /",
        "   (_/ (_/"
    ]
         print(Fore.CYAN + "\n".join(_dog_))

    elif choice in ['coffee','Coffee','caffeine','coffee?']:
         _coffee_ = [
        "     ( (",
        "      ) )",
        "   .........._",
        "  ||       ||_]",
        "   \\      //",
        "    `------'"
    ]
         print(Fore.YELLOW + "\n".join(_coffee_))

   
    elif choice in ['pc','computer','terminal','hello world']:
        inner_text = f"{Fore.GREEN}> print({Fore.YELLOW}\"hello world\"{Fore.GREEN}){Fore.CYAN}"
    
        _pc_ = [
        Fore.CYAN + "    ___________________________",
        Fore.CYAN + "   |  _______________________  |",
        Fore.CYAN + "   | |                       | |",
        Fore.CYAN + "   | | " + inner_text + "| |",
        Fore.CYAN + "   | |                       | |",
        Fore.CYAN + "   | |_______________________| |",
        Fore.CYAN + "   |___________________________|",
        Fore.CYAN + "        _[_______________]_",
        Fore.CYAN + "     ___[_________________]_____",
        Fore.CYAN + "    |                           |",
        Fore.CYAN + "    |   " + Fore.MAGENTA + " ___________  " + Fore.CYAN + "          |",  
        Fore.CYAN + "    |___" + Fore.MAGENTA + "|___________|" + Fore.CYAN + "___________|"
    ]
        print("\n".join(_pc_))
        
    elif choice == "game":
        print("Guess the Number game! 🎲")
        import random
        num_to_guess = random.randint(1, 100)
        attempts = 0
        while True:
            guess = Bint(Fore.BLUE + Style.BRIGHT + "Guess a number (1-100): ")
            attempts += 1
            if guess < num_to_guess:
                print(Fore.YELLOW + "Too low! 📉")
            elif guess > num_to_guess:
                print(Fore.RED + "Too high! 📈")
            else:
                 success_print(f"Yay! You guessed it in {attempts} attempts 🎉")
                 break

    elif choice in ['do you belive in God', 'do you follow any religion', 'God']:
        print(Fore.MAGENTA + ''' Iam a chat bot...
                 I dont follow any religion
                 ''')

    elif choice in ['bro', 'Bro']:
        print(Fore.MAGENTA +"yes?")

    elif choice in ['help me in chemistry', 'chemical']:
        print(Fore.MAGENTA + "To be honest you can only do two compounds for now")
        class Ion:
            def __init__(self, name, charge):                                                                                 
                self.name = name                                                                   #this section (chemical) of code is not mine. someone helped                          
                self.charge = charge                                                                                          

        class Cation(Ion):
            def __init__(self, name, charge):                                                                                 
                super().__init__(name, charge)

        class Anion(Ion):
            def __init__(self, name, charge):
                super().__init__(name, charge)

        class Compound:
            def __init__(self, cation, anion):
                self.cation = cation
                self.anion = anion

            def formula(self):
                cation_charge = abs(self.cation.charge)
                anion_charge = abs(self.anion.charge)
                gcd = self.gcd(cation_charge, anion_charge)
                cation_subscript = anion_charge // gcd
                anion_subscript = cation_charge // gcd
                cation_formula = f"{self.cation.name}" if cation_subscript == 1 else f"{self.cation.name}{cation_subscript}"
                anion_formula = f"{self.anion.name}" if anion_subscript == 1 else f"{self.anion.name}{anion_subscript}"
                return f"{cation_formula}{anion_formula}"

            def gcd(self, a, b):
                while b:
                    a, b = b, a % b
                return a

        def create_ion(ion_type):
            name = input(Fore.CYAN + f"Enter the symbol of the {ion_type} (e.g., Na, Cl): ")
            charge = Bint(Fore.CYAN + f"Enter the charge of the {ion_type} (e.g., 1, -1): ")
            if ion_type == "cation":
                return Cation(name, charge)
            else:
                return Anion(name, charge)

        def main():
            while True:
                print("\nCreate a compound:")
                cation = create_ion("cation")
                anion = create_ion("anion")
                compound = Compound(cation, anion)
                success_print(f"The formula of the compound is: \"{compound.formula()}\"")
                cont = input(Fore.YELLOW + "Do you want to create another compound? (yes/no): ")
                if cont.strip().lower() != "yes":
                    break

        if __name__ == "__main__":
           main()

    elif choice in ['i need help in spelling', 'spell corrector', 'correct my sentence', 'spell checker']:
        print(Fore.RED + '''

               At this point I dont even know if iam a calculator or what
               
                                  ⚙️ °_o ⚙️''')


        # class
        class SpellCheckers:
            def __init__(self):
                self.spell = SpellChecker()

            def correct_text(self, text):
                words = text.split()  # Ex: "hello world" = ['hello','world']
                corrected_words = []

                for word in words:
                    corrected_word = self.spell.correction(word)
                    if corrected_word is None:  # handle words it can't correct
                        corrected_word = word
            
                    if corrected_word != word.lower():
                        print(Fore.RED + Style.BRIGHT + f"Correcting {word} to {corrected_word}")
            
                    corrected_words.append(corrected_word)  

        # returning corrected text
                return ' '.join(corrected_words)

            def run(self):
                 print(Fore.YELLOW + Style.BRIGHT + "\n---Spell Corrector---")

                 while True:
                     text = input(Fore.CYAN + "Enter text to check (or type 'exit' to quit): ")

                     if text.lower() == 'exit':
                         print(Fore.YELLOW + "Closing the program...")
                         break

                     corrected_text = self.correct_text(text)
                     success_print(f"Corrected Text: {corrected_text}\n")

        if __name__ == '__main__':
            SpellCheckers().run()

    elif choice == 'exit':
        break



    else:

        #System letter for the user
        
        error_print("\nIncoming system Error:\n\nDear sir,\n\tyour input is outside the choice.\n\tPlease choose correctly next time,\n\tto avoid this kinds of \"Error\".\n\n")

        #If the user wants to do more calculations:

    
    cont = input(Fore.YELLOW + "Do you want to do another calculation(yes/no):")
    if cont.lower() != 'yes':
         break
      

                                     #End
