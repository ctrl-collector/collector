
import yaml

class ToolkitHandler:

    def __init__(self, tkfilename):
        self.tkfilename = tkfilename
        self.store = []

    def gettools(self):
        tools = None
        with open(self.tkfilename) as tkfile:
            tools = yaml.load(tkfile)
        return tools

if __name__ == '__main__':
    toolkit_handler = ToolkitHandler('collector.yml')
    print(toolkit_handler.gettools())