from classification_model.predict import make_prediction


def test_make_prediction(sample_input_data):
    expected_first_prediction_value = True
    expected_no_predictions = 107

    result = make_prediction(input_data=sample_input_data)

    predictions = result.get("predictions")
    assert isinstance(predictions, list)
    assert result.get("errors") is None
    assert len(predictions) == expected_no_predictions
    assert predictions[0] == expected_first_prediction_value
