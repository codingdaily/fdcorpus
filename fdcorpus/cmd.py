from argparse import ArgumentParser
from fdcorpus.cmd_handler import list_fn, download_fn, register_fn, default_fn

def main():
    parser = ArgumentParser(description="FDN corpus client",prog="fdncorpus")
    sparser = parser.add_subparsers()

    reg_cmd = sparser.add_parser("register", help="register to fdcorpus service , just need name and email ")
    list_cmd = sparser.add_parser("list", help="list available corpus")
    download_cmd = sparser.add_parser("download", help="download the corpus just need corpus ID")

    occupation_help = '''
        We wanted to make a connection with you. so.. please give us information where you working at
        if you're a student, please state which Uni / School you're currently studying at
        If you work by yourselves just state: Wirausaha / Independent
    '''
    #command arguments

    

    download_cmd.add_argument('corpus-id', help="corpus ID you wanted to download")
    #set defaults actions
    reg_cmd.set_defaults(func=register_fn)
    list_cmd.set_defaults(func=list_fn)
    download_cmd.set_defaults(func=download_fn)


    args = parser.parse_args()
    try:
        args.func(args)
    except Exception as e:
        print("error <!!!!> : {}".format(e))
        parser.print_help()
    

if __name__ == "__main__" :
    main()
