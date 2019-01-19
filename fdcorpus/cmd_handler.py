import json, os
import hashlib

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


    home = os.path.expanduser('~')
    fd_utilpath = os.path.join(home, '.fdutils')
    if not os.path.isdir(fd_utilpath):
        os.makedirs(fd_utilpath)

    fd_utilfile = os.path.join(fd_utilpath, 'token.config')

    token_param = {
        'telegramid' : '',
        'name': '',
        'email': '',
        'phone': '',
        'institution': ''
    }
    print("open file...")

    if os.path.isfile(fd_utilfile):
        with open(fd_utilfile, 'r') as f:
            print("read config")
            token_str = f.read()
            token_param = json.loads(token_str)

    print("token param : {}".format(token_param))

    #take the user information
    help = '''
        Hello, Register yourself.
        telegram : please entry telegram id without @
        name : your name eg. Dr. Stephen Strange
        email: valid email address  eg. dr.strange@avengers.org.us
        phone : valid phone number (with or without are code) eg. +6234675995684 or 034675995684
        insitution: where do you work: The Avengers Initiative America
            if you're a student use your uni e.g University of Gotham
    '''
    # print(help)

    temp = input("username telegram [{}]: ".format(token_param['telegramid']))
    token_param['telegramid'] = temp or token_param['telegramid']
    temp = None

    temp = input("name [{}]: ".format(token_param['name']))
    token_param['name']  = temp or token_param['name']
    temp = None

    temp = input("email [{}]: ".format(token_param['email']))
    token_param['email']  = temp or token_param['email']
    temp = None

    temp = input("phone [{}]: ".format(token_param['phone']))
    token_param['phone']  = temp or token_param['phone']
    temp = None
    
    temp = input("institution [{}]: ".format(token_param['institution']))
    token_param['institution']  = temp or token_param['institution']
    temp = None

    print(" this is your data to be registered: {}".format(token_param))

    token_str = json.dumps(token_param)
    token = hashlib.md5(str.encode(token_str)).hexdigest()

    with open(fd_utilfile, 'w+') as f :
        token_param['token'] = token
        config_entry = json.dumps(token_param)
        print("config entry {}, type: {}".format(config_entry, type(config_entry)))
        f.writelines(config_entry)
    
    #store user info to server
    print("Storing to the server")
    print("Thank You! please see : list and download ")