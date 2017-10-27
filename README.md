# これは何

「AB Shutter 3」という安価なIoTボタン(正確にはリモートでシャッター押すためのボタン)で遊んだ。


## そもそも AB Shutter 3とは

 * 公式には Remote Shutter でiOS, Androidのカメラシャッターをリモートで押すボタン
 * ダイソーに300円売っている。ネットだと何故か送料込みでも100円切ることがある
   * 1円という時期があったらしい。
 * 電池としてボタン電池のRS2032が別途要る
 * HIDキーボードとして認識される
   * ボタン二つはそれぞれVolume-upとEnterとマッピングされている
 * 数分で電源が切れるため、IoTボタンとして使う場合は「起動」と「操作」で大体2回押さないとダメ
 * 作りが安っぽい


色々記事があるので詳細はそちらで

 * https://shkspr.mobi/blog/2016/02/cheap-bluetooth-buttons-and-linux/
   * 役に立つ
 * https://qiita.com/vimyum/items/8b7548ca8cf45383c5b0
   * きっかけになったがラズパイだけか？
   * 動作しなかった
 * https://qiita.com/shskwmt/items/fffabf521201f5835214
   * ここから学ぶ必要があった
 * http://d.hatena.ne.jp/wakwak_koba/20170831


## ツールの使い方

BTのUSBドングルを差したLinux(Ubuntu 16.04 LTS)で動作確認

python-bluezの関係でPython 2。virtualenvするなら `apt install python-dev libbluetooth-dev`あたりも必要そう。

bluetoothctlの使い方は省略。ペアリングしてある状態で、かつ電源が入っていれば

```
(venv)$ pip freeze
click==6.7
Flask==0.12.2
itsdangerous==0.24
Jinja2==2.9.6
MarkupSafe==1.0
pkg-resources==0.0.0
PyBluez==0.22
Werkzeug==0.12.2
(venv)$ lookup_device.py XX:XX:XX:XX:XX:XX
Device detected
(venv)$ BUTTON_DEVICE=XX:XX:XX:XX:XX:XX ./server.py
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
(ブラウザでアクセスすると、接続されていればアドレスが表示される。セキュリティとかの考慮は皆無)
```

## 注意

なおこのツールでは「ボタンを押す」操作は確認しない。

単にペアリングをサーバサイドから確認出来たレベルで満足しているので、ボタン操作を認識するにはもっと実装が必要。
