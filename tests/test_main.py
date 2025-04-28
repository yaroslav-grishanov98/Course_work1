from unittest.mock import patch


@patch("src.main.generate_main_page_response")
def test_main_page_command_line(mock_generate_main):
    """Тест вызова скрипта для страницы main"""
    expected_response = {"greeting": "Тестовое приветствие"}
    mock_generate_main.return_value = expected_response

    with patch("sys.argv", ["src/main.py", "--page", "main", "--date", "2025-04-15"]):
        from src.main import main

        response = main()

        mock_generate_main.assert_called_once()
        assert response == expected_response


@patch("src.main.generate_events_page_response")
def test_events_page_command_line(mock_generate_events):
    """Тест вызова скрипта для страницы events"""
    expected_response = {"expenses": {"total_amount": 1000}}
    mock_generate_events.return_value = expected_response

    periods = ["W", "M", "Y", "ALL"]

    for period in periods:
        mock_generate_events.reset_mock()
        with patch(
            "sys.argv",
            ["src/main.py", "--page", "events", "--date", "2025-04-15", "--period", period],
        ):
            from src.main import main

            response = main()

            mock_generate_events.assert_called_once()
            assert response == expected_response
