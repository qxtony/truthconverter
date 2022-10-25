from re import findall
from typing import List


class Truth:
    def __init__(self, expression: str) -> None:
        self.expression: str = expression.replace(" ", "")

    def get_variables_from_expression(self) -> List[str]:
        return list(set(findall(r"[A-Z]", self.expression)))

    def get_truth_table(self) -> List[List[int]]:
        variables = self.get_variables_from_expression()
        table = []

        for value in range(2 ** len(variables)):
            table.append([int(row) for row in f"{value:0{len(variables)}b}"])

        return table

    def get_truth_values(self) -> List[int]:
        return [self.get_truth_value(row) for row in self.get_truth_table()]

    def get_truth_value(self, row: List[int]) -> int:
        expression = self.expression

        for index, variable in enumerate(self.get_variables_from_expression()):
            expression = expression.replace(variable, str(row[index]))

        return int(eval(expression))

    def __str__(self) -> str:
        table = self.get_truth_table()
        values = self.get_truth_values()

        string = ""

        for index, variable in enumerate(self.get_variables_from_expression()):
            string += f"{variable} "

        string += "| Result\n"

        for row in table:
            for value in row:
                string += f"{value} "

            string += f"| {values[table.index(row)]}\n"

        return string
