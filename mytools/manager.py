

def split_job(length, sep=1):
    '''
    将给定的长度length分成sep份,用于多线程
    return:
        [(0, 5), (5, 10), (10, 15), (15, 20)]
    '''
    job_list = []
    b = length // sep
    for i in range(sep):
        job_list.append((i * b, i * b + b))
    if length % sep:
        job_list.append((b * sep, length + 1))

    return job_list

if __name__ == '__main__':
    print(split_job(101, 5))