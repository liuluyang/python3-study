#coding:utf8
def generator_t():
    print ('start')
    yield 1
    return

def normal_():
    return 1

print (generator_t(), type(generator_t()))
print (normal_(), type(normal_()))

t = generator_t()
print (next(t))
#print (next(t))

####################################################
def gen_data_from_file(file_name):
    with open(file_name,'r',encoding='utf-8') as f:
        for line in f.readlines():
            yield line

def gen_words(line):
    for word in line:
        if word.strip():
            yield word
        #else:
            #return

def count_words(file_name):
    word_map = {}
    for line in gen_data_from_file(file_name):
        for word in gen_words(line):
            if word not in word_map:
                word_map[word] = 0
            word_map[word] += 1
    return word_map

def count_total_chars(file_name):
    total = 0
    for line in gen_data_from_file(file_name):
        total += len(line)
    return total

if __name__ == '__main__':
    print (count_words('desc.txt'), count_total_chars('yanghui.py'))

with open('desc.txt', 'r', encoding='utf8') as f:
    #f.write('放松的方式')
    #for i in f.readlines():
        #print (i.strip())
    print (1)
    print (f.readline().strip())
    print (type(f.readline().strip()))
    print (f.readline().strip())
    print (type(f.readline().strip()))