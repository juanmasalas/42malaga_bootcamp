from loading import ft_progress
from time import sleep

X = range(3333)
def test_X(X):
    ret = 0
    for elem in ft_progress(X):
        ret += elem 
        sleep(0.005)
    print()
    print(ret)
test_X(X)