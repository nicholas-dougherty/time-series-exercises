```
    ███      ▄█    ▄▄▄▄███▄▄▄▄      ▄████████                                          
▀█████████▄ ███  ▄██▀▀▀███▀▀▀██▄   ███    ███                                          
   ▀███▀▀██ ███▌ ███   ███   ███   ███    █▀                                           
    ███   ▀ ███▌ ███   ███   ███  ▄███▄▄▄                                              
    ███     ███▌ ███   ███   ███ ▀▀███▀▀▀                                              
    ███     ███  ███   ███   ███   ███    █▄                                           
    ███     ███  ███   ███   ███   ███    ███                                          
   ▄████▀   █▀    ▀█   ███   █▀    ██████████                                          
   ▄████████    ▄████████    ▄████████  ▄█     ▄████████    ▄████████                  
  ███    ███   ███    ███   ███    ███ ███    ███    ███   ███    ███                  
  ███    █▀    ███    █▀    ███    ███ ███▌   ███    █▀    ███    █▀                   
  ███         ▄███▄▄▄      ▄███▄▄▄▄██▀ ███▌  ▄███▄▄▄       ███                         
▀███████████ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ███▌ ▀▀███▀▀▀     ▀███████████                  
         ███   ███    █▄  ▀███████████ ███    ███    █▄           ███                  
   ▄█    ███   ███    ███   ███    ███ ███    ███    ███    ▄█    ███                  
 ▄████████▀    ██████████   ███    ███ █▀     ██████████  ▄████████▀                   
                            ███    ███                                                 
   ▄████████ ███▄▄▄▄      ▄████████  ▄█       ▄██   ▄      ▄████████  ▄█     ▄████████ 
  ███    ███ ███▀▀▀██▄   ███    ███ ███       ███   ██▄   ███    ███ ███    ███    ███ 
  ███    ███ ███   ███   ███    ███ ███       ███▄▄▄███   ███    █▀  ███▌   ███    █▀  
  ███    ███ ███   ███   ███    ███ ███       ▀▀▀▀▀▀███   ███        ███▌   ███        
▀███████████ ███   ███ ▀███████████ ███       ▄██   ███ ▀███████████ ███▌ ▀███████████ 
  ███    ███ ███   ███   ███    ███ ███       ███   ███          ███ ███           ███ 
  ███    ███ ███   ███   ███    ███ ███▌    ▄ ███   ███    ▄█    ███ ███     ▄█    ███ 
  ███    █▀   ▀█   █▀    ███    █▀  █████▄▄██  ▀█████▀   ▄████████▀  █▀    ▄████████▀  
                                    ▀                                                  
```
# Time Series:
## Analyzing, Modeling, & Forecasting Temporal Events
***
Time series analysis is about finding patterns in temporal data and making predictions, or forecasting, based on those patterns.

Why is this different from basic regression? In short, time is dependent. This means that each feature, that is, each new point in time, is dependent on the previous features. In time series, the previous features are the historical points in time.
***
### Time Series use-cases

Common use-case and domains where time series is common includes sales and revenue, signal processing, speech & chatbots, economics, healthcare, stock values, census analysis, supply chain, and staffing. 

Examples of questions or requests that might arise related to sales and revenue include:

- Given historical customer invoices, calculate a firm's SaaS metrics, perform a cohort analysis on growth & churn, and develop a basic per-product line revenue forecast.
- Given historical customer invoices, determine predictors of growth. How does this change over time?
- Based on usage & support data, are there any unlikely predictors of growth or churn? Which customers are the most interesting?
- Which customers are expected to grow at least 20% over the next few months?
***
### Time series vocabulary

- Temporal: Relating to time
- Periodic: Occurring at intervals
- Resampling in Time Sereis: Changing the frequency of your data points
- Stationary Process: Distribution does not change over time
- Trend: Long term progression (increasing or decreasing, for example)
- Seasonality: Changes in patterns due to seasonal factors
- Heteroskedasticity: Changes in variance over time
- Autocorrelation: A correlation coefficient, but instead of between two different variables, it is between the values of the same variable at two different times
***
### Skills specific to time series

- Working with datetimes
- Resampling methods
- Test/Train Split sklearn.model_selection.TimeSeriesSplit.
- Identifying seasonality
- Maintaining a time series model: We can predict using new data as input as you move along, or we can use the predictions themselves which leads to much less stable predictions.
- Visualizing Time Series Data: Line Charts, Stacked Area Chart, Scatter Plot, Stream Graph, Heat Map, Polar Area Diagram
***
### Modeling time series data

Stats-based methods for forecasting are based on statistical models and require underlying assumptions of the data to be upheld. Pros of going with stats-based methods are that they are SIC - Simple, Interpretable, Capture the trend. Cons include limitations in seasonality, high risk of overfitting, reliance on underlying assumptions about the time series. Common stats-based methods include:

- Persistence or Naive Model: Use the last n-observations assigned to the test set to make n-forecasts using a walk-forward validation model.
- Simple Average: Use the average as the prediction for the next value.
- Moving Average: Use the average over the last n-time periods only, when the most recent values are what matter the most. This will create a moving window of n-time periods. This could be done for the same month over each year, or in other ways that are not continuous.
- Time Series Decomposition: De-trending by differencing, i.e. just looking at whether it's going up or down.
- Variance Stabilization: Transform using log, square root, or box-cox transformations. The noise is reduced and the data gets much more uniform.
- Exponential Smoothing: Apply larger weights to the more recent values, but not eliminate the earlier values totally (like in moving average). This uses weighted averages to forecast.
- Holt's Linear Trend Method: Exponential smoothing applied to both the average and the trend (slope).
- Holt-Winters Method: Exponential smoothing applied to both the average and the trend (slope) WITH seasonality. Extract a combination of patterns at varying frequencies, such as daily, weekly, seasonally, and yearly, along with an overall trend so that we can then use linear regression.