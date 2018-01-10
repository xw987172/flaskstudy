class mytest:
    def hello(self):
        def decorator(f):
            print "111"
            # print "hello,",string1
            return f
        return decorator

    @hello(1)
    def say(self):
        print "xw"

if __name__=="__main__":
    a =mytest()
    f=a.hello()
    f(1)