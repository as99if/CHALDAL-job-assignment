from ..src import active, superactive, read, bored
import sys



if __name__ == '__main__':

    function = ""
    if len(sys.argv) < 3:
        print('check arguments again')
    else:
        function = getattr(sys.modules[__name__], sys.argv[1])
        d1 = sys.argv[2]
        d2 = sys.argv[3]
        function(d1, d2)
