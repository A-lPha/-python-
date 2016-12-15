from sys import argv

#输入要读取的文件名
filename = raw_input("Filename:")
#解压
script, filename = argv, filename
#打开输入的文件
txt = open (filename)
#“这是你的文件”
print "Here's your file %r:" % filename
#文件内容
print txt.read()
#再次读取文件内容
print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again.read()
