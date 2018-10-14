import threading

def calc_square(number):
    print('Square:' , number * number)


def calc_quad(number):
    print('Quad:' , number * number * number * number)

def main(number):
    print('Def main called')
    thread1 = threading.Thread(target=calc_square, args=(number,))
    thread2 = threading.Thread(target=calc_quad, args=(number,))
    # Will execute both in parallel
    thread1.start()
    thread2.start()
    # Joins threads back to the parent process, which is this
    # program
    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main(2)




#The multithreading library is lightweight, shares memory, responsible for responsive UI and is used well for I/O bound applications. However, the module isn’t killable and is subject to the GIL

#Threading library in Python

#Multiple threads live in the same process in the same space, each thread will do a specific task, have its own code, own stack memory, instruction pointer, and share heap memory. If a thread has a memory leak it can damage the other threads and parent process
