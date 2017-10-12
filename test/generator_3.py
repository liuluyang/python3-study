
def gen_with_return(range_num):
    if range_num < 0:
        return
    else:
        for i in range(range_num):
            yield i

if __name__ == '__main__':
    print (list(gen_with_return(-1)))
    print (list(gen_with_return(1)))

##############################################

def consumer(func):
    def wapper(*args, **kwargs):
        gen = func()
        next(gen)
        return gen
    wapper.__name__ = func.__name__
    wapper.__doc__ = func.__doc__
    wapper.__dict__ = func.__dict__
    return wapper
@consumer
def t():
    yield 1
    yield 2

print (next(t()))

#############################################################
import types
@types.coroutine
def generator_coroutine():
    yield 1

async def native_coroutine():
    await generator_coroutine()

def main():
    print (native_coroutine().send(None))

main()