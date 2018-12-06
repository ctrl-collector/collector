from collector.cli import Command, Args


if __name__ == '__main__':
    cli = Command(
            name='',
            description='Pretends to be collector',
            usage=open('collector/figlet').read())
    putin = Command(
        name='putin',
        pos=2,
        description='Record changes to the repository',
        usage="Putin tested"
    )
    boast = Command(
        name='boast',
        pos=2,
        description='Download objects and refs from another repository',
        usage="Boast tested"
    )
    cli.add_command(putin)
    cli.add_command(boast)
    cli.run()


    # while True:
    #     color = input("Your color: ")
    #     text = open('collector/figlet').read()
    #     display(text, color=color)