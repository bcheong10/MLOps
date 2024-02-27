from pipelines.training_pipeline import train_pipeline
from zenml.client import Client

if __name__ == "__main__":
    # Run the pipeline
    print(Client().active_stack.experiment_tracker.get_tracking_uri())
    train_pipeline(data_path='data\olist_customers_dataset.csv')

    # mlflow ui --backend-store-uri "file:C:\Users\bcheo\AppData\Roaming\zenml\local_stores\4d29fd51-3d12-4f77-9311-6117630cb8e4\mlruns"