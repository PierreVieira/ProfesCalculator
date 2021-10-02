from controller.input_manager import InputManager
from controller.output.output_manager import OutputManager
from controller.transactions_controller import TransactionsController

controller = TransactionsController(InputManager().get_transactions())
total_sum, deposits_sum_by_period, mean_by_month = controller.get_total_sum(), controller.deposits_sum_by_period, controller.get_mean_by_month()
OutputManager.run(total_sum, deposits_sum_by_period, mean_by_month, output_txt=False)
