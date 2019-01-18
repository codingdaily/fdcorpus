def default_fn(args):
    '''
        give default action: (showing the usage)
    '''

def list_fn(args):
    '''
        list corpus information
    '''
    #reject if there's no user info

    #pull corpus informations
    pass

def download_fn(args):
    '''
        download corpus
    '''
    #reject if there's user info

    #download corpus based on argument
    #find out the home location
    #make user's FDN-corpus directory
    pass

def register_fn(args):
    '''
        register the user
    '''

    # reg_cmd.add_argument('telegram-username', help='Your Telegram Username, Please')
    # reg_cmd.add_argument('name', help='Your Real Name')
    # reg_cmd.add_argument('email', help='Your email, so we can inform you latest data from Female Daily Network')
    # reg_cmd.add_argument('phone', help="Let's connect! we wanted to know who use our data, please enter the number :) ")
    # reg_cmd.add_argument('institution', help=occupation_help)
    help = '''
        Hello, Register yourself.
        telegram : please entry telegram id without @
        name : your name eg. Dr. Stephen Strange
        email: valid email address  eg. dr.strange@avengers.org.us
        phone : valid phone number (with or without are code) eg. +6234675995684 or 034675995684
        insitution: where do you work: The Avengers Initiative America
            if you're a student use your uni e.g University of Gotham
    '''
    print(help)

    telegram_id = input("username telegram: ")
    name  = input("name: ")
    email = input("email: ")
    phone = input("phone: ")
    insitution = input("institution: ")

    print(" this is your data to be registered: {} \n {} \n {} \n {} \n {}".format(telegram_id, name, email, phone, insitution))




    

    #register the user
    #tasks:
    #take the user information
    #store user session info
    #store user info to server
    pass