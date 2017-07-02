# BrowserCtrl
<b>内部にBigWorldで用意されているブラウザにWebページを表示するプログラム</b>  
Button 1にhttp://www.wgmods.net を、Button 2にhttp://koreanrandom.com を表示するようにしてあります  

現時点での問題点・改善点（？）  
- Button 1でのブラウザ表示と、Button 2でのブラウザ表示を統一しているためブラウザウィンドウ２個を表示することができない  
↑解決,それぞれのブラウザ呼び出し時の引数、`browserID` の名前を変えることにより複数表示が可能
- Buttonに画像を配置してみたい
