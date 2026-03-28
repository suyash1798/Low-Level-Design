from random import randint


class CodeGenerator:

    @staticmethod
    def generateCode(digits):

        return randint(10 ** (digits-1), (10 ** digits) - 1)
