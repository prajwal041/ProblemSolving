import re

def remove_comments(inp_file, out_file):
    try:
        f = open(inp_file, 'r')
        content = f.read()
        f.close()

        no_multilines = re.sub(r"('''.*?'''|\"\"\".*?\"\"\")", '', content, flags=re.DOTALL)
        no_comments = re.sub(r'#.*', '', no_multilines)
        print(no_comments)
        #f = open(out_file, 'w')


    except Exception as e:
        print("Exception occurred")


remove_comments('Flipkart_Cab_Sharing.py', None)
