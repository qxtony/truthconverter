from re import findall
from typing import List, Tuple


class Truth:
    def __init__(self, expression: str) -> None:
        self.expression: str = expression

    def get_variables_from_expression(self) -> List[str]:
        return sorted(list(set(findall(r"[A-Z]", self.expression))))

    def insert_operators_into_expression(self, expression: list) -> str:
        return (
            expression
            .replace("&", "and")
            .replace("|", "or")
            .replace("!", "not")
            .replace("_", "<=")
        )

    def get_truth_values(self) -> List[List[int]]:
        variables = self.get_variables_from_expression()
        table = []

        for value in range(2 ** len(variables)):
            table.append([int(row) for row in f"{value:0{len(variables)}b}"])

        return table

    def get_table_with_replaced_operations(self) -> List[List[int]]:
        table = []

        for row in self.get_truth_values():
            variables = self.get_variables_from_expression()
            expression = self.expression

            for variable, value in zip(variables, row):
                expression = expression.replace(variable, str(value))

            table.append(expression)

        return table

    def execute_code(self, expression: str) -> int:
        return int(eval(expression))

    def get_values_of_expressions(self) -> List[int]:
        values = []

        for replacing_expression in self.get_table_with_replaced_operations():
            values.append(
                self.execute_code(
                    self.insert_operators_into_expression(replacing_expression)
                )
            )

        return values

    def get_truth_table(self):
        table = zip(self.get_truth_values(), self.get_values_of_expressions())

        string_truth_table = "\n".join(
            " ".join(map(str, row)) + f" → {result}"
            for row, result in table
        )
        return string_truth_table

    def __str__(self):
        truth_table = [
            f"Expression: {self.expression}\n"
            f"{' '.join(self.get_variables_from_expression())} → Result",
            self.get_truth_table()
        ]

        return "\n".join(truth_table)
