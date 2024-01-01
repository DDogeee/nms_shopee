# Prerequisite
- Conda
- Tor
- Privoxy

# Install Tor and Privoxy
```
sudo apt-get update
sudo apt-get install tor tor-geoipdb privoxy
```

# Configuring Tor and Privoxy

Add below code at the end of `/etc/tor/torrc`
```
ControlPort 9051
CookieAuthentication 0
```

Add below code at the end of `/etc/privoxy/config`
```
forward-socks5t / 127.0.0.1:9050 .
```
# Restart Tor and Privoxy
```
sudo service privoxy start
sudo service tor start
```

# Clone repo and create new environment with conda and install packages with pip
```
git clone https://github.com/DDogeee/nms_shopee.git
cd nms_shopee
conda create -n scrapy python==3.10.13
conda activate scrapy
pip install -r requirements.txt
```

# Start Scrapy spider to crawl and dump data to `data.csv`
```
scrapy crawl shopee -O data.csv --logfile log.txt -L INFO
```

# Result 
Crawling speed
```
2024-01-01 19:02:43 [scrapy.extensions.logstats] INFO: Crawled 40 pages (at 40 pages/min), scraped 12816 items (at 12816 items/min)
2024-01-01 19:03:43 [scrapy.extensions.logstats] INFO: Crawled 100 pages (at 60 pages/min), scraped 41056 items (at 28240 items/min)
2024-01-01 19:05:15 [scrapy.extensions.logstats] INFO: Crawled 153 pages (at 53 pages/min), scraped 66215 items (at 25159 items/min)
2024-01-01 19:05:44 [scrapy.extensions.logstats] INFO: Crawled 187 pages (at 34 pages/min), scraped 82960 items (at 16745 items/min)
2024-01-01 19:06:43 [scrapy.extensions.logstats] INFO: Crawled 249 pages (at 62 pages/min), scraped 113950 items (at 30990 items/min)
```

Total product crawled
```
Thời Trang Nam                  9732
Thời Trang Nữ                   9536
Phụ Kiện & Trang Sức Nữ         8489
Mẹ & Bé                         7494
Nhà Cửa & Đời Sống              6970
Bách Hóa Online                 6469
Thiết Bị Điện Tử                5499
Sắc Đẹp                         5473
Ô Tô & Xe Máy & Xe Đạp          5344
Balo & Túi Ví Nam               4922
Máy Tính & Laptop               4921
Túi Ví Nữ                       4695
Nhà Sách Online                 4500
Điện Thoại & Phụ Kiện           4455
Thể Thao & Du Lịch              4000
Sức Khỏe                        4000
Giặt Giũ & Chăm Sóc Nhà Cửa     3923
Thời Trang Trẻ Em               3911
Thiết Bị Điện Gia Dụng          3889
Giày Dép Nam                    3834
Chăm Sóc Thú Cưng               3500
Đồ Chơi                         3000
Máy Ảnh & Máy Quay Phim         2986
Giày Dép Nữ                     2975
Đồng Hồ                         2609
Dụng cụ và thiết bị tiện ích    2500
Voucher & Dịch Vụ                317
```

Time to transform csv file to xlsx file
~ 7.5s for 129943 rows ~ 17326 rows/sec

Detail transform code in [notebook](notebook.ipynb)


