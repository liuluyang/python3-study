
def gen_with_return(range_num):
    if range_num < 0:
        return
    else:
        for i in range(range_num):
            yield i

if __name__ == '__main__':
    print (list(gen_with_return(-1)))
    print (list(gen_with_return(1)))