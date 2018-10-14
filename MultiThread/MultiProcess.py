import multiprocessing

def calc_square(number):
    print('Square:' , number * number)
    result = number * number
    print(result)


def calc_quad(number):
    print('Quad:' , number * number * number * number)


def main(number):
    print('Def main called')
    p1 = multiprocessing.Process(target=calc_square, args=(number,))
    p2 = multiprocessing.Process(target=calc_quad, args=(number,))


    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == "__main__":
    main(2)
