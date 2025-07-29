import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/apidojo/api/seeking-alpha'

mcp = FastMCP('seeking-alpha')

@mcp.tool()
def v2_auto_complete(query: Annotated[str, Field(description='Any word or phrase that you are familiar with')],
                     type: Annotated[Union[str, None], Field(description='One of the following : people|symbols|pages. Separated by comma for multiple options')] = None,
                     size: Annotated[Union[int, float, None], Field(description='The number items per response (10 is maximum) Default: 5')] = None) -> dict: 
    '''Get suggested symbols, authors, etc... by provided word or phrase'''
    url = 'https://seeking-alpha.p.rapidapi.com/v2/auto-complete'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'type': type,
        'size': size,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def auto_complete(term: Annotated[str, Field(description='Any word or phrase that you are familiar with')]) -> dict: 
    '''Get suggested symbols, authors, etc... by provided word or phrase'''
    url = 'https://seeking-alpha.p.rapidapi.com/auto-complete'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'term': term,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def authors_get_details(slug: Annotated[str, Field(description='The value of people/slug json object returned in .../auto-complete endpoint')]) -> dict: 
    '''Get author details'''
    url = 'https://seeking-alpha.p.rapidapi.com/authors/get-details'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'slug': slug,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_meta_data(symbol: Annotated[str, Field(description='Symbol to query for data, only one is allowed at a time.')]) -> dict: 
    '''Get meta data of specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-meta-data'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_profile(symbols: Annotated[str, Field(description='Symbol to query for data. Separating by comma to query multiple symbols at once, ex : aapl,tsla')]) -> dict: 
    '''Get profile information of specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-profile'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbols': symbols,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_summary(symbols: Annotated[str, Field(description='Symbol to query for data. Separating by comma to query multiple symbols at once, ex : aapl,tsla')]) -> dict: 
    '''Get summary information of specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-summary'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbols': symbols,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_financials(symbol: Annotated[str, Field(description='Symbol to query for data, only one is allowed at a time.')],
                           target_currency: Annotated[Union[str, None], Field(description='The currency code')] = None,
                           period_type: Annotated[Union[str, None], Field(description='One of the following : annual|quarterly|ttm')] = None,
                           statement_type: Annotated[Union[str, None], Field(description='One of the following : income-statement|balance-sheet|cash-flow-statement')] = None) -> dict: 
    '''Get financials for specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-financials'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'target_currency': target_currency,
        'period_type': period_type,
        'statement_type': statement_type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_fundamentals(symbol: Annotated[str, Field(description='Symbol to query for data, only one is allowed at a time.')],
                             limit: Annotated[Union[str, None], Field(description='')] = None,
                             period_type: Annotated[Union[str, None], Field(description='One of the following : quarterly|annual')] = None,
                             field: Annotated[Union[str, None], Field(description='One of the following : revenues|other_revenues_summary_subtotal|total_revenue|cost_revenue|gross_profit|selling_general_admin_expenses_total|rd_expenses|other_operating_exp_total|operating_income|interest_expense_total|interest_and_investment_income|net_interest_exp_standard|currency_exchange_gains_loss|other_non_operating_income|ebt_incl_unusual_items|income_tax_expense|earnings_from_cont_ops|net_income_to_company|net_income|ni_to_common_incl_extra_items|ni_to_common_excl_extra_items|revenue_per_share|eps|basic_eps_excl_extra_items|weighted_average_basic_shares_outstanding|diluted_eps|diluted_eps_excl_extra_itmes|weighted_average_diluted_shares_outstanding|normalized_basic_eps|normalized_diluted_eps|div_rate|payout_ratio|ebitda|ebita|ebit_op_in|ebitdar|effective_tax_rate|normalized_net_income|interest_on_long_term_debt|r_d_exp|foreign_sales')] = None) -> dict: 
    '''Get fundamentals for specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-fundamentals'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'limit': limit,
        'period_type': period_type,
        'field': field,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_peers(symbol: Annotated[str, Field(description='Symbol to query for data. Separating by comma to query multiple symbols at once, ex : aapl,tsla')]) -> dict: 
    '''Get peers of specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-peers'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_historical_prices(symbol: Annotated[str, Field(description='Symbol to query for data, only one is allowed at a time.')],
                                  start: Annotated[str, Field(description='The date to get historical prices from. The format is yyyy-MM-dd . Ex : 2022-02-01')],
                                  end: Annotated[str, Field(description='The date to get historical prices to. The format is yyyy-MM-dd . Ex : 2023-03-09')],
                                  show_by: Annotated[Union[str, None], Field(description='One of the following : day|week|month')] = None,
                                  sort: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get historical prices'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-historical-prices'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'start': start,
        'end': end,
        'show_by': show_by,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_dividend_history(symbol: Annotated[str, Field(description='Symbol to query for data, only one is allowed at a time.')],
                                 years: Annotated[Union[str, None], Field(description='')] = None,
                                 group_by: Annotated[Union[str, None], Field(description='One of the following : year|month')] = None) -> dict: 
    '''Get dividend history of specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-dividend-history'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'years': years,
        'group_by': group_by,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_splits(symbol: Annotated[str, Field(description='Symbol to query for data, only one is allowed at a time.')]) -> dict: 
    '''Get splits'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-splits'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_momentum(symbols: Annotated[str, Field(description='Symbol to query for data. Separating by comma to query multiple symbols at once, ex : aapl,tsla')],
                    fields: Annotated[Union[str, None], Field(description='One of the following : movAvg10d|movAvg50d|movAvg100d|movAvg200d|pClose10d|pClose50d|pClose100d|pClose200d|pWeekVolShares|low52|high52|chgp5d|chgp1m|chgp3m|chgp6m|chgp9m|chgpYtd|chgp1y|chgp3y|chgt3y|chgp5y|chgt5y|chgp10y|chgt10y|chgt1m|chgtYtd|chgt1y Separated by comma for multiple options. Ex : chgp3m,chgp6m,chgp9m,chgp1y,low52,high52,movAvg10d')] = None) -> dict: 
    '''Get momentum of specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/v2/get-momentum'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbols': symbols,
        'fields': fields,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_valuation(symbols: Annotated[str, Field(description='Symbol to query for data. Separating by comma to query multiple symbols at once, ex : aapl,tsla')]) -> dict: 
    '''Get valuation of specific symbols'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-valuation'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbols': symbols,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_metrics(symbols: Annotated[str, Field(description='Symbol to query for data. Separating by comma to query multiple symbols at once, ex : aapl,tsla')],
                        fields: Annotated[Union[str, None], Field(description='One of the following : altman_z_score|analysts_down_avg_5y|analysts_down_percent_avg_5y|analysts_up_avg_5y|analysts_up_percent_avg_5y|assets_turnover|authors_rating_pro|beta24|capex_change|capex_change_avg_5y|capex_to_sales|cash_from_operations_as_reported|cf_op_change_display|cf_op_change_display_avg_5y|coefficient_of_variation_90d|common_equity_10y|common_equity_3y|common_equity_5y|common_equity_yoy|degree_of_operating_leverage_ttm|diluted_eps_growth|diluted_eps_growth_avg_5y|dilutedEps10y|dilutedEps3y|dilutedEps5y|dilutedEpsGrowth|div_grow_rate10|div_grow_rate3|div_grow_rate5|div_growth_category|div_pay_date|div_rate_fwd|div_rate_ttm|div_yield_4y_avg_5y|div_yield_category_avg_5y|div_yield_fwd|div_yield_fwd_avg_5y|dividend_growth|dividend_lt_fwd_growth|dividend_per_share_change_dislpay|dividend_per_share_change_dislpay_avg_5y|dividend_yield|dividend_yield_avg_5y|dps_yoy|dps_yoy_avg_5y|earn_yield_gaap_fy1_avg_5y|earnings_yield_avg_5y|earningsGrowth|earningsGrowth10y|earningsGrowth3|earningsGrowth5y|ebit_change_display|ebit_change_display_avg_5y|ebit_margin|ebitda_10y|ebitda_3y|ebitda_5y|ebitda_change_display|ebitda_change_display_avg_5y|ebitda_margin|ebitda_yoy|ebitda_yoy_avg_5y|ebitdaYoy|eps_change_display|eps_change_display_avg_5y|eps_gaap_annual_growth_yoy|eps_gaap_annual_growth_yoy_avg_5y|eps_gaap_growth_3y_annual_fwd|eps_gaap_growth_3y_annual_fwd_avg_5y|eps_ltg|eps_ltg_avg_5y|eps_revisions_category|ev_12m_sales_ratio|ev_12m_sales_ratio_avg_5y|ev_ebit|ev_ebit_avg_5y|ev_ebit_fy1|ev_ebit_fy1_avg_5y|ev_ebitda|ev_ebitda_avg_5y|ev_ebitda_fy1|ev_ebitda_fy1_avg_5y|ev_sales_fy1|ev_sales_fy1_avg_5y|fcf_per_share_change_display|fcf_per_share_change_display_avg_5y|fcf_yield_avg_5y|fcf_yield_fy1_avg_5y|gross_loans_10y|gross_loans_3y|gross_loans_5y|gross_loans_yoy|gross_margin|growth_category|impliedmarketcap|last_div_date|last_price_vs_sma_10d|last_price_vs_sma_200d|last_price_vs_sma_50d|levered_fcf_margin|levered_free_cash_flow_yoy|levered_free_cash_flow_yoy_avg_5y|leveredFreeCashFlow10y|leveredFreeCashFlow3y|leveredFreeCashFlow5y|leveredFreeCashFlowYoy|log_of_unadjusted_stock_price|marketcap|marketcap_display|momentum_category|net_eps|net_inc_per_employee|net_income|net_interest_income_10y|net_interest_income_3y|net_interest_income_5y|net_interest_income_yoy|net_margin|netIncome10y|netIncome3y|netIncome5y|netIncomeYoy|normalizedNetIncome10y|normalizedNetIncome3y|normalizedNetIncome5y|normalizedNetIncomeYoy|op_cf_yoy|op_cf_yoy_avg_5y|oper_income_fy1_market_cap_avg_5y|oper_income_market_cap_avg_5y|operating_income_ebit_yoy|operating_income_ebit_yoy_avg_5y|operatingIncomeEbit10y|operatingIncomeEbit3y|operatingIncomeEbit5y|operatingIncomeEbitYoy|payout_ratio|pb_fy1_ratio|pb_fy1_ratio_avg_5y|pb_ratio|pb_ratio_avg_5y|pe_gaap_fy1|pe_gaap_fy1_avg_5y|pe_nongaap|pe_nongaap_avg_5y|pe_nongaap_fy1|pe_nongaap_fy1_avg_5y|pe_ratio|pe_ratio_avg_5y|peg_gaap|peg_gaap_avg_5y|peg_nongaap_fy1|peg_nongaap_fy1_avg_5y|price_cf_ratio|price_cf_ratio_avg_5y|price_cf_ratio_fy1|price_cf_ratio_fy1_avg_5y|price_high_52w|price_low_52w|profitability_category|ps_ratio|ps_ratio_avg_5y|ps_ratio_fy1|ps_ratio_fy1_avg_5y|quant_rating|return_on_avg_tot_assets|return_on_net_tangible_assets|return_on_total_capital|revenue_change_display|revenue_change_display_avg_5y|revenue_growth|revenue_growth_avg_5y|revenue_growth3|revenue_growth5|revenueGrowth10|roe|roe_change_display|roe_change_display_avg_5y|roe_yoy|roe_yoy_avg_5y|rtn_on_common_equity|sell_side_rating|shares|short_interest_percent_of_float|sma_10d|sma_200d|sma_50d|tangible_book_per_share|tangibleBookValue10y|tangibleBookValue3y|tangibleBookValue5y|tangibleBookValueYoy|tev|total_cash|total_debt|total_revenue|totalAssets10y|totalAssets3y|totalAssets5y|totalAssetsYoy|value_category|working_cap_change|working_cap_change_avg_5y|yld_on_cost_1y_avg_5y|yld_on_cost_3y_avg_5y|yld_on_cost_5y_avg_5y . Separated by comma for multiple options. Ex : quant_rating,authors_rating_pro,sell_side_rating,marketcap,dividend_yield,etc...')] = None) -> dict: 
    '''Get metrics of specific symbols'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-metrics'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbols': symbols,
        'fields': fields,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_option_expirations(symbol: Annotated[str, Field(description='Symbol to query for data.')]) -> dict: 
    '''Get option expirations to use with .../symbols/get-options endpoint'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-option-expirations'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_options(ticker_id: Annotated[str, Field(description='The value of ticker_id returned in .../symbols/get-option-expirations')],
                   expiration_date: Annotated[Union[str, None], Field(description='The format is yyyy-MM-dd (2024-11-15), and the valid dates returned in .../symbols/get-option-expirations endpoint')] = None) -> dict: 
    '''Get optional prices'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/v2/get-options'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker_id': ticker_id,
        'expiration_date': expiration_date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_metric_grades(symbol: Annotated[str, Field(description='Symbol to query for data, only one is allowed at a time.')],
                              fields: Annotated[Union[str, None], Field(description='One of the following, separated by comma for multiple options : altman_z_score|analysts_down_avg_5y|analysts_down_percent_avg_5y|analysts_up_avg_5y|analysts_up_percent_avg_5y|assets_turnover|authors_rating_pro|beta24|capex_change|capex_change_avg_5y|capex_to_sales|cash_from_operations_as_reported|cf_op_change_display|cf_op_change_display_avg_5y|common_equity_10y|common_equity_3y|common_equity_5y|common_equity_yoy|diluted_eps_growth|diluted_eps_growth_avg_5y|dilutedEps10y|dilutedEps3y|dilutedEps5y|dilutedEpsGrowth|div_grow_rate3|div_grow_rate5|div_pay_date|div_rate_fwd|div_rate_ttm|div_yield_fwd|dividend_growth|dividend_per_share_change_dislpay|dividend_per_share_change_dislpay_avg_5y|dividend_yield|dps_yoy|dps_yoy_avg_5y|earningsGrowth|earningsGrowth10y|earningsGrowth3|earningsGrowth5y|ebit_change_display|ebit_change_display_avg_5y|ebit_margin|ebitda_10y|ebitda_3y|ebitda_5y|ebitda_change_display|ebitda_change_display_avg_5y|ebitda_margin|ebitda_yoy|ebitda_yoy_avg_5y|ebitdaYoy|eps_change_display|eps_change_display_avg_5y|eps_ltg|eps_ltg_avg_5y|eps_revisions_category|ev_12m_sales_ratio|ev_ebitda|fcf_per_share_change_display|fcf_per_share_change_display_avg_5y|gross_loans_10y|gross_loans_3y|gross_loans_5y|gross_loans_yoy|gross_margin|growth_category|impliedmarketcap|last_div_date|last_price_vs_sma_10d|last_price_vs_sma_200d|last_price_vs_sma_50d|levered_fcf_margin|levered_free_cash_flow_yoy|levered_free_cash_flow_yoy_avg_5y|leveredFreeCashFlow10y|leveredFreeCashFlow3y|leveredFreeCashFlow5y|leveredFreeCashFlowYoy|marketcap|marketcap_display|momentum_category|net_eps|net_inc_per_employee|net_income|net_interest_income_10y|net_interest_income_3y|net_interest_income_5y|net_interest_income_yoy|net_margin|netIncome10y|netIncome3y|netIncome5y|netIncomeYoy|normalizedNetIncome10y|normalizedNetIncome3y|normalizedNetIncome5y|normalizedNetIncomeYoy|op_cf_yoy|op_cf_yoy_avg_5y|operating_income_ebit_yoy|operating_income_ebit_yoy_avg_5y|operatingIncomeEbit10y|operatingIncomeEbit3y|operatingIncomeEbit5y|operatingIncomeEbitYoy|payout_ratio|pb_ratio|pe_nongaap_fy1|pe_ratio|price_cf_ratio|price_high_52w|price_low_52w|profitability_category|quant_rating|return_on_avg_tot_assets|return_on_total_capital|revenue_change_display|revenue_change_display_avg_5y|revenue_growth|revenue_growth_avg_5y|revenue_growth3|revenue_growth5|revenueGrowth10|roe|roe_change_display|roe_change_display_avg_5y|roe_yoy|roe_yoy_avg_5y|rtn_on_common_equity|sell_side_rating|shares|short_interest_percent_of_float|sma_10d|sma_200d|sma_50d|tangible_book_per_share|tangibleBookValue10y|tangibleBookValue3y|tangibleBookValue5y|tangibleBookValueYoy|tev|total_cash|total_debt|total_revenue|totalAssets10y|totalAssets3y|totalAssets5y|totalAssetsYoy|value_category|working_cap_change|working_cap_change_avg_5y')] = None,
                              algos: Annotated[Union[str, None], Field(description='One of the following, separated by comma for multiple options : main_quant,dividends')] = None) -> dict: 
    '''Get Profitability, Growth, etc... grade'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-metric-grades'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'fields': fields,
        'algos': algos,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_sector_metrics(symbol: Annotated[str, Field(description='Symbol to query for data, only one is allowed at a time.')],
                               fields: Annotated[Union[str, None], Field(description='One of the following, separated by comma for multiple options : altman_z_score|analysts_down_avg_5y|analysts_down_percent_avg_5y|analysts_up_avg_5y|analysts_up_percent_avg_5y|assets_turnover|authors_rating_pro|beta24|capex_change|capex_change_avg_5y|capex_to_sales|cash_from_operations_as_reported|cf_op_change_display|cf_op_change_display_avg_5y|coefficient_of_variation_90d|common_equity_10y|common_equity_3y|common_equity_5y|common_equity_yoy|degree_of_operating_leverage_ttm|diluted_eps_growth|diluted_eps_growth_avg_5y|dilutedEps10y|dilutedEps3y|dilutedEps5y|dilutedEpsGrowth|div_grow_rate10|div_grow_rate3|div_grow_rate5|div_growth_category|div_pay_date|div_rate_fwd|div_rate_ttm|div_yield_4y_avg_5y|div_yield_category_avg_5y|div_yield_fwd|div_yield_fwd_avg_5y|dividend_growth|dividend_lt_fwd_growth|dividend_per_share_change_dislpay|dividend_per_share_change_dislpay_avg_5y|dividend_yield|dividend_yield_avg_5y|dps_yoy|dps_yoy_avg_5y|earn_yield_gaap_fy1_avg_5y|earnings_yield_avg_5y|earningsGrowth|earningsGrowth10y|earningsGrowth3|earningsGrowth5y|ebit_change_display|ebit_change_display_avg_5y|ebit_margin|ebitda_10y|ebitda_3y|ebitda_5y|ebitda_change_display|ebitda_change_display_avg_5y|ebitda_margin|ebitda_yoy|ebitda_yoy_avg_5y|ebitdaYoy|eps_change_display|eps_change_display_avg_5y|eps_gaap_annual_growth_yoy|eps_gaap_annual_growth_yoy_avg_5y|eps_gaap_growth_3y_annual_fwd|eps_gaap_growth_3y_annual_fwd_avg_5y|eps_ltg|eps_ltg_avg_5y|eps_revisions_category|ev_12m_sales_ratio|ev_12m_sales_ratio_avg_5y|ev_ebit|ev_ebit_avg_5y|ev_ebit_fy1|ev_ebit_fy1_avg_5y|ev_ebitda|ev_ebitda_avg_5y|ev_ebitda_fy1|ev_ebitda_fy1_avg_5y|ev_sales_fy1|ev_sales_fy1_avg_5y|fcf_per_share_change_display|fcf_per_share_change_display_avg_5y|fcf_yield_avg_5y|fcf_yield_fy1_avg_5y|gross_loans_10y|gross_loans_3y|gross_loans_5y|gross_loans_yoy|gross_margin|growth_category|impliedmarketcap|last_div_date|last_price_vs_sma_10d|last_price_vs_sma_200d|last_price_vs_sma_50d|levered_fcf_margin|levered_free_cash_flow_yoy|levered_free_cash_flow_yoy_avg_5y|leveredFreeCashFlow10y|leveredFreeCashFlow3y|leveredFreeCashFlow5y|leveredFreeCashFlowYoy|log_of_unadjusted_stock_price|marketcap|marketcap_display|momentum_category|net_eps|net_inc_per_employee|net_income|net_interest_income_10y|net_interest_income_3y|net_interest_income_5y|net_interest_income_yoy|net_margin|netIncome10y|netIncome3y|netIncome5y|netIncomeYoy|normalizedNetIncome10y|normalizedNetIncome3y|normalizedNetIncome5y|normalizedNetIncomeYoy|op_cf_yoy|op_cf_yoy_avg_5y|oper_income_fy1_market_cap_avg_5y|oper_income_market_cap_avg_5y|operating_income_ebit_yoy|operating_income_ebit_yoy_avg_5y|operatingIncomeEbit10y|operatingIncomeEbit3y|operatingIncomeEbit5y|operatingIncomeEbitYoy|payout_ratio|pb_fy1_ratio|pb_fy1_ratio_avg_5y|pb_ratio|pb_ratio_avg_5y|pe_gaap_fy1|pe_gaap_fy1_avg_5y|pe_nongaap|pe_nongaap_avg_5y|pe_nongaap_fy1|pe_nongaap_fy1_avg_5y|pe_ratio|pe_ratio_avg_5y|peg_gaap|peg_gaap_avg_5y|peg_nongaap_fy1|peg_nongaap_fy1_avg_5y|price_cf_ratio|price_cf_ratio_avg_5y|price_cf_ratio_fy1|price_cf_ratio_fy1_avg_5y|price_high_52w|price_low_52w|profitability_category|ps_ratio|ps_ratio_avg_5y|ps_ratio_fy1|ps_ratio_fy1_avg_5y|quant_rating|return_on_avg_tot_assets|return_on_net_tangible_assets|return_on_total_capital|revenue_change_display|revenue_change_display_avg_5y|revenue_growth|revenue_growth_avg_5y|revenue_growth3|revenue_growth5|revenueGrowth10|roe|roe_change_display|roe_change_display_avg_5y|roe_yoy|roe_yoy_avg_5y|rtn_on_common_equity|sell_side_rating|shares|short_interest_percent_of_float|sma_10d|sma_200d|sma_50d|tangible_book_per_share|tangibleBookValue10y|tangibleBookValue3y|tangibleBookValue5y|tangibleBookValueYoy|tev|total_cash|total_debt|total_revenue|totalAssets10y|totalAssets3y|totalAssets5y|totalAssetsYoy|value_category|working_cap_change|working_cap_change_avg_5y|yld_on_cost_1y_avg_5y|yld_on_cost_3y_avg_5y|yld_on_cost_5y_avg_5y Separated by comma for multiple options. Ex : quant_rating,authors_rating_pro,sell_side_rating,marketcap,dividend_yield,etc...')] = None) -> dict: 
    '''Get Profitability, Growth, etc... metrics'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-sector-metrics'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'fields': fields,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_sec_filings(symbol: Annotated[str, Field(description='Symbol to query for data. Separating by comma to query multiple symbols at once, ex : aapl,tsla')],
                            filing_category: Annotated[Union[str, None], Field(description='One of the followings : all|financials|news|proxies|tenders|ownership|other')] = None,
                            number: Annotated[Union[int, float, None], Field(description='The page index for paging purpose Default: 1')] = None,
                            size: Annotated[Union[int, float, None], Field(description='The number of items per response for paging purpose Default: 20')] = None) -> dict: 
    '''Get sec filings of specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-sec-filings'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'filing_category': filing_category,
        'number': number,
        'size': size,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_chart(symbol: Annotated[str, Field(description='Symbol to query for data, only one is allowed at a time.')],
                      period: Annotated[Union[str, None], Field(description='One of the following : 1D|5D|1M|6M|YTD|1Y|3Y|5Y|10Y|MAX')] = None) -> dict: 
    '''Get data to draw chart for specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-chart'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'period': period,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_chart(symbols: Annotated[str, Field(description='Symbol to query for data. Separating by comma to query multiple symbols at once, ex : aapl,tsla')],
                 start: Annotated[Union[str, datetime], Field(description='Starting date to query for data, the format is yyyy-MM-dd')],
                 end: Annotated[Union[str, datetime], Field(description='Ending date to query for data, the format is yyyy-MM-dd')],
                 metrics: Annotated[Union[str, None], Field(description='One of the following : total_revenue|ebitda_yoy|net_income|diluted_eps_growth|pe_ratio|pb_ratio|price_cf_ratio|ps_ratio|price_tang_book|ev_ebit|ev_12m_sales_ratio|enterprise_value|ev_ebitda|market_cap|gross_margin|net_margin|operating_income_ebit_yoy|normalized_net_income|tangible_book|total_assets|levered_free_cash_flow_yoy|diluted_weighted_average_shares_outstanding|ebit_margin|normalized_net_income_margin|ebitda_margin|levered_fcf_margin|return_on_equity|return_on_avg_tot_assets|return_on_total_capital|assets_turnover|net_interest_income|gross_loans|total_common_equity|sga_margin|ebt_margin|net_interest_income_per_total_revenue')] = None) -> dict: 
    '''This endpoint reproduces public data and features in Charting tab.'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/v2/get-chart'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbols': symbols,
        'start': start,
        'end': end,
        'metrics': metrics,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_estimates(symbol: Annotated[str, Field(description='Symbol to query for data, only one is allowed at a time.')],
                          data_type: Annotated[Union[str, None], Field(description='One of the following : eps|revenues')] = None,
                          period_type: Annotated[Union[str, None], Field(description='One of the following : quarterly|annual')] = None) -> dict: 
    '''Get estimated EPS/revenue of specific symbol by annual or quarterly'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-estimates'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'data_type': data_type,
        'period_type': period_type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_holdings(symbols: Annotated[str, Field(description='Symbol to query for data. Separating by comma to query multiple symbols at once, ex : aapl,tsla')]) -> dict: 
    '''Get information in Holdings tab of specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-holdings'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbols': symbols,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_estimated_earning_announces(symbol: Annotated[str, Field(description='Symbol to query for data. Ex : AAPL')]) -> dict: 
    '''Get estimated earning announces of a symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-estimated-earning-announces'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_earnings(ticker_ids: Annotated[str, Field(description='The value of id fields returned in .../symbols/get-meta-data endpoint. Separating by comma to query multiple tickers at once, ex : 1742,146')],
                         period_type: Annotated[Union[str, None], Field(description='One of the followings : quarterly|annual')] = None,
                         relative_periods: Annotated[Union[str, None], Field(description='Valid range -23,...,-2,-1,0,1,2,..,23')] = None,
                         estimates_data_items: Annotated[Union[str, None], Field(description='One of the followings : eps_gaap_actual,eps_gaap_consensus_mean,eps_normalized_actual,eps_normalized_consensus_mean,revenue_actual,revenue_consensus_mean,eps_primary,revenue_consensus_low,revenue_consensus_high,revenue_num_of_estimates . Separated by comma for multiple options')] = None,
                         revisions_data_items: Annotated[Union[str, None], Field(description='One of the followings : eps_normalized_actual,eps_normalized_consensus_mean,revenue_consensus_mean . Separated by comma for multiple options')] = None,
                         group_by_month: Annotated[Union[bool, None], Field(description='true|false')] = None,
                         return_window: Annotated[Union[int, float, None], Field(description='Default: 0')] = None) -> dict: 
    '''Get information in Earnings tab of specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-earnings'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker_ids': ticker_ids,
        'period_type': period_type,
        'relative_periods': relative_periods,
        'estimates_data_items': estimates_data_items,
        'revisions_data_items': revisions_data_items,
        'group_by_month': group_by_month,
        'return_window': return_window,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_analyst_price_target(ticker_ids: Annotated[str, Field(description='The value of id field returned in .../symbols/get-meta-data')],
                                     return_window: Annotated[Union[int, float, None], Field(description='The return window Default: 1')] = None,
                                     group_by_month: Annotated[Union[bool, None], Field(description='Whether or not the data is grouped by month')] = None) -> dict: 
    '''Get Wall Street analyst price target for specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-analyst-price-target'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker_ids': ticker_ids,
        'return_window': return_window,
        'group_by_month': group_by_month,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_analyst_recommendations(ticker_ids: Annotated[str, Field(description='The value of id field returned in .../symbols/get-meta-data')],
                                        return_window: Annotated[Union[int, float, None], Field(description='The return window Default: 3')] = None,
                                        group_by_month: Annotated[Union[bool, None], Field(description='Whether or not the data is grouped by month')] = None) -> dict: 
    '''Get Wall Street analyst recommendations for specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-analyst-recommendations'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker_ids': ticker_ids,
        'return_window': return_window,
        'group_by_month': group_by_month,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_key_data(symbol: Annotated[str, Field(description='Symbol to query for data, only one is allowed at a time.')]) -> dict: 
    '''Get key data of specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-key-data'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_quant_rating_histories(symbol: Annotated[str, Field(description='Symbol to query for data, only one is allowed at a time.')],
                                       number: Annotated[Union[int, float, None], Field(description='For paging purpose Default: 1')] = None) -> dict: 
    '''Get quant rating histories for specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-quant-rating-histories'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'number': number,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_analyst_ratings(symbol: Annotated[str, Field(description='Symbol to query for data, only one is allowed at a time.')]) -> dict: 
    '''Get Wall Street analyst ratings for specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-analyst-ratings'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_factor_grades(symbol: Annotated[str, Field(description='Symbol to query for data, only one is allowed at a time.')]) -> dict: 
    '''Get factor grades for specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-factor-grades'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_top_holdings(symbol: Annotated[str, Field(description='Symbol to query for data. Separating by comma to query multiple symbols at once, ex : aapl,tsla')]) -> dict: 
    '''Get top holdings of specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-top-holdings'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_momentum(symbols: Annotated[str, Field(description='Symbol to query for data. Separating by comma to query multiple symbols at once, ex : aapl,tsla')]) -> dict: 
    '''Get momentum of specific symbol * This endpoint is deprecated, you need to use .../symbols/v2/get-momentum endpoint instead.'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-momentum'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbols': symbols,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_ratings(symbol: Annotated[str, Field(description='Symbol to query for data, only one is allowed at a time.')]) -> dict: 
    '''Get ratings data for specific symbol * This endpoint is replaced by .../symbols/get-factor-grades and .../symbols/get-quant-rating-histories'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-ratings'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols_get_options(Identifier: Annotated[str, Field(description='Symbol to query for data, only one is allowed at a time.')],
                        Month: Annotated[Union[int, float], Field(description='Default: 3')],
                        Year: Annotated[Union[int, float], Field(description='Default: 2023')],
                        IdentifierType: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get optional prices'''
    url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-options'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'Identifier': Identifier,
        'Month': Month,
        'Year': Year,
        'IdentifierType': IdentifierType,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_list(id: Annotated[str, Field(description='Symbol to query for data, only one is allowed at a time.')],
            until: Annotated[Union[int, float, None], Field(description="Unix timestamp (Epoch timestamp), ex : 1636693199 Maybe use together with 'since' parameter to filter data by date range Default: 0")] = None,
            since: Annotated[Union[int, float, None], Field(description="Unix timestamp (Epoch timestamp), ex : 1636693199 Maybe use together with 'until' parameter to filter data by date range Default: 0")] = None,
            size: Annotated[Union[int, float, None], Field(description='The number of items per response (max 40) Default: 20')] = None,
            number: Annotated[Union[int, float, None], Field(description='Page index for paging purpose Default: 1')] = None) -> dict: 
    '''List analysis of specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/analysis/v2/list'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'until': until,
        'since': since,
        'size': size,
        'number': number,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_details(id: Annotated[Union[int, float], Field(description='The value of id returned in .../analysis/list endpoint Default: 4341786')]) -> dict: 
    '''Get analysis detail by id'''
    url = 'https://seeking-alpha.p.rapidapi.com/analysis/v2/get-details'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def analysis_get_details(id: Annotated[Union[int, float], Field(description='The value of id returned in .../analysis/list endpoint Default: 4341786')]) -> dict: 
    '''Get analysis detail by id * This endpoint is deprecating. Use .../analysis/v2/get-details instead'''
    url = 'https://seeking-alpha.p.rapidapi.com/analysis/get-details'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def analysis_list(id: Annotated[str, Field(description='Symbol to query for data, only one is allowed at a time.')],
                  until: Annotated[Union[int, float, None], Field(description='The value of meta/page/minmaxPublishOn/min json object returned right in this endpoint to load next page Default: 0')] = None,
                  size: Annotated[Union[int, float, None], Field(description='The number of items per response Default: 20')] = None) -> dict: 
    '''List analysis of specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/analysis/list'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'until': until,
        'size': size,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_list_trending(until: Annotated[Union[int, float, None], Field(description="Unix timestamp (Epoch timestamp), ex : 1636693199 Maybe use together with 'since' parameter to filter data by date range Default: 0")] = None,
                     since: Annotated[Union[int, float, None], Field(description="Unix timestamp (Epoch timestamp), ex : 1636693199 Maybe use together with 'until' parameter to filter data by date range Default: 0")] = None,
                     size: Annotated[Union[int, float, None], Field(description='The number of items per response (max 40) Default: 20')] = None) -> dict: 
    '''List trending articles'''
    url = 'https://seeking-alpha.p.rapidapi.com/articles/v2/list-trending'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'until': until,
        'since': since,
        'size': size,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def articles_list_wall_street_breakfast() -> dict: 
    '''List articles by category'''
    url = 'https://seeking-alpha.p.rapidapi.com/articles/list-wall-street-breakfast'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def articles_get_details(id: Annotated[Union[int, float], Field(description='The value of id returned in .../articles/list or .../articles/list-trending or .../articles/list-wall-street-breakfast endpoints Default: 4349447')]) -> dict: 
    '''Get analysis detail by id'''
    url = 'https://seeking-alpha.p.rapidapi.com/articles/get-details'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def articles_list(category: Annotated[str, Field(description='One of the following : etfs-and-funds|latest-articles|stock-ideas|editors-picks|stock-ideas::editors-picks|dividends|investing-strategy|dividends::reits|podcast|market-outlook')],
                  until: Annotated[Union[int, float, None], Field(description='The value of meta/page/minmaxPublishOn/min json object returned right in this endpoint to load next page Default: 0')] = None,
                  size: Annotated[Union[int, float, None], Field(description='The number of items per response Default: 20')] = None) -> dict: 
    '''List articles by category'''
    url = 'https://seeking-alpha.p.rapidapi.com/articles/list'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'category': category,
        'until': until,
        'size': size,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def articles_list_trending() -> dict: 
    '''List trending articles'''
    url = 'https://seeking-alpha.p.rapidapi.com/articles/list-trending'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_list_by_symbol(id: Annotated[str, Field(description='Symbol to query for data, only one is allowed at a time')],
                      until: Annotated[Union[int, float, None], Field(description="Unix timestamp (Epoch timestamp), ex : 1636693199 Maybe use together with 'since' parameter to filter data by date range Default: 0")] = None,
                      since: Annotated[Union[int, float, None], Field(description="Unix timestamp (Epoch timestamp), ex : 1636693199 Maybe use together with 'until' parameter to filter data by date range Default: 0")] = None,
                      size: Annotated[Union[int, float, None], Field(description='The number of items per response (max 40) Default: 20')] = None,
                      number: Annotated[Union[int, float, None], Field(description='Page index for paging purpose Default: 1')] = None,
                      category: Annotated[Union[str, None], Field(description='One of the following : dividend_news|earnings_news|m_n_a_news')] = None) -> dict: 
    '''List news by symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/news/v2/list-by-symbol'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'until': until,
        'since': since,
        'size': size,
        'number': number,
        'category': category,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def news_get_details(id: Annotated[Union[int, float], Field(description='The value of id returned in .../news/list or .../news/list-trending endpoint Default: 3577036')]) -> dict: 
    '''Get analysis detail by id'''
    url = 'https://seeking-alpha.p.rapidapi.com/news/get-details'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def news_list(id: Annotated[str, Field(description='Symbol to query for data, only one is allowed at a time.')],
              until: Annotated[Union[int, float, None], Field(description='The value of meta/page/minmaxPublishOn/min json object returned right in this endpoint to load next page Default: 0')] = None,
              size: Annotated[Union[int, float, None], Field(description='The number of items per response Default: 20')] = None) -> dict: 
    '''List news of specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/news/list'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'until': until,
        'size': size,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def news_list_trending() -> dict: 
    '''List latest trending news'''
    url = 'https://seeking-alpha.p.rapidapi.com/news/list-trending'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def press_releases_get_details(id: Annotated[Union[int, float], Field(description='The value of id returned in .../press-releases/v2/list endpoint Default: 17867968')]) -> dict: 
    '''Get press release detail by id'''
    url = 'https://seeking-alpha.p.rapidapi.com/press-releases/get-details'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def press_releases_list(id: Annotated[str, Field(description='Symbol to query for data, only one is allowed at a time.')],
                        until: Annotated[Union[int, float, None], Field(description='The value of meta/page/minmaxPublishOn/min json object returned right in this endpoint to load next page Default: 0')] = None,
                        size: Annotated[Union[int, float, None], Field(description='The number of items per response Default: 20')] = None) -> dict: 
    '''List press releases of specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/press-releases/list'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'until': until,
        'size': size,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def transcripts_get_details(id: Annotated[Union[int, float], Field(description='The value of id returned in .../transcripts/list endpoint Default: 4341792')]) -> dict: 
    '''Get transcript detail by id * This endpoint is deprecating. Use .../transcripts/v2/get-details instead'''
    url = 'https://seeking-alpha.p.rapidapi.com/transcripts/get-details'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def transcripts_list(id: Annotated[str, Field(description='Symbol to query for data, only one is allowed at a time.')],
                     until: Annotated[Union[int, float, None], Field(description='The value of meta/page/minmaxPublishOn/min json object returned right in this endpoint to load next page Default: 0')] = None,
                     size: Annotated[Union[int, float, None], Field(description='The number of items per response Default: 20')] = None) -> dict: 
    '''List transcripts of specific symbol'''
    url = 'https://seeking-alpha.p.rapidapi.com/transcripts/list'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'until': until,
        'size': size,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def comments_get_contents(id: Annotated[Union[int, float], Field(description='The value of id returned in .../articles/list or .../articles/list-trending or .../articles/list-wall-street-breakfast endpoints Default: 4469484')],
                          comment_ids: Annotated[Union[int, float], Field(description='The value of id field returned in .../comments/v2/list endpoint. You may pass this parameter multiple times to get content of many comments at once. Ex : ...&comment_ids=90666350&comment_ids=90666780&... Default: 90666350')],
                          sort: Annotated[Union[str, None], Field(description='Order by newest : -top_parent_id | Order by oldest : leave empty')] = None) -> dict: 
    '''This endpoint is used to get many comment's content at once by comment ids.'''
    url = 'https://seeking-alpha.p.rapidapi.com/comments/get-contents'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'comment_ids': comment_ids,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def comments_get_sub_comments(id: Annotated[Union[int, float], Field(description='The value of id returned in .../articles/list or .../articles/list-trending or .../articles/list-wall-street-breakfast endpoints Default: 90949998')],
                              sort: Annotated[Union[str, None], Field(description='Order by newest : -top_parent_id | Order by oldest : leave empty')] = None) -> dict: 
    '''This endpoint is used to get sub or nested comments of another comment'''
    url = 'https://seeking-alpha.p.rapidapi.com/comments/get-sub-comments'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def comments_list(id: Annotated[Union[int, float], Field(description='The value of id returned in .../articles/list or .../articles/list-trending or .../articles/list-wall-street-breakfast endpoints Default: 4405526')],
                  from_id: Annotated[Union[int, float, None], Field(description='Leave empty to load the first page or get suitable value of the last comment id returned right in this endpoint with parentId being "null" to load the next page Default: 88004158')] = None,
                  parent_count: Annotated[Union[int, float, None], Field(description='For paging purpose (max 20) Default: 20')] = None,
                  sort: Annotated[Union[str, None], Field(description='Order by newest : -top_parent_id | Order by oldest : leave empty')] = None) -> dict: 
    '''List all comments relating to a post or article or news'''
    url = 'https://seeking-alpha.p.rapidapi.com/comments/list'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'from_id': from_id,
        'parent_count': parent_count,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def screeners_list() -> dict: 
    '''List all screeners (Top Rated Stocks, Top Quant Dividend Stocks, Top Yield Monsters, etc...)'''
    url = 'https://seeking-alpha.p.rapidapi.com/screeners/list'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def screener_filters_list() -> dict: 
    '''List available filters to be used in .../screeners/get-results endpoint'''
    url = 'https://seeking-alpha.p.rapidapi.com/screener-filters/list'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def screeners_detail(id: Annotated[str, Field(description='The value of id field returned in .../screeners/list endpoint')]) -> dict: 
    '''Get more information of a screener'''
    url = 'https://seeking-alpha.p.rapidapi.com/screeners/detail'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def screeners_get_results(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Get results of symbols by applied filters relating to a screener'''
    url = 'https://seeking-alpha.p.rapidapi.com/screeners/get-results'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def accounts_get_access_token(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Get access token by using own account from SA. The token is used to pass via request header while calling other endpoints. *The API does not support login by Google, or Apple.'''
    url = 'https://seeking-alpha.p.rapidapi.com/accounts/get-access-token'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def accounts_get_info() -> dict: 
    '''Get account information with access token'''
    url = 'https://seeking-alpha.p.rapidapi.com/accounts/get-info'
    headers = {'x-rapidapi-host': 'seeking-alpha.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
