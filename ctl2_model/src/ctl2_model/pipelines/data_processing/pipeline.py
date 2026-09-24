"""data_processing pipeline."""
from kedro.pipeline import node, Pipeline, pipeline
from .nodes import preprocess_and_augment


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=preprocess_and_augment,
            inputs=["ctl2_model_data_loaded", "params:data_processing", "params:load_data"],
            outputs=[
                "processed_X_train",
                "processed_X_train_aug",
                "processed_y_train",
                "processed_met_train",
                "processed_X_val",
                "processed_y_val",
                "processed_met_val",
                "processed_X_eval",
                "processed_y_eval",
                "processed_met_eval",
            ],
            name="data_processing_node",
        ),
    ])
