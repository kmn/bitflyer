# Bitflyer: Bitflyer Api Library

bitflyer は [bitflyer](https://bitfyer.jp) の python 製 api ライブラリです. 

```
> from bitflyer import public
> p1 = public.Public()
> p1.ticker()
{'volume_by_product': 2965.84952775, 'best_ask': 44689.0, 'timestamp': '2016-02-04T05:30:31.763', 'product_code': 'BTC_JPY', 'tick_id': 137706, 'best_ask_size': 0.016, 'volume': 5333.87259331, 'total_bid_depth': 679.52073, 'best_bid_size': 2.4, 'ltp': 44700.0, 'total_ask_depth': 1144.14296596, 'best_bid': 44670.0}
```

## Documentation

Documentation for Bitflyer API is  available at https://lightning.bitflyer.jp/docs?lang=ja

### Public

#### 板情報

[板情報](https://lightning.bitflyer.jp/docs?lang=ja#板情報) を取得します.

```
>> from bitflyer import public
>> print(public.Public().getboard())
{'asks':...
```

詳細は[こちら](https://lightning.bitflyer.jp/docs?lang=ja#板情報).

#### Ticker

```
>> from bitflyer import public
>> print(public.Public().getticker())
{'timestamp': '2016-02-04T05:47:26.64', 'best_bid': 44711.0, 'product_code': 'BTC_JPY', 'total_bid_depth': 785.91873, 'best_ask': 44725.0, 'ltp': 44750.0, 'best_bid_size': 1.667, 'total_ask_depth': 735.61096596, 'volume': 5344.37969331, 'volume_by_product': 2975.34662775, 'tick_id': 139547, 'best_ask_size': 0.013}
```

[ticker](https://lightning.bitflyer.jp/docs?lang=ja#ticker) を取得します.

詳細は[こちら](https://lightning.bitflyer.jp/docs?lang=ja#ticker).

#### 約定履歴

約定履歴を取得します.

```
>> from bitflyer import public
>> print(public.Public().getexecutions())
[{'size': 1.618, 'buy_child_order_acceptance_id':...
```

詳細は[こちら](https://lightning.bitflyer.jp/docs?lang=ja#約定履歴).


#### 取引所の状態

[取引所の状態](https://lightning.bitflyer.jp/docs?lang=ja#取引所の状態) を取得します.

```
>> from bitflyer import public
>> print(public.Public().gethealth())
{'status': 'NORMAL'}
```
詳細は[こちら](https://lightning.bitflyer.jp/docs?lang=ja#取引所の状態).

 
### Private

#### 資産残高を取得


```
>> from bitflyer import private
>> p = private.Private(access_key='YOUR_ACCESS_KEY',secret_key='YOUR_SECRET_KEY')
>> p.getbalance()
{'status_code': 200, 'response': ....}
```

#### 証拠金の状態を取得

```
>> from bitflyer import private
>> p = private.Private(access_key='YOUR_ACCESS_KEY',secret_key='YOUR_SECRET_KEY')
>> p.getcollateral()
{'status_code': 200, 'response': ....}
```

#### 新規注文を出す

```
>> from bitflyer import private
>> p = private.Private(access_key='YOUR_ACCESS_KEY',secret_key='YOUR_SECRET_KEY')
>> p.sendchildorder()
{'status_code': 200, 'response': ....}
```

#### 注文をキャンセルする

```
>> from bitflyer import private
>> p = private.Private(access_key='YOUR_ACCESS_KEY',secret_key='YOUR_SECRET_KEY')
>> p.cancelchildorder()
{'status_code': 200, 'response': ....}
```

#### 新規の親注文を出す（特殊注文）

未実装

#### 親注文をキャンセルする

未実装

#### すべての注文をキャンセルする

```
>> from bitflyer import private
>> p = private.Private(access_key='YOUR_ACCESS_KEY',secret_key='YOUR_SECRET_KEY')
>> p.cancelallchildorders()
{'status_code': 200, 'response': ....}
```


#### 注文の一覧を取得

```
>> from bitflyer import private
>> p = private.Private(access_key='YOUR_ACCESS_KEY',secret_key='YOUR_SECRET_KEY')
>> p.getchildorders()
{'status_code': 200, 'response': ....}
```

#### 親注文の一覧を取得

未テスト

#### 親注文の詳細を取得

未テスト

#### 約定の一覧を取得

```
>> from bitflyer import private
>> p = private.Private(access_key='YOUR_ACCESS_KEY',secret_key='YOUR_SECRET_KEY')
>> p.getexecutions()
{'status_code': 200, 'response': ....}
```


#### 建玉の一覧を取得

```
>> from bitflyer import private
>> p = private.Private(access_key='YOUR_ACCESS_KEY',secret_key='YOUR_SECRET_KEY')
>> p.getpositions()
{'status_code': 200, 'response': ....}
```


## TODO

- 親注文
