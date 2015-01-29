#!/usr/bin/python

def repeat(s, flag):
    result = s * 3
    if flag:
        result = result + '!!!'
    return result

def main():
    print repeat('qzw', True)
    print repeat('qzw', False)

if __name__ == '__main__':
	main()
