import turtle


class Fractal:
    
    def __new__(cls) -> 'Fractal':
        if not hasattr(cls, 'instance'):
            cls.__instance: 'Fractal' = super(Fractal, cls).__new__(cls)
            cls.__turtle = turtle.Turtle()
    
            cls.__turtle.screen.setup(512, 512) # type: ignore
            cls.__turtle.screen.screensize(512, 512)
            cls.__turtle.screen.setworldcoordinates(0, 0, turtle.Screen().window_width(), turtle.Screen().window_height())
            cls.__turtle.speed(0)
            cls.__turtle.delay(0) # type: ignore
            cls.__turtle.tracer(0, 0) # type: ignore
            cls.__turtle.hideturtle()
            cls.__turtle.goto(0, 0)
        return cls.__instance

    # https://stackoverflow.com/questions/47841025/how-to-draw-a-sierpinski-carpet-in-python-using-turtle
    @classmethod
    def sierpinski_carpet(cls, n: int, l: int = 512) -> None:

        if n == 0:
            turtle.color('black')
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(l)
                turtle.left(90)
            turtle.end_fill()
        else:
            for _ in range(4):
                littler : int = int(n - 1)
                forward : int = int(l / 3) 

                cls.sierpinski_carpet(littler,forward)
                turtle.forward(forward)

                cls.sierpinski_carpet(littler,forward)
                turtle.forward(forward)

                turtle.forward(forward)
                turtle.left(90)

                turtle.update()

    @staticmethod
    def sierpinsky_sieve_60(n: int):
        pass

    @staticmethod
    def sierpinsky_sieve_90(n: int):
        pass

    @staticmethod
    def sierpinsky_sieve_102(n: int):
        pass

    @staticmethod
    def h(n: int):
        pass

    @staticmethod
    def haferman_carpet(n: int):
        pass

    @staticmethod
    def cantor_square(n: int):
        pass

    @staticmethod
    def box(n: int):
        pass
