import sqlite3

### CONNECTING TO DATABASE ###
conn = sqlite3.connect('stockmarket.db')
c = conn.cursor()


### CREATING TABLES ###
createTable_stocks = """
        CREATE TABLE IF NOT EXISTS 
            stocks(
                stock_id INTEGER PRIMARY KEY,
                stock_ticker TEXT NOT NULL UNIQUE,
                stock_name TEXT,
                stock_exchange TEXT,
                stock_type TEXT,
                stock_ipoDate DATE,
                stock_delistingDate DATE,
                stock_status TEXT,
                stock_updateTime DATE
            )
        """
c.execute(createTable_stocks)


# createTable_avData_daily = """
#         CREATE TABLE IF NOT EXISTS 
#             avData_daily(
#                 daily_id INTEGER PRIMARY KEY,
#                 stock_id TEXT,
#                 daily_date TEXT,
#                 daily_openPrice TEXT,
#                 daily_highPrice TEXT,
#                 daily_lowPrice TEXT,
#                 daily_adjustedClosingPrice TEXT,
#                 daily_tradingVolume TEXT,
#                 daily_lastDividendAmount TEXT,
#                 daily_updateTime DATE
#             )
#         """
# c.execute(createTable_avData_daily)


createTable_avData_daily = """
        CREATE TABLE IF NOT EXISTS 
            avData_daily(
                daily_id INTEGER PRIMARY KEY,
                stock_id INTEGER,
                daily_date DATE,
                daily_adjustedClosingPrice INTEGER,
                daily_tradingVolume INTEGER,
                daily_lastDividendAmount INTEGER,
                daily_updateTime DATE,
                CONSTRAINT `avData_daily` FOREIGN KEY (`stock_id`) REFERENCES `stocks` (`stock_id`)
            )
        """
c.execute(createTable_avData_daily)


createTable_avData_overview = """
        CREATE TABLE IF NOT EXISTS 
            avData_overview(
                overview_id INTEGER PRIMARY KEY,
                stock_id INTEGER NOT NULL UNIQUE,
                overview_assetType TEXT,
                overview_marketCapitalization INTEGER,
                overview_updateTime DATE NOT NULL,
                CONSTRAINT `avData_overview` FOREIGN KEY (`stock_id`) REFERENCES `stocks` (`stock_id`)
            )
        """
c.execute(createTable_avData_overview)


createTable_avData_income = """
        CREATE TABLE IF NOT EXISTS 
            avData_income(
                income_id INTEGER PRIMARY KEY,
                stock_id INTEGER NOT NULL,
                income_reportID INTEGER,
                income_reportYear INTEGER ,
                income_fiscalDateEnding DATE ,
                income_totalRevenue INTEGER,
                income_updateTime DATE,
                CONSTRAINT `avData_income` FOREIGN KEY (`stock_id`) REFERENCES `stocks` (`stock_id`)
            )
        """
c.execute(createTable_avData_income)


c.close()
conn.close()