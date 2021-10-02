from collections import OrderedDict

from controller.output.output_graph import output_graph


class OutputManager:
    @staticmethod
    def __get_string_sum_by_period(deposits_sum_by_period: OrderedDict) -> str:
        output = ''
        for key, value in deposits_sum_by_period.items():
            output += f'{key}: R$ {value:.2f}\n'
        return output

    @staticmethod
    def __output_in_txt(output: str):
        with open('files/output/output.txt', 'w', encoding='utf-8') as arq:
            arq.write(output)

    @staticmethod
    def run(total_sum: float,
            deposits_sum_by_period: OrderedDict,
            mean_by_month: float,
            output_txt: bool = True) -> None:
        total_output = f'TOTAL: R$ {total_sum:.2f}\nMean by month: R$ {mean_by_month:.2f}'
        output = f'{total_output}\n{"=" * (2 + len(total_output))}\n{OutputManager.__get_string_sum_by_period(deposits_sum_by_period)}'
        print(output)
        if output_txt:
            OutputManager.__output_in_txt(output)
        output_graph(deposits_sum_by_period)
