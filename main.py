from controller.input_manager import InputManager
from controller.transactions_controller import TransactionsController

controller = TransactionsController(InputManager().get_transactions())
total_sum, deposits_sum_by_period = controller.get_total_sum(), controller.deposits_sum_by_period
OutputManager.init(total_sum, deposits_sum_by_period)
