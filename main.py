from typing import List


class ATM(object):
    def __init__(self):
        self.__atm_banknotes = {
            500: 0,
            200: 0,
            100: 0,
            50: 0,
            10: 0,
        }
        self.__d_len = len(self.__atm_banknotes)

    def deposit(self, banknotesCount) -> None:
        """
        :type banknotesCount: List[int]
        :rtype: None
        """
        # сложность по времени - O(n)
        # сложность по памяти - O(1)
        for i, k in enumerate(self.__atm_banknotes):
            i_end = self.__d_len - 1 - i
            self.__atm_banknotes[k] += banknotesCount[i_end]

    def withdraw(self, amount) -> List[int]:
        """
        :type amount: int
        :rtype: List[int]
        """
        # сложность по времени - O(n + amount)
        # сложность по памяти - O(n)

        # если сумма выдачи меньше или равана нулю
        if amount <= 0:
            return [-1]

        # делаем копию словаря с количеством банкнот каждого номинала
        temp_banknotes = self.__atm_banknotes.copy()
        result = [0] * self.__d_len
        # цикл по номиналу.
        for i, denom in enumerate(self.__atm_banknotes):
            # получаем количество банкнот номинала
            count = temp_banknotes[denom]
            i_end = self.__d_len - 1 - i
            # пока сумма больше текущего номинала, и банкноты есть в банкомате
            while amount >= denom and count > 0:
                amount -= denom
                temp_banknotes[denom] -= 1
                count -= 1
                result[i_end] += 1
            # если сумма равна 0 - переопределяем количество банкнот и возвращаем результат
            if amount == 0:
                self.__atm_banknotes = temp_banknotes
                return result

        return [-1]


if __name__ == "__main__":
    obj = ATM()
    obj.deposit([0, 0, 1, 2, 1])
    assert obj.withdraw(600) == [0, 0, 1, 0, 1]
    obj.deposit([0, 1, 0, 1, 1])
    assert obj.withdraw(600) == [-1]
    assert obj.withdraw(550) == [0, 1, 0, 0, 1]
