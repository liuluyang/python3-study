
def main():
    try:
        print ('t')
        return 1
    finally:
        print ('f')
        #return 2
        #print ('f')

print (main())