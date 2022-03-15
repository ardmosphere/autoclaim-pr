# autoclaim-pr

requirements:
- hacker's keyboard (5mb)
- termux (20mb)
- python3.9 (430mb)
- git (19mb)

ikuti langkah-langkah berikut untuk menjalankan bot auto claim coin prisga di android.

- install hacker's keyboard, lalu buka, enable input keyboard, back dan masuk settings, ubah 4 row menjadi full 5 row
- install termux, lalu buka, kemudian ketikan command di bawah ini (perbaris) dan enter


- apt-get update
- apt install git
- apt install python3
- pip3 install -r requirements.txt
- git clone https://github.com/ardmosphere/autoclaim-pr
- cd autoclaim-pr
- nano username.txt
- (isi username dan password, lalu ctrl+s dan ctrl+x)
- python3 autoclaim.py

biarkan termux berjalan di background. apabila termux mati atau tidak sengaja tertutup, buka lagi dan jalankan command berikut:
- cd autoclaim-pr
- python3 autoclaim.py

tertanda, Hyena Ganteng.
