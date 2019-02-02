class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)


counter = JustCounter()
print(JustCounter.__secretCount)
counter.count()
counter.count()
print (counter.__secretCount)

