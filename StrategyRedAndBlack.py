from queue import Queue
import unicorn_binance_websocket_api as unicorn


def main():
    trigger_buy_sell = 'buy', 'sell'
    sum_profit = 0
    q = Queue(maxsize=2)
    q.queue.clear()
    ubwa = unicorn.BinanceWebSocketApiManager(exchange='binance.com')
    ubwa.create_stream('kline_1m', 'BTCUSDT', output='UnicornFy')

    while True:
        data = ubwa.pop_stream_data_from_stream_buffer()
        if data and len(data) > 3 and data['kline']['is_closed']:
            q.put(float(data['kline']['close_price']))
            print(data['kline'])
            if trigger_buy_sell == 'buy':
                profit = float(data['kline']['close_price']) - float(q.queue[0])
                sum_profit = sum_profit + profit
            elif trigger_buy_sell == 'sell':
                profit = -1*(float(data['kline']['close_price']) - float(q.queue[0]))
                sum_profit = sum_profit + profit
            print(f'Sum profit in points: '+str("%.8f" % sum_profit)+'\n')
            if q.full():
                if q.queue[0] < q.queue[1]:
                    trigger_buy_sell = 'buy'
                    print('Bought for the price: '+str(q.queue[1]))
                    q.get()
                else:
                    trigger_buy_sell = 'sell'
                    print('Sold at the price: '+str(q.queue[1]))
                    q.get()


if __name__ == "__main__":
    main()
