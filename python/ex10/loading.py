import time
import sys
def ft_progress(lst):
    total = len(lst)
    t0 = time.time()
    progress_bar_length = 30
    for i, item in enumerate(lst,1):
        percent = int(i / total * 100)
        completed = int(percent / 100 * progress_bar_length)
        remaining = progress_bar_length - completed
        t = time.time() - t0
        if completed == 0:
            completed = 1
        eta = (remaining * t) / completed
        sys.stdout.write("\rETA: {:.2f}s [{:3d}%][{}>{}] {}/{} | elapsed time {:.2f}s "
                         .format(eta, percent, "=" * completed, " " * remaining, i, total, t))
        sys.stdout.flush()
        yield item
    

# listy = range(3333)
# ret = 0
# for elem in ft_progress(listy):
#     ret += elem
#     time.sleep(0.005)
# print()
# print(ret)