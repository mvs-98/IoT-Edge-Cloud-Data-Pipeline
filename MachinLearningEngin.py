# from ml_engine import MLPredictor
#
# if __name__ == '__main__':
#     # Prepare data
#     data = {
#     'Timestamp': ['2020-09-01', '2020-09-02', '2020-09-03',
#                   '2020-09-04', '2020-09-05'],
#     'Value': [1, 2, 1, 10, 5]
#     }
#     data_df = pd.DataFrame(data)
#     # Create ML engine predictor object
#     predictor = MLPredictor(data_df)
#     # Train ML model
#     predictor.train()
#     # Do prediction
#     forecast = predictor.predict()
#
#     # Get canvas
#     fig = predictor.plot_result(forecast)
#     fig.savefig("prediction.png")
#     fig.show()