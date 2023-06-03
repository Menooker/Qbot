from easyquant.backtest_engine import BackTestEngine
from strategy_loader import load_strategy_class
from web.database import Database
from web.db_service import DbService
from web.settings import APISettings
from strategies.CCI import Strategy
#from strategies.中概互联_自动T import Strategy
# settings = APISettings()
# database = Database()
# db_service = DbService(settings, database)

# strategy = db_service.list_strategies()[0]

# strategy_class = load_strategy_class(strategy.code, "custom_strategy_%d" % strategy.id)

mock_start_dt = "2021-08-05"
mock_end_dt = "2022-08-05"


#strategy = Strategy(user=m.user, log_handler=log_handler, main_engine=m)
backtest_engine = BackTestEngine(
    strategy_class=Strategy,
    start_date=mock_start_dt,
    end_date=mock_end_dt,
    bar_type="1d",
    quotation="jqdata",
)

backtest_engine.start()

print("mock end")

print(backtest_engine.user.get_balance())

for deal in backtest_engine.user.get_current_deal():
    print(deal.deal_time, deal.bs_type, deal.deal_price, deal.deal_amount)

backtest_engine.shutdown()
