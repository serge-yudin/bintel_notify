# bintel_notify

A simply notify service about the current price  of the chosen COIN on Binance. If the price changes more than 5 percent, you'll receive a picture containing the actual coin's  price and change percentage in your telegram

<h3>Installation</h3>
<ul>
  <li>Clone this repo <code>git clone https://github.com/serge-yudin/bintel_notify</code>
  <li>run <code>pip3 install -r requirements.txt</code>
  <li>Set a cronjob for every n - minutes/hours <code>crontab -e</code>
  <pre>*/5 * * * * cd /path/to/dir; /usr/bin/python3 calc_difference.py >> /path/to/log-file.txt 2>&1</pre>
</ul>
