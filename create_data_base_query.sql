CREATE TABLE register_of_call_and_put_actions (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(100),
    candle_date datetime,
    open_value float,
    close_value float,
    action_type VARCHAR(100),
    call_or_put VARCHAR(100),
    strike float,
    ask_price float,
    bid_price float,
    status_of_action VARCHAR(100),
    order_date TIMESTAMP NULL
);